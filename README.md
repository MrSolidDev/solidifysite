# Solidify

Sitio público de Solidify construido con Vue 3, TypeScript, Vite y Vue Router.

## Rutas

- `/`: landing principal.
- `/projects`: catálogo de productos.
- `/projects/:slug`: detalle de producto.
- `/case-studies`: catálogo de casos de éxito.
- `/case-studies/:slug`: detalle de caso.
- `/admin`: reservada para el CMS; permanecerá protegida hasta incorporar autenticación.

El contenido continúa en `src/data/siteContent.ts`. En la siguiente fase, los componentes podrán conservarse y reemplazar esta fuente por un servicio HTTP.

## Despliegue con Nginx

Vue Router usa history mode. Nginx debe devolver `index.html` para las rutas que no sean archivos físicos:

```nginx
location / {
    try_files $uri $uri/ /index.html;
}
```

Hay una configuración de referencia en `infra/nginx/solidify.conf.example`. Debe adaptarse al dominio, certificado y ubicación utilizados en el VPS.

## API de contenido

El backend está en `api/` y expone documentación interactiva en `/docs`.

1. Copiar `.env.example` como `.env` y reemplazar todos los secretos.
2. Iniciar PostgreSQL y el API con `docker compose up -d --build`.
3. Compose aplicará automáticamente las migraciones antes de iniciar el API.
4. Cargar los productos iniciales con `docker compose exec api python -m scripts.seed`.

Endpoints públicos:

- `GET /api/projects`
- `GET /api/projects/:slug`
- `GET /api/case-studies`
- `GET /api/case-studies/:slug`
- `GET /api/technologies`

## Panel administrativo

El CMS está disponible en `/admin`. Utiliza sesiones opacas almacenadas en PostgreSQL, cookie `HttpOnly`, protección CSRF y contraseñas Argon2. Las credenciales iniciales se toman de `SOLIDIFY_ADMIN_EMAIL` y `SOLIDIFY_ADMIN_PASSWORD`; el comando local crea o actualiza ese usuario automáticamente.

Con `.env.example`, las credenciales exclusivamente locales son `admin@solidify.local` y `change-me-locally`.

En producción es obligatorio establecer `SOLIDIFY_ENVIRONMENT=production` y cambiar `SOLIDIFY_ADMIN_PASSWORD` antes del despliegue. El panel permite administrar productos, tecnologías, imágenes y múltiples casos de éxito opcionales asociados a cada producto.

El frontend consume `/api` por defecto. Durante `npm run dev`, Vite envía esas solicitudes a `http://127.0.0.1:8000`. Si el API vive en otro origen puede definirse `VITE_API_BASE_URL`, aunque en producción se recomienda conservar `/api` detrás de Nginx para evitar CORS adicional.

## Despliegue automático

El workflow de GitHub Actions construye las imágenes `web` y `api`, levanta PostgreSQL, aplica migraciones, ejecuta el seed idempotente y valida el frontend y `/api/projects` a través del contenedor web. Antes del primer despliegue se debe crear manualmente `/opt/apps/solidifysite/.env` y aplicar en Nginx el proxy incluido en la configuración de referencia.

Para pruebas locales del backend:

```sh
cd api
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.txt
.venv/Scripts/python -m pytest
```

## Ejecución local automática

En Windows, el entorno completo puede iniciarse con:

```powershell
npm run local
```

El comando crea un `.env` local si todavía no existe y levanta la plataforma completa en contenedores:

- `web`: construye Vue con Node y sirve `dist` mediante Nginx.
- `api`: ejecuta FastAPI con Uvicorn.
- `db`: ejecuta `postgres:17-alpine`.
- `migrate`: aplica Alembic y termina.

Después ejecuta el seed y comprueba el frontend y los endpoints. El sitio queda disponible en `http://localhost:8080`.

El puerto publicado se controla con `SOLIDIFY_WEB_PORT` en `.env`. Si `8080` ya está ocupado, puede usarse por ejemplo `SOLIDIFY_WEB_PORT=8085`; el proxy Nginx del host debe apuntar al mismo puerto.

Para ejecutar además las pruebas del API (el build de producción ya ocurre dentro de `web`):

```powershell
npm run local:validate
```

Para apagar los contenedores sin borrar la base de datos local:

```powershell
npm run local:stop
```

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) 
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```
