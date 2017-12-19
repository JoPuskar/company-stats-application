import Chart from '@/components/Echarts/Chart'
import PieChart from '@/components/Echarts/PieChart'
import Dashboard from '@/components/Dashboard'
import Router from 'vue-router'
import Vue from 'vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/echarts/chart',
      name: 'Chart',
      component: Chart
    },
    {
      path: '/echarts/chart',
      name: 'PieChart',
      component: PieChart
    }
  ],
  mode: 'history'
})
