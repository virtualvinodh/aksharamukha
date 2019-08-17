import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'

Vue.use(VueRouter)

const Router = new VueRouter({
  /*
   * NOTE! Change Vue Router mode from quasar.conf.js -> build -> vueRouterMode
   *
   * When going with "history" mode, please also make sure "build.publicPath"
   * is set to something other than an empty string.
   * Example: '/' instead of ''
   */

  // Leave as is and change from quasar.conf.js instead!
  mode: process.env.VUE_ROUTER_MODE,
  base: process.env.VUE_ROUTER_BASE,
  scrollBehavior: () => ({ y: 0 }),
  routes
})

Router.beforeEach((to, from, next) => {
  // Redirect if fullPath begins with a hash (ignore hashes later in path)
  if (to.fullPath.substr(0, 2) === '/#') {
    const path = to.fullPath.substr(2)
    next(path)
    return
  }
  if (to.fullPath.substr(0, 12) === '/converter#/') {
    console.log('here 222')
    const path = to.fullPath.substr(12)
    next(path)
    return
  }
  next()
})

export default Router
