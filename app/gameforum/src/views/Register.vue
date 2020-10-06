<template>
  <div>
    <button @click="register">注册</button>
  </div>
</template>

<script>
export default {
  methods: {
    register() {
      this.$http
        .post('http://127.0.0.1:8000/register/userReg', {
          username: 'gayu',
          nickname: 'gayu',
          password: 1234567
        })
        .then(res => {
          console.log(res.data)
        })
    }
  }
}
</script>

<style lang="scss" scoped></style>
