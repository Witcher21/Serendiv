const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'journal', component: () => import('pages/JournalPage.vue') },
      { path: 'heritage', component: () => import('pages/HeritagePage.vue') },
      { path: 'wildlife', component: () => import('pages/WildlifePage.vue') },
      { path: 'coastal', component: () => import('pages/CoastalPage.vue') },
      { path: 'aviation', component: () => import('pages/AviationPage.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
