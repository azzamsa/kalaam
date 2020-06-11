<template>
  <div class="welcome">
    <p>Show all existing users.</p>
    <b-button variant="primary" @click="getUsers()">
      Show Users
    </b-button>
    <b-table :data="users" :columns="columns"></b-table>
  </div>
</template>

<style scoped>
.welcome {
  text-align: center;
  color: black;
}
</style>

<script>
import axios from "axios"
export default {
  data() {
    return {
      users: [],
      columns: [
        {
          field: "id",
          label: "ID",
          width: "40",
          numeric: true,
        },
        {
          field: "name",
          label: "Name",
        },
        {
          field: "email",
          label: "Email",
        },
        {
          field: "is_active",
          label: "Active",
          centered: true,
        },
        {
          field: "is_superuser",
          label: "Admin",
        },
      ],
    }
  },
  methods: {
    getUsers() {
      axios.get("http://127.0.0.1:8000/v1/users/").then(response => {
        console.log(response.data)
        this.users = response.data
      })
    },
  },
}
</script>
