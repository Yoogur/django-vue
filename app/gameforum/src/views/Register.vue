<template>
  <el-card shadow="hover" class="box">
    <div slot="header" class="clearfix">
      <span>注册</span>
    </div>
    <common-form :form="registerForm" :formLabel="registerFormLabel" class="form">
      <el-button @click="register" type="primary">注册</el-button>
    </common-form>
  </el-card>
</template>

<script>
import CommonForm from '../components/CommonForm'
export default {
  data() {
    return {
      registerForm: {
        username: '',
        nickname: '',
        password: ''
      },
      registerFormLabel: [
        {
          model: 'nickname',
          label: '昵称'
        },
        {
          model: 'username',
          label: '用户名'
        },
        {
          model: 'password',
          label: '密码',
          type: 'password'
        }
      ]
    }
  },
  components: {
    CommonForm
  },
  methods: {
    register() {
      this.$http
        .post('http://127.0.0.1:8000/register/userReg', this.registerForm)
        .then(res => {
          console.log(res.data)
        })
    }
  }
}
</script>

<style lang="stylus" scoped>
.box
    width 500px
    height 300px
    padding 20px
    margin 100px auto
    . form
        height 100%
        width 100%
        margin 0 auto;
        text-align: center
</style>
