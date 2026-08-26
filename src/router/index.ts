import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: () => import('@/views/HomeView.vue') },
    { path: '/projects', name: 'projects', component: () => import('@/views/ProjectsView.vue') },
    { path: '/projects/:slug', name: 'project-detail', component: () => import('@/views/ProjectDetailView.vue') },
    { path: '/case-studies', name: 'case-studies', component: () => import('@/views/CaseStudiesView.vue') },
    { path: '/case-studies/:slug', name: 'case-study-detail', component: () => import('@/views/CaseStudyDetailView.vue') },
    { path: '/admin', name: 'admin', component: () => import('@/views/admin/AdminView.vue') },
    { path: '/:pathMatch(.*)*', name: 'not-found', component: () => import('@/views/NotFoundView.vue') },
  ],
  scrollBehavior(to, _from, savedPosition) {
    if (savedPosition) return savedPosition
    if (to.hash) return { el: to.hash, top: 80, behavior: 'smooth' }
    return { top: 0 }
  },
})

export default router
