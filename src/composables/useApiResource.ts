import { onBeforeUnmount, onMounted, ref, type Ref } from 'vue'

export function useApiResource<T>(loader: (signal: AbortSignal) => Promise<T>) {
  const data = ref<T | null>(null) as Ref<T | null>
  const loading = ref(true)
  const error = ref<string | null>(null)
  let controller: AbortController | null = null

  async function load() {
    controller?.abort()
    controller = new AbortController()
    loading.value = true
    error.value = null
    try {
      data.value = await loader(controller.signal)
    } catch (reason) {
      if (reason instanceof DOMException && reason.name === 'AbortError') return
      error.value = reason instanceof Error ? reason.message : 'Ocurrió un error inesperado.'
    } finally {
      loading.value = false
    }
  }

  onMounted(load)
  onBeforeUnmount(() => controller?.abort())

  return { data, loading, error, reload: load }
}
