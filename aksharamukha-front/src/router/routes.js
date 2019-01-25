
export default [
  {
    path: '/',
    redirect: '/converter'
  },

  {
    path: '/upload',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/upload-file') }
    ]
  },

  {
    path: '/api',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/api') }
    ]
  },

  {
    path: '/rosetta-stone',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/rosetta-stone') }
    ]
  },

  {
    path: '/help',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/help') }
    ]
  },

  {
    path: '/plugin',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/plugin') }
    ]
  },

  {
    path: '/describe/:script',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/describe') }
    ]
  },

  {
    path: '/website',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/website-convert') }
    ]
  },

  {
    path: '/roman',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/latinmatrix') }
    ]
  },

  {
    path: '/syllabary',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/syllabary') }
    ]
  },

  {
    path: '/conjuncts',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/conjuncts') }
    ]
  },

  {
    path: '/fill',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/fill') }
    ]
  },

  {
    path: '/memory-cards',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/memory-cards') }
    ]
  },

  {
    path: '/script-matrix',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/scriptmatrix') }
    ]
  },

  {
    path: '/flipcards-shuffle',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/flipcards-shuffle') }
    ]
  },

  {
    path: '/match-letter',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/match-letter') }
    ]
  },

  {
    path: '/texts/:text',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/texts') }
    ]
  },

  {
    path: '/about',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/about') }
    ]
  },

  {
    path: '/converter',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/index') }
    ]
  },

  {
    path: '/download',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/download') }
    ]
  },

  /* {
    path: '/input/:script',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/IME') }
    ]
  }, */

  { // Always leave this as last one
    path: '*',
    component: () => import('pages/404')
  }
]
