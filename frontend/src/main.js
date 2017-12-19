import Vue from 'vue'
import '../node_modules/vuetify/src/stylus/app.styl'
import router from './router'
import vueResource from 'vue-resource'
import App from './App'
import ECharts from 'vue-echarts/components/ECharts.vue'
// import IEcharts from 'vue-echarts-v3/src/full.js'

// import 'echarts/lib/chart/line';
import 'echarts/lib/chart/bar'
import 'echarts/lib/chart/pie'
import 'echarts/lib/component/title'

// import ECharts modules manually to reduce bundle size
import 'echarts/lib/component/tooltip'

import {
  Vuetify,
  VApp,
  VDataTable,
  VNavigationDrawer,
  VFooter,
  VList,
  VBtn,
  VIcon,
  VGrid,
  VToolbar,
  transitions
} from 'vuetify'

Vue.use(Vuetify, {
  components: {
    VApp,
    VDataTable,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
    transitions
  }
})

// Vue.component('chart', ECharts)
Vue.use(ECharts)
Vue.use(vueResource)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
