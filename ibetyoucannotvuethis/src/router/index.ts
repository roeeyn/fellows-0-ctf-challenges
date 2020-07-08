import Vue from 'vue'
import VueRouter from 'vue-router'
import EntryPointView from '../views/EntryPointView.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'EntryPointView',
    component: EntryPointView
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = new VueRouter({
  routes
})

export default router
