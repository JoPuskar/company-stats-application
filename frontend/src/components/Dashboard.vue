<template>
  <div id="dashboard">
  <v-card>
    <v-card-title>
      Expense Live Dashboard
      <v-spacer></v-spacer>
      <v-text-field
        append-icon="search"
        label="Search"
        single-line
        hide-details
        v-model="search"
      ></v-text-field>
    </v-card-title>
    <v-data-table
        v-bind:headers="headers"
        v-bind:items="items"
        v-bind:search="search"
      >
      <template slot="items" slot-scope="props">
        <td>
          <v-edit-dialog
            lazy
          > {{ props.item.company_name }}
            <v-text-field
              slot="input"
              label="Edit"
              v-model="props.item.company_name"
              single-line
              counter
              :rules="[max25chars]"
            ></v-text-field>
          </v-edit-dialog>
        </td>
        <td class="text-xs-right">{{ props.item.department_name }}</td>
        <td class="text-xs-right">{{ props.item.expenditure_point }}</td>
        <td class="text-xs-right">{{ props.item.amount }}</td>
        <td class="text-xs-right">{{ props.item.payment_date }}</td>
        <td class="text-xs-right">{{ props.item.status }}</td>
        <td class="text-xs-right">{{ props.item.remaining_days }}</td>
          </v-edit-dialog>
        </td>
      </template>
      <template slot="pageText" slot-scope="{ pageStart, pageStop }">
        From {{ pageStart }} to {{ pageStop }}
      </template>
    </v-data-table>
  </v-card>
</div>
</template>
<script>
  import axios from 'axios'
  export default {
    ele: '#dashboard',
    data () {
      return {
        max25chars: (v) => v.length <= 25 || 'Input too long!',
        tmp: '',
        search: '',
        pagination: {},
        headers: [
          {
            text: 'Company',
            align: 'left',
            sortable: true,
            value: 'company'
          },
          { text: 'Department', value: 'department_name' },
          { text: 'Expenditure Point', value: 'expenditure_point' },
          { text: 'Amount', value: 'amount' },
          { text: 'Payment Date', value: 'payment_date' },
          { text: 'Status', value: 'status' },
          { text: 'Remaining Days', value: 'remaining_days' }
        ],
        items: []
      }
    },
    created () {
      axios.get(`http://127.0.0.1:8000/api/company/`)
      .then(response => {
        let billings = []
        for (let i = 0; i < response.data.length; i++) {
          for (let j = 0; j < 7; j++) {
            billings.push(response.data[i].billings[j])
          }
        }
      //   console.log(billings)
        this.items = billings
      })
        // this.items = response.data
      // .catch(e => {
      //   this.errors.push(e)
      // })
    }
}
</script>

