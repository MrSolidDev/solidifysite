param(
    [ValidateSet('start', 'validate', 'stop')]
    [string]$Action = 'start'
)

$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ApiPython = Join-Path $ProjectRoot 'api\.venv\Scripts\python.exe'
Set-Location $ProjectRoot

function Write-Step([string]$Message) {
    Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Assert-Command([string]$Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "No se encontro '$Name' en PATH. Instalalo antes de continuar."
    }
}

function Initialize-Environment {
    if (-not (Test-Path '.env')) {
        Copy-Item -LiteralPath '.env.example' -Destination '.env'
        Write-Host 'Se creo .env desde .env.example para desarrollo local.' -ForegroundColor Yellow
        Write-Host 'No utilices estos valores en produccion.' -ForegroundColor Yellow
    }
}

function Wait-ForApi {
    for ($Attempt = 1; $Attempt -le 30; $Attempt++) {
        docker compose exec -T api python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health/ready')" 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host 'API lista.' -ForegroundColor Green
            return
        }
        Start-Sleep -Seconds 2
    }
    docker compose logs --tail 80 api migrate db
    throw 'El API no respondio correctamente despues de 60 segundos.'
}

function Wait-ForWeb {
    $WebAddress = (docker compose port web 80).Trim()
    $WebBaseUrl = "http://$WebAddress"
    for ($Attempt = 1; $Attempt -le 30; $Attempt++) {
        try {
            $Response = Invoke-WebRequest -Uri "$WebBaseUrl/health" -TimeoutSec 3 -UseBasicParsing
            if ($Response.StatusCode -eq 200) {
                Write-Host 'Frontend listo.' -ForegroundColor Green
                return
            }
        }
        catch {
            Start-Sleep -Seconds 2
        }
    }
    docker compose logs --tail 80 web
    throw 'El frontend no respondio correctamente despues de 60 segundos.'
}

function Start-Platform {
    Write-Step 'Levantando web, API, migraciones y PostgreSQL'
    docker compose up -d --build --remove-orphans
    if ($LASTEXITCODE -ne 0) { throw 'docker compose up fallo.' }
    Wait-ForApi
    Wait-ForWeb

    Write-Step 'Cargando contenido inicial'
    docker compose exec -T api python -m scripts.seed
    if ($LASTEXITCODE -ne 0) { throw 'El seed del API fallo.' }
    docker compose exec -T api python -m scripts.create_admin
    if ($LASTEXITCODE -ne 0) { throw 'No fue posible crear el administrador local.' }
}

function Test-Runtime {
    Write-Step 'Validando frontend y endpoints publicos'
    $WebAddress = (docker compose port web 80).Trim()
    $WebBaseUrl = "http://$WebAddress"
    $HomeResponse = Invoke-WebRequest -Uri "$WebBaseUrl/" -TimeoutSec 5 -UseBasicParsing
    $Projects = Invoke-RestMethod -Uri "$WebBaseUrl/api/projects" -TimeoutSec 5
    $Cases = Invoke-RestMethod -Uri "$WebBaseUrl/api/case-studies" -TimeoutSec 5
    if ($HomeResponse.StatusCode -ne 200) { throw 'El frontend no devolvio HTTP 200.' }
    if (@($Projects).Count -lt 1) { throw 'El API no devolvio proyectos publicados.' }
    if (@($Cases).Count -lt 1) { throw 'El API no devolvio casos publicados.' }
    Write-Host "Validacion correcta: frontend, $(@($Projects).Count) proyectos y $(@($Cases).Count) casos." -ForegroundColor Green
}

Assert-Command 'docker'

if ($Action -eq 'stop') {
    Write-Step 'Deteniendo el entorno local'
    docker compose down
    if ($LASTEXITCODE -ne 0) { throw 'No fue posible detener Docker Compose.' }
    exit 0
}

Initialize-Environment
Start-Platform
Test-Runtime

if ($Action -eq 'validate') {
    Write-Step 'Ejecutando pruebas del backend'
    if (-not (Test-Path $ApiPython)) {
        throw 'No existe api/.venv. Crealo e instala api/requirements-dev.txt para ejecutar las pruebas.'
    }
    Push-Location (Join-Path $ProjectRoot 'api')
    try {
        & $ApiPython -m pytest -q -p no:cacheprovider
        if ($LASTEXITCODE -ne 0) { throw 'Las pruebas del backend fallaron.' }
    }
    finally {
        Pop-Location
    }
    Write-Host "`nEntorno local validado correctamente." -ForegroundColor Green
    exit 0
}

$WebAddress = (docker compose port web 80).Trim()
Write-Host "`nSolidify esta disponible en http://$WebAddress" -ForegroundColor Green
Write-Host 'Los contenedores seguiran activos; ejecuta npm run local:stop para apagarlos.' -ForegroundColor DarkGray
