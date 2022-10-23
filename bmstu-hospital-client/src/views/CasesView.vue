<template>
  <div class="wards-block">
    <h2>Список палат</h2>
    <table class="wards-table">
      <thead>
        <tr>
          <th>Дата поступления</th>
          <th>Выписан</th>
          <th>Дата выписки</th>
          <th>Пациент</th>
          <th>Врач</th>
          <th>Номер палаты</th>
          <th>Описание</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="case_ in cases" :key="case_.id">
          <td>{{ case_.start_date }}</td>
          <td>{{ case_.active ? 'Нет' : 'Да' }}</td>
          <td>{{ case_.end_date || 'Нет' }}</td>
          <td>{{ [case_.patient.last_name, case_.patient.first_name, case_.patient.patronymic].join(' ') }}</td>
          <td>{{ [case_.doctor.last_name, case_.doctor.first_name, case_.doctor.patronymic].join(' ') }}</td>
          <td>{{ case_.ward ? case_.ward.number : 'Нет' }}</td>
          <td>{{ case_.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
  
<script lang="ts">
import {defineComponent} from 'vue';
  
export default defineComponent({
  data: () => ({
    cases: [] as any[]
  }),
  methods: {
    async getCases() {
      try {
        let response = await fetch('http://127.0.0.1:8000/api/cases/', {
          method: 'GET'
        });
        let cases = await response.json(); 
        for (let case_ of cases) {
          case_.patient = await (await fetch(case_.patient)).json()
          case_.doctor = await (await fetch(case_.doctor)).json()
          case_.ward = await (await fetch(case_.ward)).json()
        }
        this.cases = cases
      } catch (error) {
        console.log(error)
      }
    }
  },
  created() {
    this.getCases()
  }
})
  
</script>

<style scoped>

</style>
  