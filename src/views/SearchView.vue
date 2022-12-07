<!-- for search -->
<template>

    <el-row :gutter="20">
        <el-col :span="16" :offset="4">
                <el-input v-model="word" placeholder="请搜索">
                    <template #append>
                        <el-button style="margin-left:-20px; margin-top: 0px; 
                        height: 60px;
                        width: 70px;
                        font-size:40px;" @click="search" :icon="Search" round/>
                    </template>
                </el-input>
        </el-col>
        <el-col :span="4"></el-col>
    </el-row>
    <el-row :gutter="20" v-if="showResult">
        <el-col :span="20" :offset="2">
            <h1 style="margin-left:10px">Search Results</h1>
            <!-- 对card进行相关的设计 -->
                <el-card v-for="item in data" :key="item" shadow="always">
                <el-row :gutter="20">
                    <!-- 图片部分 -->
                    <el-col :span="5">
                    <img
                        src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                        class="image"
                    />
                    </el-col>
                    <!-- 文字部分 -->
                    <el-col :span="13" :offset="1">
                    <h1 id="title">{{ item['title'] }}</h1>
                    <p id="date">{{ item['publication_date'] }}</p>
                    <p id="author">{{ item['author'] }}</p>
                    <p id="abstract">{{ item['abstract'] }}</p></el-col>
                    <!-- 按钮部分 -->
                    <el-col :span="5">
                    <div style="text-align: -webkit-center">
                        <el-button type="warning" :icon="Star" round>收藏</el-button>
                        <p style="color:grey">Likes: 114514/hour</p>
                        <el-button type="primary" style="width:150px" @click="toInfor(item['id'])">Paper</el-button>
                        <el-button type="success" style="width:150px">Code</el-button>
                    </div>
                    </el-col>
                </el-row>
                </el-card>
        </el-col>
        <el-col :span="2"></el-col>
    </el-row>
</template>

<script setup>
import { Search } from '@element-plus/icons-vue'
</script>

<script>
  export default {
    data(){
      return{
        word: null,
        data: null,
        showResult: false,
      }
    },
    methods: {
        search(){
            this.$http.post('/SearchView', this.word).then(res=>{
                this.showResult = true;
                this.data = res.data['data'];
            });
        },
    }
  }
  </script>

<style scoped>

.el-button{
  margin-left: 10px;
  margin-top: 20px;
}

.el-card{
  margin-top: 50px;
}

.el-input{
    margin-top: 30px;
    height: 60px;
}
</style>