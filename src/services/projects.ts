import { apiGet } from './api'
import type { Project } from '@/types/content'

export function listProjects(signal?: AbortSignal) {
  return apiGet<Project[]>('/projects', signal)
}

export function getProject(slug: string, signal?: AbortSignal) {
  return apiGet<Project>(`/projects/${encodeURIComponent(slug)}`, signal)
}
