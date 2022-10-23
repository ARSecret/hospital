<template>
  <div class="doctors-block">
    <h2>Список врачей</h2>
    <div class="doctors-cards">
      <DoctorCard v-for="doctor in doctors" :key="doctor" :doctor="doctor"></DoctorCard>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import DoctorCard from '@/components/DoctorCard.vue'

export default defineComponent({
  data: () => ({
    doctors: [] as any[]
  }),
  methods: {
    async getDoctors() {
      try {
        let response = await fetch('http://127.0.0.1:8000/api/doctors/', {
          method: 'GET',
        })
        let doctors = await response.json()
        for (let doctor of doctors) {
          response = await fetch(doctor.speciality)
          doctor.speciality = await response.json()
          this.doctors.push(doctor)
        }
        while (this.doctors.length < 24) {
          this.doctors = this.doctors.concat(this.doctors);
        }
      } catch (error) {
        console.log('Get doctors error:', error)
      }
    }
  },
  components: {
    DoctorCard
  },
  created() {
    this.getDoctors()
  }
})

</script>

<style>
.doctors-cards {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 1em;
}
</style>
