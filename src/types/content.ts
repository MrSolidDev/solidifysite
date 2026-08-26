export type PublicationStatus = 'draft' | 'published' | 'archived'

export type Technology = {
  id: string
  name: string
  slug: string
  icon: string | null
}

export type ProjectMedia = {
  id: string
  project_id: string
  type: 'image' | 'video' | 'demo'
  url: string
  alt: string
  sort_order: number
}

export type CaseStudySummary = {
  id: string
  slug: string
  title: string
  challenge: string
  results: string
}

export type Project = {
  id: string
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
  published_at: string | null
  created_at: string
  updated_at: string
  technologies: Technology[]
  media: ProjectMedia[]
  case_studies: CaseStudySummary[]
}

export type ProjectSummary = Pick<Project, 'id' | 'slug' | 'name' | 'tagline' | 'technologies'>

export type CaseStudy = {
  id: string
  project_id: string
  slug: string
  title: string
  challenge: string
  solution: string
  architecture: string | null
  results: string
  publication_status: PublicationStatus
  published_at: string | null
  created_at: string
  updated_at: string
  project: ProjectSummary
}
