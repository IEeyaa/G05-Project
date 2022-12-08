<template>
    <el-tag
        v-for="tag in dynamicTags"
        :key="tag"
        class="mx-1"
        closable
        :disable-transitions="false"
        @close="handleClose(tag)"
    >
        {{ tag }}
    </el-tag>
</template>

<script setup>
    import { ref } from 'vue'
        const dynamicTags = ref(['Tag 1', 'Tag 2', 'Tag 3'])
        const handleClose = (tag) => {
        dynamicTags.value.splice(dynamicTags.value.indexOf(tag), 1)
    }
</script>