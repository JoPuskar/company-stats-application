<template>
  <div class="piecharts">
    <IEcharts :option="option"></IEcharts>
  </div>
</template>

<script type="text/babel">
  import axios from 'axios'
  import IEcharts from 'vue-echarts-v3/src/full.js'
  import 'echarts/lib/chart/pie'
  export default {
    name: 'view',
    components: {
      IEcharts
    },
    props: {
    },
    data: () => ({
      option: {
        backgroundColor: '#2c343c',

        title: {
          text: 'Department Expenses In Pie Chart',
          left: 'center',
          top: 20,
          textStyle: {
            color: '#ccc'
          }
        },

        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },

        visualMap: {
          show: false,
          min: 80,
          max: 600,
          inRange: {
            colorLightness: [0, 1]
          }
        },
        series: [
          {
            name: 'Department Expenses Pie Chart',
            type: 'pie',
            radius: '55%',
            center: ['50%', '50%'],
            data: [].sort(function (a, b) { return a.value - b.value }),
            roseType: 'radius',
            label: {
              normal: {
                textStyle: {
                  color: 'rgba(255, 255, 255, 0.3)'
                }
              }
            },
            labelLine: {
              normal: {
                lineStyle: {
                  color: 'rgba(255, 255, 255, 0.3)'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
              }
            },
            itemStyle: {
              normal: {
                color: '#c23531',
                shadowBlur: 200,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },

            animationType: 'scale',
            animationEasing: 'elasticOut',
            animationDelay: function (idx) {
              return Math.random() * 200
            }
          }
        ]
      }
    }),
    created () {
      axios.get(`http://127.0.0.1:8000/api/billings/`)
      .then(response => {
        let billings = []
        for (let i = 0; i < response.data.length; i++) {
          // for (let j = 0; j < 7; j++) {
          billings.push(response.data[i].department_name)
          billings.push(response.data[i].amount)
          // }
        }
        console.log(billings)
        console.log('starting')
        this.option.series[0].data = billings
        // console.log(billings)
        console.log('Ending')
      })
        // this.items = response.data
      // .catch(e => {
      //   this.errors.push(e)
      // })
    }
}
</script>
<style scoped>
  .piecharts {
    width: 100px;
    height: 300px;
  }
</style>