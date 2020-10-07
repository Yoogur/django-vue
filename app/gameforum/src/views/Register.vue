<template>
  <el-row class="box" :span="24">
    <el-card shadow="hover" class="el-cardbox">
      <div slot="header" class="clearfix">
        <span>注册</span>
      </div>
      <common-form
        :form="registerForm"
        :formLabel="registerFormLabel"
        :rules="rules"
        class="form"
      >
        <el-button @click="register" type="primary">注册</el-button>
      </common-form>
    </el-card>
  </el-row>
</template>

<script>
import CommonForm from '../components/CommonForm'
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value !== this.registerForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      rules: {
        nickname: [
          { required: true, message: '昵称不能为空', trigger: 'blur' },
          {
            min: 1,
            max: 6,
            message: '昵称长度在 1 到 6 个字符',
            trigger: 'blur'
          }
        ],
        username: [
          { required: true, message: '用户名不能为空', trigger: 'blur' },
          {
            min: 3,
            max: 5,
            message: '用户名长度在 3 到 5 个字符',
            trigger: 'blur'
          }
        ],
        password: [
          { required: true, message: '密码不能为空', trigger: 'blur' },
          {
            min: 3,
            max: 11,
            message: '密码长度在 3 到 11 个字符',
            trigger: 'blur'
          }
        ],
        checkpass: [
          { required: true, message: '密码不能为空', trigger: 'blur' },
          {
            min: 3,
            max: 11,
            message: '密码长度在 3 到 11 个字符',
            trigger: 'blur'
          },
          { validator: validatePass, trigger: 'blur' }
        ]
      },
      registerForm: {
        username: '',
        nickname: '',
        password: '',
        checkpass: ''
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
        },
        {
          model: 'checkpass',
          label: '确认密码',
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
          if (res.data.result) {
            this.$message({
              message: '注册成功！',
              type: 'success'
            })
          } else {
            this.$message.error('注册失败，用户名已存在！');
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
        height 400px
        padding 20px
        background-color rgba(245,245,245,0.8)
        margin 200px auto
        . form
            height 100%
            width 100%
            margin 0 auto;
            text-align: center
</style>
