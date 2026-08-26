import { apiGet } from './api'
import type { CaseStudy } from '@/types/content'

export function listCaseStudies(signal?: AbortSignal) {
  return apiGet<CaseStudy[]>('/case-studies', signal)
}

export function getCaseStudy(slug: string, signal?: AbortSignal) {
  return apiGet<CaseStudy>(`/case-studies/${encodeURIComponent(slug)}`, signal)
}
