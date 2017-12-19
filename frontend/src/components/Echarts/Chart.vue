<template>
  <div class="echarts">
    <IEcharts :option="bar" :loading="loading" @ready="onReady" @click="onClick"></IEcharts>
    <button   @click="doRandom">Get Bar Chart Comparison</button>
  </div>
</template>

<script type="text/babel">
  import axios from 'axios'
  import IEcharts from 'vue-echarts-v3/src/full.js'
  export default {
    name: 'view',
    components: {
      IEcharts
    },
    props: {
    },
    data: () => ({
      loading: true,
      bar: {
        title: {
          text: 'ECharts Expenses Comparison of Departments'
        },
        tooltip: {},
        xAxis: {
          data: []
        },
        yAxis: [{
          type: 'value',
          scale: true,
          name: 'Expenses'
        }],
        series: [{
          name: 'Sales',
          type: 'bar',
          data: []
        }]
      }
    }),
    methods: {
      doRandom () {
        const that = this
        let data = []
        for (let i = 0, min = 5, max = 99; i < 5; i++) {
          data.push(Math.floor(Math.random() * (max + 1 - min) + min))
        }
        that.loading = !that.loading
        that.bar.series[0].data = data
        console.log('starting')
        // this.loading = true
        axios.get(`http://127.0.0.1:8000/api/billing/`)
        .then(response => {
          let companies = []
          let amounts = []
          for (let i = 0; i < 5; i++) {
            companies.push(response.data[i].company_name + ' ' + response.data[i].department_name)
            amounts.push(response.data[i].amount)
          }
          this.bar.xAxis.data = companies
          this.bar.series[0].data = amounts
          // console.log(response.data)
          // let data = []
          // $$.each(response.data.department_name, function(value, key) {
          //   console.log(value)
        })
        // })
          // this.items = response.data
        .catch(e => {
          this.errors.push(e)
        })
        console.log('Ending')
      },
      onReady (instance) {
        console.log(instance)
      },
      onClick (event, instance, echarts) {
        console.log(arguments)
      },
      created () {
        // console.log('starting')
        // this.loading = true
        // axios.get(`http://127.0.0.1:8000/api/billing/`)
        // .then(response => {
        //   let departments = []
        //   let amounts = []
        //   for (let i = 0; i < response.data.length; i++) {
        //     departments.push(response.data[i].department_name)
        //     amounts.push(response.data[i].amount)
        //   }
        //   this.bar.xAxis.data = departments
        //   this.bar.series[0].data = amounts
        //   // console.log(response.data)
        //   // let data = []
        //   // $$.each(response.data.department_name, function(value, key) {
        //   //   console.log(value)
        // })
        // // })
        //   // this.items = response.data
        // .catch(e => {
        //   this.errors.push(e)
        // })
        // console.log('Ending')
      }
    }
}
</script>

<style scoped>
  .echarts {
    width: 900px;
    height: 400px;
  }
</style>