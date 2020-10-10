<template>
  <el-form
    :model="form"
    ref="form"
    :rules="rules"
    :inline="inline"
    label-position="right"
    label-width="80px"
    status-icon
  >
    <el-form-item
      :label="item.label"
      v-for="item in formLabel"
      :key="item.model"
      :prop="item.model"
    >
      <el-input v-if="!item.type" v-model="form[item.model]"></el-input>
      <el-input
        v-if="item.type === 'password'"
        :type="item.type"
        v-model="form[item.model]"
        required
      ></el-input>
    </el-form-item>
    <el-form-item>
      <slot></slot>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  props: {
    form: Object,
    formLabel: Array,
    rules: Object,
    inline: Boolean
  }
}
</script>

<style lang="scss" scoped></style>
