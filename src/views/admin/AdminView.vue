<script setup lang="ts">
import { computed, onMounted, reactive, ref } from 'vue'
import { adminApi, authApi, type AdminUser, type CasePayload, type ProjectPayload } from '@/services/admin'
import type { CaseStudy, Project, PublicationStatus, Technology } from '@/types/content'

const user = ref<AdminUser | null>(null)
const checkingSession = ref(true)
const busy = ref(false)
const message = ref('')
const error = ref('')
const projects = ref<Project[]>([])
const cases = ref<CaseStudy[]>([])
const technologies = ref<Technology[]>([])
const selectedId = ref<string | null>(null)
const selectedCaseId = ref<string | null>(null)
const loginForm = reactive({ email: '', password: '' })
const technologyForm = reactive({ name: '', slug: '' })
const uploadForm = reactive<{ file: File | null; alt: string }>({ file: null, alt: '' })

const emptyProject = (): ProjectPayload => ({
  slug: '', name: '', tagline: null, short_description: null, full_description: null,
  status: 'En desarrollo', project_url: null, repository_url: null, featured: false,
  publication_status: 'draft', technology_ids: [],
})
const projectForm = reactive<ProjectPayload>(emptyProject())
const caseForm = reactive<CasePayload>({
  project_id: '', slug: '', title: '', challenge: '', solution: '', architecture: null,
  results: '', publication_status: 'draft',
})

const selectedProject = computed(() => projects.value.find((item) => item.id === selectedId.value) ?? null)
const productCases = computed(() => cases.value.filter((item) => item.project_id === selectedId.value))
const selectedCase = computed(() => cases.value.find((item) => item.id === selectedCaseId.value) ?? null)

function slugify(value: string) {
  return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
}

function clearNotices() { message.value = ''; error.value = '' }
function nullable(value: string | null) { return value?.trim() || null }
function chooseUpload(event: Event) { uploadForm.file = (event.target as HTMLInputElement).files?.[0] ?? null }

async function loadContent(preferredId?: string) {
  const [projectData, caseData, technologyData] = await Promise.all([adminApi.projects(), adminApi.cases(), adminApi.technologies()])
  projects.value = projectData
  cases.value = caseData
  technologies.value = technologyData
  if (preferredId) selectProject(preferredId)
}

function newProject() {
  selectedId.value = null
  selectedCaseId.value = null
  Object.assign(projectForm, emptyProject())
  Object.assign(caseForm, { project_id: '', slug: '', title: '', challenge: '', solution: '', architecture: null, results: '', publication_status: 'draft' as PublicationStatus })
  clearNotices()
}

function selectProject(id: string) {
  const project = projects.value.find((item) => item.id === id)
  if (!project) return
  selectedId.value = id
  Object.assign(projectForm, {
    slug: project.slug, name: project.name, tagline: project.tagline,
    short_description: project.short_description, full_description: project.full_description,
    status: project.status, project_url: project.project_url, repository_url: project.repository_url,
    featured: project.featured, publication_status: project.publication_status,
    technology_ids: project.technologies.map((item) => item.id),
  })
  const study = cases.value.find((item) => item.project_id === id)
  selectedCaseId.value = study?.id ?? null
  Object.assign(caseForm, study ? {
    project_id: id, slug: study.slug, title: study.title, challenge: study.challenge,
    solution: study.solution, architecture: study.architecture, results: study.results,
    publication_status: study.publication_status,
  } : { project_id: id, slug: '', title: '', challenge: '', solution: '', architecture: null, results: '', publication_status: 'draft' as PublicationStatus })
  clearNotices()
}

function newCase() {
  if (!selectedId.value) return
  selectedCaseId.value = null
  Object.assign(caseForm, { project_id: selectedId.value, slug: '', title: '', challenge: '', solution: '', architecture: null, results: '', publication_status: 'draft' as PublicationStatus })
  clearNotices()
}

function selectCase(id: string) {
  const study = cases.value.find((item) => item.id === id)
  if (!study) return
  selectedCaseId.value = id
  Object.assign(caseForm, { project_id: study.project_id, slug: study.slug, title: study.title, challenge: study.challenge, solution: study.solution, architecture: study.architecture, results: study.results, publication_status: study.publication_status })
  clearNotices()
}

async function login() {
  busy.value = true; clearNotices()
  try { user.value = await authApi.login(loginForm.email, loginForm.password); await loadContent() }
  catch (reason) { error.value = reason instanceof Error ? reason.message : 'No fue posible iniciar sesión.' }
  finally { busy.value = false }
}

async function logout() {
  try { await authApi.logout() } finally { user.value = null; projects.value = []; newProject() }
}

