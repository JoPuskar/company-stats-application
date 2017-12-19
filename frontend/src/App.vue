<template>
  <v-app>
  <v-toolbar dark color="primary">
    <v-toolbar-side-icon @click.native.stop="sideNav =!sideNav"></v-toolbar-side-icon>
    <v-toolbar-title class="whitetext"><strong>Expense Live Dashboard</strong></v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon>
      <v-icon>search</v-icon>
    </v-btn>
    <v-btn icon>
      <v-icon>apps</v-icon>
    </v-btn>
    <v-btn icon>
      <v-icon>refresh</v-icon>
    </v-btn>
    <v-btn icon>
      <v-icon>more_vert</v-icon>
    </v-btn>
  </v-toolbar>
    <div id="app">
      <dashboard></dashboard>
      <piechart></piechart>
      <chart></chart>
    </div>
  </v-app>
</template>
<script>
import Dashboard from './components/Dashboard'
import Chart from './components/Echarts/Chart'
import PieChart from './components/Echarts/PieChart'
export default {
  ele: '#app',
  components: {
    Dashboard,
    Chart,
    PieChart
  }
}
</script>