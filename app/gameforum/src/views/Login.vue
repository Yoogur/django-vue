<template>
  <el-row class="box" :span="24">
    <el-card shadow="hover" class="el-cardbox">
      <div slot="header" class="clearfix">
        <span>登录</span>
      </div>
      <common-form
        :form="LoginForm"
        :formLabel="LoginFormLabel"
        class="form"
        :rules="rules"
      >
        <el-button
          @click="login"
          type="primary"
          style="width:100%;margin-bottom:20px"
          >登录</el-button
        >
        <el-button type="primary" style="width:100%;margin:0" @click="$router.push({name:'Register'})"
          >没有账号？立即注册</el-button
        >
      </common-form>
    </el-card>
  </el-row>
</template>

<script>
import CommonForm from '../components/CommonForm'
export default {
  data() {
    return {
      rules: {
        username: [
          { required: true, message: '用户名不能为空', trigger: 'blur' }
        ],
        password: [{ required: true, message: '密码不能为空', trigger: 'blur' }]
      },
      LoginForm: {
        username: '',
        password: ''
      },
      LoginFormLabel: [
        {
          model: 'username',
          label: '用户名',
        },
        {
          model: 'password',
          label: '密码',
          type: 'password',
        }
      ]
    }
  },
  components: {
    CommonForm
  },
  methods: {
    login() {
      this.$http
        .get('http://127.0.0.1:8000/user/login', { params: this.LoginForm })
        .then(res => {
          console.log(res.data)
          if (!res.data.result) {
            this.$message.error('用户名或密码错误！')
          }
        })
    }
  }
}
</script>

<style lang="stylus" scoped>
.box
    height 100vh
    background url(../assets/images/background.jpg) no-repeat center center/100% 100%
    .el-cardbox
        width 500px
        height 300px
        padding 20px
        background-color rgba(245,245,245,0.8)
        margin 200px auto
        . form
            height 100%
            width 100%
            margin 0 auto;
            text-align: center
</style>