async function saveProject() {
  busy.value = true; clearNotices()
  try {
    const payload = { ...projectForm, tagline: nullable(projectForm.tagline), short_description: nullable(projectForm.short_description), full_description: nullable(projectForm.full_description), status: nullable(projectForm.status), project_url: nullable(projectForm.project_url), repository_url: nullable(projectForm.repository_url) }
    const saved = selectedId.value ? await adminApi.updateProject(selectedId.value, payload) : await adminApi.createProject(payload)
    await loadContent(saved.id)
    message.value = 'Producto guardado correctamente.'
  } catch (reason) { error.value = reason instanceof Error ? reason.message : 'No fue posible guardar.' }
  finally { busy.value = false }
}

async function removeProject() {
  if (!selectedId.value || !confirm('¿Eliminar este producto y todo su contenido?')) return
  busy.value = true
  try { await adminApi.deleteProject(selectedId.value); await loadContent(); newProject() }
  catch (reason) { error.value = reason instanceof Error ? reason.message : 'No fue posible eliminar.' }
  finally { busy.value = false }
}

async function saveCase() {
  if (!selectedId.value) return
  busy.value = true; clearNotices()
  try {
    const payload = { ...caseForm, project_id: selectedId.value, architecture: nullable(caseForm.architecture) }
    let saved: CaseStudy
    if (selectedCase.value) {
      const { project_id: _projectId, ...changes } = payload
      saved = await adminApi.updateCase(selectedCase.value.id, changes)
    } else saved = await adminApi.createCase(payload)
    await loadContent(selectedId.value)
    selectCase(saved.id)
    message.value = 'Caso de éxito guardado.'
  } catch (reason) { error.value = reason instanceof Error ? reason.message : 'No fue posible guardar el caso.' }
  finally { busy.value = false }
}

async function removeCase() {
  if (!selectedCase.value || !confirm('¿Eliminar el caso de éxito?')) return
  busy.value = true
  try { await adminApi.deleteCase(selectedCase.value.id); await loadContent(selectedId.value ?? undefined); newCase(); message.value = 'Caso eliminado.' }
  finally { busy.value = false }
}

async function addTechnology() {
  if (!technologyForm.name.trim()) return
  busy.value = true; clearNotices()
  try {
    const created = await adminApi.createTechnology(technologyForm.name.trim(), technologyForm.slug || slugify(technologyForm.name))
    technologies.value.push(created); projectForm.technology_ids.push(created.id)
    technologyForm.name = ''; technologyForm.slug = ''
  } catch (reason) { error.value = reason instanceof Error ? reason.message : 'No fue posible crear la tecnología.' }
  finally { busy.value = false }
}

async function uploadImage() {
  if (!selectedId.value || !uploadForm.file) return
  busy.value = true; clearNotices()
  try {
    const nextOrder = Math.max(-1, ...(selectedProject.value?.media.map((item) => item.sort_order) ?? [])) + 1
    await adminApi.uploadImage(selectedId.value, uploadForm.file, uploadForm.alt, nextOrder)
    uploadForm.file = null; uploadForm.alt = ''; await loadContent(selectedId.value); message.value = 'Imagen cargada.'
  } catch (reason) { error.value = reason instanceof Error ? reason.message : 'No fue posible cargar la imagen.' }
  finally { busy.value = false }
}

async function removeMedia(id: string) {
  if (!confirm('¿Eliminar esta imagen?')) return
  await adminApi.deleteMedia(id)
  await loadContent(selectedId.value ?? undefined)
}

onMounted(async () => {
  try { user.value = await authApi.me(); await loadContent() } catch { user.value = null } finally { checkingSession.value = false }
})
</script>

