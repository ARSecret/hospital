<template>
  <div class="wards-block">
    <h2>Список палат</h2>
    <table class="wards-table">
      <thead>
        <tr>
          <th>Номер</th>
          <th>Кол-во мест</th>
          <th>Занято мест</th>
          <th>Пациенты</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ward in wards" :key="ward.id">
          <td>{{ ward.number }}</td>
          <td>{{ ward.capacity }}</td>
          <td>{{ ward.patients.length }}</td>
          <td>
            <table class="inner-table">
              <tr v-for="patient in ward.patients" :key="patient.id">
                <td>{{ [patient.last_name, patient.first_name, patient.patronymic].join(' ') }}</td>  
              </tr>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
  
<script lang="ts">
import {defineComponent} from 'vue';
  
export default defineComponent({
  data: () => ({
    wards: [] as any[]
  }),
  methods: {
    async getWards() {
      try {
        let response = await fetch('http://127.0.0.1:8000/api/wards/', {
          method: 'GET'
        });
        let wards = await response.json(); 
        for (let ward of wards) {
          for (let i = 0; i < ward.patients.length; i++) {
            let response = await fetch(ward.patients[i])
            let patient = await response.json();
            ward.patients[i] = patient
          }
        }  
        console.log(wards)
        this.wards = wards
      } catch (error) {
        console.log(error)
      }
    }
  },
  created() {
    this.getWards()
  }
})
  
</script>

<style scoped>

</style>
  