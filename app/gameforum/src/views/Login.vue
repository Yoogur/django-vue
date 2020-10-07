<template>
  <div>
    <button @click="login">登录</button>
    <button>登录</button>
  </div>
</template>

<script>
export default {
  methods: {
    login() {
      this.$http
        .get('http://127.0.0.1:8000/login/userLogin', {
          params: { username: 'gayu', password: 1234567 }
        })
        .then(res => {
          console.log(res.data)
        })
    }
  }
}
</script>

<style lang="scss" scoped></style>