<template>
  <main class="min-h-screen bg-[#091011] text-white">
    <div v-if="checkingSession" class="grid min-h-screen place-items-center"><i class="pi pi-spin pi-spinner text-3xl text-orange-300"></i></div>
    <section v-else-if="!user" class="grid min-h-screen place-items-center px-5">
      <form class="glass-card w-full max-w-md rounded-3xl p-8" @submit.prevent="login">
        <RouterLink :to="{ name: 'home' }" class="text-sm text-white/50"><i class="pi pi-arrow-left mr-2"></i>Volver al sitio</RouterLink>
        <p class="eyebrow mt-10">Solidify CMS</p><h1 class="mt-3 text-3xl font-semibold">Administración</h1>
        <label class="mt-8 block text-sm">Correo<input v-model="loginForm.email" type="email" autocomplete="username" required class="admin-input mt-2" /></label>
        <label class="mt-5 block text-sm">Contraseña<input v-model="loginForm.password" type="password" autocomplete="current-password" minlength="8" required class="admin-input mt-2" /></label>
        <p v-if="error" class="mt-4 text-sm text-red-300">{{ error }}</p>
        <button :disabled="busy" class="mt-7 w-full rounded-xl bg-orange-400 px-5 py-3 font-semibold text-[#091011] disabled:opacity-50">{{ busy ? 'Ingresando…' : 'Ingresar' }}</button>
      </form>
    </section>

    <template v-else>
      <header class="border-b border-white/8 bg-[#0d1516]"><div class="mx-auto flex h-20 max-w-[1500px] items-center justify-between px-5"><div><b class="tracking-widest">SOLIDIFY</b><span class="ml-3 text-xs text-white/40">CMS</span></div><div class="flex items-center gap-4"><RouterLink :to="{ name: 'home' }" target="_blank" class="text-sm text-white/55">Ver sitio <i class="pi pi-external-link ml-1"></i></RouterLink><button class="text-sm text-orange-300" @click="logout">Salir</button></div></div></header>
      <div class="mx-auto grid max-w-[1500px] lg:grid-cols-[300px_1fr]">
        <aside class="border-b border-white/8 bg-[#0b1213] p-5 lg:min-h-[calc(100vh-5rem)] lg:border-r lg:border-b-0">
          <button class="w-full rounded-xl bg-orange-400 px-4 py-3 font-semibold text-[#091011]" @click="newProject"><i class="pi pi-plus mr-2"></i>Nuevo producto</button>
          <div class="mt-6 space-y-2"><button v-for="project in projects" :key="project.id" class="w-full rounded-xl p-4 text-left transition" :class="selectedId === project.id ? 'bg-white/10' : 'hover:bg-white/5'" @click="selectProject(project.id)"><span class="block font-medium">{{ project.name }}</span><span class="mt-1 flex items-center gap-2 text-xs text-white/40"><span>{{ project.publication_status }}</span><span v-if="project.case_studies.length" class="text-emerald-300">· {{ project.case_studies.length }} {{ project.case_studies.length === 1 ? 'caso' : 'casos' }}</span></span></button></div>
        </aside>

        <section class="p-5 sm:p-8 lg:p-10">
          <div class="mx-auto max-w-5xl">
            <div class="flex flex-wrap items-start justify-between gap-4"><div><p class="eyebrow">{{ selectedId ? 'Editar producto' : 'Nuevo producto' }}</p><h1 class="mt-2 text-3xl font-semibold">{{ projectForm.name || 'Sin título' }}</h1></div><button v-if="selectedId" class="text-sm text-red-300" @click="removeProject">Eliminar producto</button></div>
            <p v-if="message" class="mt-6 rounded-xl bg-emerald-300/10 p-4 text-sm text-emerald-200">{{ message }}</p><p v-if="error" class="mt-6 rounded-xl bg-red-300/10 p-4 text-sm text-red-200">{{ error }}</p>

            <form class="glass-card mt-7 grid gap-5 rounded-3xl p-6 sm:grid-cols-2 sm:p-8" @submit.prevent="saveProject">
              <label class="admin-label">Nombre<input v-model="projectForm.name" required maxlength="200" class="admin-input" @blur="!projectForm.slug && (projectForm.slug = slugify(projectForm.name))" /></label>
              <label class="admin-label">Slug<input v-model="projectForm.slug" required pattern="[a-z0-9]+(?:-[a-z0-9]+)*" class="admin-input" /></label>
              <label class="admin-label sm:col-span-2">Tagline<input v-model="projectForm.tagline" maxlength="300" class="admin-input" /></label>
              <label class="admin-label sm:col-span-2">Descripción corta<textarea v-model="projectForm.short_description" rows="3" class="admin-input"></textarea></label>
              <label class="admin-label sm:col-span-2">Descripción completa<textarea v-model="projectForm.full_description" rows="6" class="admin-input"></textarea></label>
              <label class="admin-label">Estado<input v-model="projectForm.status" maxlength="100" class="admin-input" /></label>
              <label class="admin-label">Publicación<select v-model="projectForm.publication_status" class="admin-input"><option value="draft">Borrador</option><option value="published">Publicado</option><option value="archived">Archivado</option></select></label>
              <label class="admin-label">URL del producto<input v-model="projectForm.project_url" type="url" class="admin-input" /></label>
              <label class="admin-label">Repositorio<input v-model="projectForm.repository_url" type="url" class="admin-input" /></label>
              <label class="flex items-center gap-3 text-sm"><input v-model="projectForm.featured" type="checkbox" /> Producto destacado</label>
              <fieldset class="sm:col-span-2"><legend class="admin-label">Tecnologías</legend><div class="mt-3 flex flex-wrap gap-3"><label v-for="technology in technologies" :key="technology.id" class="rounded-full border border-white/10 px-3 py-2 text-xs"><input v-model="projectForm.technology_ids" type="checkbox" :value="technology.id" class="mr-2" />{{ technology.name }}</label></div><div class="mt-4 flex gap-2"><input v-model="technologyForm.name" placeholder="Nueva tecnología" class="admin-input" /><button type="button" class="rounded-xl border border-white/15 px-4 text-sm" @click="addTechnology">Agregar</button></div></fieldset>
              <button :disabled="busy" class="rounded-xl bg-orange-400 px-5 py-3 font-semibold text-[#091011] disabled:opacity-50 sm:col-span-2">Guardar producto</button>
            </form>

            <section v-if="selectedProject" class="glass-card mt-7 rounded-3xl p-6 sm:p-8">
              <p class="eyebrow">Media</p><h2 class="mt-2 text-xl font-semibold">Imágenes</h2>
              <div v-if="selectedProject.media.length" class="mt-5 grid gap-4 sm:grid-cols-3"><figure v-for="media in selectedProject.media" :key="media.id" class="overflow-hidden rounded-xl bg-black/20"><img :src="media.url" :alt="media.alt" class="aspect-video w-full object-cover" /><figcaption class="flex items-center justify-between gap-2 p-3 text-xs text-white/50"><span class="truncate">{{ media.alt || 'Sin texto alternativo' }}</span><button class="text-red-300" @click="removeMedia(media.id)"><i class="pi pi-trash"></i></button></figcaption></figure></div>
              <div class="mt-5 grid gap-3 sm:grid-cols-[1fr_1fr_auto]"><input type="file" accept="image/jpeg,image/png,image/webp,image/gif" class="admin-input" @change="chooseUpload" /><input v-model="uploadForm.alt" placeholder="Texto alternativo" class="admin-input" /><button :disabled="!uploadForm.file || busy" class="rounded-xl border border-white/15 px-5 disabled:opacity-40" @click="uploadImage">Subir</button></div>
            </section>

            <section v-if="selectedId" class="glass-card mt-7 rounded-3xl p-6 sm:p-8">
              <div class="flex flex-wrap items-start justify-between gap-4"><div><p class="eyebrow">Opcional</p><h2 class="mt-2 text-2xl font-semibold">Casos de éxito</h2><p class="muted mt-2 text-sm">Puedes asociar varios casos; sólo aparecen públicamente cuando están publicados.</p></div><button class="rounded-xl border border-emerald-300/30 px-4 py-2 text-sm text-emerald-200" @click="newCase"><i class="pi pi-plus mr-2"></i>Nuevo caso</button></div>
              <div v-if="productCases.length" class="mt-5 flex flex-wrap gap-2"><button v-for="study in productCases" :key="study.id" class="rounded-full border px-4 py-2 text-sm" :class="selectedCaseId === study.id ? 'border-emerald-300/50 bg-emerald-300/10 text-emerald-200' : 'border-white/10 text-white/55'" @click="selectCase(study.id)">{{ study.title }}</button></div>
              <form class="mt-7 grid gap-5 sm:grid-cols-2" @submit.prevent="saveCase"><div class="sm:col-span-2"><h3 class="text-lg font-semibold">{{ selectedCase ? 'Editar caso' : 'Nuevo caso' }}</h3></div><label class="admin-label">Título<input v-model="caseForm.title" required class="admin-input" /></label><label class="admin-label">Slug<input v-model="caseForm.slug" required class="admin-input" @focus="!caseForm.slug && (caseForm.slug = `${projectForm.slug}-caso-${productCases.length + 1}`)" /></label><label class="admin-label sm:col-span-2">Reto<textarea v-model="caseForm.challenge" required rows="4" class="admin-input"></textarea></label><label class="admin-label sm:col-span-2">Solución<textarea v-model="caseForm.solution" required rows="4" class="admin-input"></textarea></label><label class="admin-label sm:col-span-2">Arquitectura<textarea v-model="caseForm.architecture" rows="4" class="admin-input"></textarea></label><label class="admin-label sm:col-span-2">Resultados<textarea v-model="caseForm.results" required rows="4" class="admin-input"></textarea></label><label class="admin-label">Publicación<select v-model="caseForm.publication_status" class="admin-input"><option value="draft">Borrador</option><option value="published">Publicado</option><option value="archived">Archivado</option></select></label><div class="flex items-end justify-end gap-4"><button v-if="selectedCase" type="button" class="text-sm text-red-300" @click="removeCase">Eliminar caso</button><button :disabled="busy" class="rounded-xl bg-emerald-300 px-5 py-3 font-semibold text-[#091011]">Guardar caso</button></div></form>
            </section>
          </div>
        </section>
      </div>
    </template>
  </main>
</template>

<style scoped>
.admin-label { display: block; font-size: .8rem; color: rgba(255,255,255,.62); }
.admin-input { display: block; width: 100%; margin-top: .5rem; border: 1px solid rgba(255,255,255,.12); border-radius: .75rem; background: rgba(255,255,255,.045); padding: .75rem .9rem; color: white; outline: none; }
.admin-input:focus { border-color: rgba(255,157,46,.65); }
select.admin-input option { background: #10191a; }
</style>
