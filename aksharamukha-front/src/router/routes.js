
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
    path: '/download',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/download') }
    ]
  },

  {
    path: '/web-api',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/web-api') }
    ]
  },

  {
    path: '/python',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/python') }
    ]
  },

  {
    path: '/explore',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/explore') }
    ]
  },

  {
    path: '/composer',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/composer') }
    ]
  },

  {
    path: '/composer-mp',
    component: () => import('layouts/default-mp'),
    children: [
      { path: '', component: () => import('pages/composer-mp') }
    ]
  },

  {
    path: '/documentation',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/documentation') }
    ]
  },

  {
    path: '/rosetta-stone',
    redirect: '/explore'
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
    path: '/describesemitic/:script',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/describesemitic') }
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
    path: '/semitic-matrix',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/semitic-matrix') }
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

  {
    path: '/input/:script',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/IME') }
    ]
  },

  { // Always leave this as last one
    path: '*',
    redirect: '/converter'
  }
]
