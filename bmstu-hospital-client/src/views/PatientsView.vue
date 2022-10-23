<template>
    <div class="patients-block">
      <h2>Список пациентов</h2>
      <table class="patients-table">
        <thead>
          <tr>
            <th>ФИО</th>
            <th>Пол</th>
            <th>Дата рождения</th>
            <th>Возраст</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in patients" :key="patient.id">
            <td>{{ [patient.last_name, patient.first_name, patient.patronymic].join(' ') }}</td>
            <td>{{ patient.gender ? 'Мужчина' : 'Женщина' }}</td>
            <td>{{ patient.birth_date }}</td>
            <td>{{ patient.age }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script lang="ts">
  import {defineComponent} from 'vue';
  
  export default defineComponent({
    data: () => ({
      patients: [] as any[]
    }),
    created() {
      fetch('http://127.0.0.1:8000/api/patients/', {
        method: 'GET'
      })
        .then(response => response.json())
        .then(patients => {
          this.patients = patients
        })
        .catch(error => {
          console.log(error)
        })
    }
  })
  
  </script>
  
  <style scoped>
  
  </style>
  