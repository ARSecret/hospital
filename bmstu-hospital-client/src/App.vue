<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <h1>Моя больница</h1>

    <nav> 
      <RouterLink to="/">Главная</RouterLink>
      <RouterLink to="/doctors">Список врачей</RouterLink>
      <RouterLink to="/patients">Список пациентов</RouterLink>
      <RouterLink to="/wards">Список палат</RouterLink>
      <RouterLink to="/cases">История болезней</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style>

header {
  margin-bottom: 1rem;
}

nav {
  display: flex;
  flex-wrap: wrap;
  column-gap: 1em;
  border-collapse: collapse;
  row-gap: 1em;
  /* border-left: 1px solid black; */
}

nav a {
  padding: 0 1em 0 1em;
  border: 1px solid black;
  text-decoration: none;
  color: inherit;
  font-size: 18px;
}

nav a.router-link-active {
  background-color: black;
  color: white;
}
</style>
