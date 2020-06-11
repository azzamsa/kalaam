<template>
  <div class="welcome hero">
    <h1 class="title">Hello!</h1>
    <router-link to="/user">
      <b-button variant="primary">Users</b-button>
    </router-link>
  </div>
</template>

<style scoped>
.welcome {
  text-align: center;
  color: green;
}
</style>
