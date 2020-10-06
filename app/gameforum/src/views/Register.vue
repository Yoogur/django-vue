<template>
  <div>
    <button @click="register">注册</button>
    <common-form></common-form>
  </div>
</template>

<script>
import CommonForm from '../components/CommonForm'
export default {
  components: {
    CommonForm,
  },
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
