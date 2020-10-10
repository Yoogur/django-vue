<template>
    <el-container>
      <el-header><common-header></common-header></el-header>
      <el-main>Main</el-main>
    </el-container>
</template>

<script>
import CommonHeader from '../components/CommonHeader'
export default {
  components: {
    CommonHeader
  }
}
</script>

<style lang="stylus" scoped>
.el-header
    padding 0px
</style>
