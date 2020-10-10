<template>
  <el-menu
    class="headermenu"
    mode="horizontal"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
  >
    <div class="l-content">
      <p>GameForum</p>
    </div>
    <div class="r-content">
      <el-menu-item index="1"
        ><router-link to="/Login">登录</router-link></el-menu-item
      >
      <el-menu-item index="2">
        <router-link to="/Register">注册</router-link>
      </el-menu-item>
    </div>
  </el-menu>
</template>

<script>
export default {}
</script>

<style lang="stylus" scoped>
.headermenu
    .l-content
        float left
        line-height 56px
        height 56px
        margin 0 20px
        color #fff
        font-family 'STXinwei'
        font-size 30px
    .r-content
        display flex
        align-items center
        justify-content flex-end
        &:last-child
            margin-right 10px
        .el-menu-item
            padding 0 10px
            a
                color #fff
</style>
