<!-- for search -->
<template>
    <el-row :gutter="20">
        <el-col :span="16" :offset="4">
            <div style="text-align: -webkit-center">
                <el-input v-model="input1" placeholder="请搜索">
                    <template #append>
                        <el-button :icon="Search" />
                    </template>
                </el-input>
            </div>
        </el-col>
        <el-col :span="4"></el-col>
        
    </el-row>
</template>

<style scoped>
.el-input{
    margin-top: 20px;
    height: 40px;
}
</style>

<script setup>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
const input1 = ref('')
</script>
