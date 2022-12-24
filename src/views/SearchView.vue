<!-- for search -->
<template>
    <el-row :gutter="20">
        <el-col :span="16" :offset="4">
                <el-input v-model="transform.word" placeholder="请搜索">
                    <template #append>
                        <el-button 
                        style="margin-left: -20px; 
                        margin-top: 0px; 
                        height: 60px;
                        width: 70px;
                        font-size: 40px;" @click="search" :icon="Search" round/>
                    </template>
                </el-input>
        </el-col>
        <el-col :span="4"></el-col>
    </el-row>
    <el-row :gutter="20" v-if="showResult">
        <el-col :span="20" :offset="2">
            <!-- 对card进行相关的设计 -->
              <el-card v-for="item in data" :key="item" shadow="always">
                <el-row :gutter="20">
                  <!-- 图片部分 -->
                  <el-col :span="5">
                    <img :src="item['image_link']" class="image">
                  </el-col>
                  <!-- 文字部分 -->
                  <el-col :span="13" :offset="1">
                    <h2 id="title">{{ strcut(item['title']) }}</h2>
                    <p id="date">{{ item['publication_date'] }}</p>
                    <p id="author">{{ item['author'] }}</p>
                    <p id="abstract">{{ strcut(item['abstract']) }}</p>
                  </el-col>
                  <!-- 按钮部分 -->
                  <el-col :span="5">
                    <div style="text-align: -webkit-center">
                      <el-button type="warning" :icon="Star" @click="like(item['thesis_id'])" round>Like</el-button>
                      <p style="color:grey">{{ "citation: " + item['citation_num'] + " times" }}</p>
                      <el-button type="primary" style="width:150px" @click="toInfor(item['thesis_id'])">详情</el-button>
                      <el-button type="success" style="width:150px" @click="toLink(item['link'])">PDF</el-button>
                    </div>
                  </el-col>
                </el-row>
              </el-card>

              <el-pagination
                class="page"
                layout="prev, pager, next"
                :total="200"
                @current-change="pageswitch()"
                v-model:current-page="currentPage"
              />

        </el-col>
        <el-col :span="2"></el-col>
    </el-row>
</template>

<script setup>
import { Search } from '@element-plus/icons-vue'
</script>

<script>
    export const highLight = (str, key) => {
        if(str.length >= 200) str = str.substring(0, 200) + "...";
        const reg = new RegExp(key, 'ig')
        return str.replace(reg, (val) => {
            return `<span style="color:#66CCFF">${val}</span>`
        })
    }
    export default {
    data(){
        return{
        transform: {
            word: ""
        },
        data: null,
        showResult: false,
        }
    },
    methods: {
        cSuggestions(suggestions){
            suggestions.map(item => {
                item['title'] = highLight(item['title'], this.transform.word)
                item['abstract'] = highLight(item['abstract'], this.transform.word)
            })
            this.data = suggestions;
        },
        search(){
            this.$http.post('/SearchView', this.transform).then(res=>{
                this.showResult = true;
                this.cSuggestions(res.data['data']);
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