<template>
  <div class="single-doctor-block">
    <p v-if="doctor === undefined">Загрузка...</p>
    <p v-else-if="doctor === null">Доктор с ID = {{ id }} не найден</p>
    <div class="doctor-block" v-else>
      <h2>{{ [doctor.last_name, doctor.first_name, doctor.patronymic].join(' ') }}</h2>
      <img v-if="doctor.photo" :src="doctor.photo">
      <img v-else-if="doctor.gender == 1" height=500 src="@/assets/placeholder_male.jpg">
      <img v-else height=500 src="@/assets/placeholder_female.jpg">
      <div>
        <h3>{{ doctor.speciality.name }}</h3>
        <p>{{ doctor.speciality.description }}</p>
        <br>
        <h3>Стаж</h3>
        <p>{{ years_to_str(doctor.work_record) }}</p>
        <br>
        <div v-if="doctor.speciality.doctors.length">
          <h3>Врачи с той же специальностью</h3>
          <RouterLink
            v-for="similar_doctor in doctor.speciality.doctors" 
            :key="similar_doctor.id" 
            :to="'/doctors/' + similar_doctor.id">
            <p>{{ [similar_doctor.last_name, similar_doctor.first_name, similar_doctor.patronymic].join(' ') }}</p>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';

export default defineComponent({
  data: () => ({
    doctor: undefined as any,
    id: undefined as any
  }),
  methods: {
    async getDoctor() {
      try {
        this.id = this.$route.params.id
        let response = await fetch('http://127.0.0.1:8000/api/doctors/' + this.id, {
          method: 'GET',
        })
        if (response.status == 404) {
          this.doctor = null
        } else {
          let doctor = await response.json()
          console.log(doctor)
          response = await fetch(doctor.speciality)
          doctor.speciality = await response.json()
          let similar_doctors = []
          for (let similar_doctor_url of doctor.speciality.doctors) {
            response = await fetch(similar_doctor_url)
            let similar_doctor = await response.json()
            if (similar_doctor.id != doctor.id) {
              similar_doctors.push(similar_doctor)
            }
          }
          doctor.speciality.doctors = similar_doctors
          this.doctor = doctor
        }
      } catch (error) {
        console.log('Get doctors error:', error)
      }
    },
    years_to_str(years: number) {
      let txt;
      let count = years % 100;
      if (count >= 5 && count <= 20) {
        txt = 'лет';
      } else {
        count = count % 10;
        if (count == 1) {
          txt = 'год';
        } else if (count >= 2 && count <= 4) {
          txt = 'года';
        } else {
          txt = 'лет';
        }
      }
      return years + " " + txt;
    }
  },
  created() {
    this.getDoctor()
    this.$watch(
      () => this.$route.params,
      () => {
        console.log('watcher')
        this.getDoctor()
      })
  }
})

</script>

<style>
.doctor-block {
  display: grid;
  grid-template: auto 1fr / auto 1fr;
  gap: 1em;
}

.doctor-block h2 {
  grid-column: span 2;
}
/* 
.doctor-block p {
  margin-bottom: 1em;
} */
</style>
