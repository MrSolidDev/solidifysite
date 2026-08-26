import { apiRequest } from './api'
import type { CaseStudy, Project, PublicationStatus, ProjectMedia, Technology } from '@/types/content'

export type AdminUser = { id: string; email: string }
export type ProjectPayload = {
  slug: string
  name: string
  tagline: string | null
  short_description: string | null
  full_description: string | null
  status: string | null
  project_url: string | null
  repository_url: string | null
  featured: boolean
  publication_status: PublicationStatus
  technology_ids: string[]
}
export type CasePayload = {
  project_id: string
  slug: string
  title: string
  challenge: string
  solution: string
  architecture: string | null
  results: string
  publication_status: PublicationStatus
}

export const authApi = {
  me: () => apiRequest<AdminUser>('/auth/me'),
  login: (email: string, password: string) => apiRequest<AdminUser>('/auth/login', { method: 'POST', body: JSON.stringify({ email, password }) }),
  logout: () => apiRequest<void>('/auth/logout', { method: 'POST' }),
}

export const adminApi = {
  projects: () => apiRequest<Project[]>('/admin/projects'),
  createProject: (payload: ProjectPayload) => apiRequest<Project>('/admin/projects', { method: 'POST', body: JSON.stringify(payload) }),
  updateProject: (id: string, payload: Partial<ProjectPayload>) => apiRequest<Project>(`/admin/projects/${id}`, { method: 'PATCH', body: JSON.stringify(payload) }),
  deleteProject: (id: string) => apiRequest<void>(`/admin/projects/${id}`, { method: 'DELETE' }),
  cases: () => apiRequest<CaseStudy[]>('/admin/case-studies'),
  createCase: (payload: CasePayload) => apiRequest<CaseStudy>('/admin/case-studies', { method: 'POST', body: JSON.stringify(payload) }),
  updateCase: (id: string, payload: Omit<CasePayload, 'project_id'>) => apiRequest<CaseStudy>(`/admin/case-studies/${id}`, { method: 'PATCH', body: JSON.stringify(payload) }),
  deleteCase: (id: string) => apiRequest<void>(`/admin/case-studies/${id}`, { method: 'DELETE' }),
  technologies: () => apiRequest<Technology[]>('/technologies'),
  createTechnology: (name: string, slug: string) => apiRequest<Technology>('/admin/technologies', { method: 'POST', body: JSON.stringify({ name, slug, icon: null }) }),
  uploadImage: (projectId: string, file: File, alt: string, sortOrder: number) => {
    const body = new FormData()
    body.append('file', file)
    body.append('alt', alt)
    body.append('sort_order', String(sortOrder))
    return apiRequest<ProjectMedia>(`/admin/projects/${projectId}/media/upload`, { method: 'POST', body })
  },
  deleteMedia: (id: string) => apiRequest<void>(`/admin/media/${id}`, { method: 'DELETE' }),
}
