<template>
  <el-form
    :model="form"
    ref="form"
    label-width="60px"
    :inline="inline"
    label-position="right"
  >
    <el-form-item
      :label="item.label"
      v-for="item in formLabel"
      :key="item.model"
    >
      <el-input v-if="!item.type" v-model="form[item.model]" autocomplete="off"></el-input>
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
    inline: Boolean
  }
}
</script>

<style lang="scss" scoped></style>
