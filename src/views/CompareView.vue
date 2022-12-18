<template>
    <el-button style="margin-left: 100px; margin-top: 30px;" type="info" :icon="Paperclip" @click="dialogTableVisible = true" plain>
        更改评价体系
    </el-button>
    <el-dialog v-model="dialogTableVisible" title="评价体系">
        <div class="slider-demo-block">
            <span class="demonstration">关键词联系</span>
            <el-slider v-model="value.author" :step="10" />
        </div>
        <div class="slider-demo-block">
            <span class="demonstration">文章引用量</span>
            <el-slider v-model="value.citation" :step="10" />
        </div>
        <div class="slider-demo-block">
            <span class="demonstration">发布时间</span>
            <el-slider v-model="value.time" :step="10" />
        </div>
        <div style="text-align:center"><el-button style="margin-top: 10px;" @click="(dialogTableVisible = false)" round>确认</el-button></div>
    </el-dialog>

    <el-row :gutter="20">
        <el-col :span="12">
            <div class="demo-rate-block">
            <span class="demonstration">第一篇论文</span>
                <el-input v-model="input1.thesis_id" placeholder="请输入论文序号" />
                <div><el-button style="margin-top: 10px;" @click="check1" round>确定</el-button></div>
                <el-card class="card" v-if="showThesis1">
                    <img :src="item1['image_link']" class="image">
                    <div style="padding: 14px">
                    <div class="bottom">
                        <h2 id="title">{{ strcut(item1['title']) }}</h2>
                        <p id="date">{{ item1['publication_date'] }}</p>
                        <p id="author">{{ item1['author'] }}</p>
                        <p id="abstract">{{ strcut(item1['abstract']) }}</p>
                    </div>
                    </div>
                </el-card>
            </div>
        </el-col>

        <el-col :span="12">
            <div class="demo-rate-block">
                <span class="demonstration">第二篇论文</span>
                <el-input v-model="input2.thesis_id" placeholder="请输入论文序号" />
                <div><el-button style="margin-top: 10px;" @click="check2" round>确定</el-button></div>
                <el-card class="card" v-if="showThesis2">
                    <img :src="item2['image_link']" class="image">
                    <div style="padding: 14px">
                        <h2 id="title">{{ strcut(item2['title']) }}</h2>
                        <p id="date">{{ item2['publication_date'] }}</p>
                        <p id="author">{{ item2['author'] }}</p>
                        <p id="abstract">{{ strcut(item2['abstract']) }}</p>
                    </div>
                </el-card>
            </div>
        </el-col>
    </el-row>
    <div style="text-align:center"><el-button style="margin-top: 10px;" @click="start" round>开始比较</el-button></div>
  </template>
  

<script setup>
import {ref } from 'vue'
import {Paperclip} from '@element-plus/icons-vue'
const dialogTableVisible = ref(false)
</script>

<script>
export default {
    data(){
        return{
            input1:{
                thesis_id: "",
            },
            input2:{
                thesis_id: ""
            },
            value:{
                author: 0,
                citation: 0,
                time: 0,
            },
            item1: null,
            item2: null,
            showThesis1: false,
            showThesis2: false,
        }
    },
    methods: {
        strcut(str){
            if(str.length >= 100) str = str.substring(0, 100) + "...";
            return str;
        },
        check1(){
            this.$http.post('/CompareView', this.input1).then(res=>{
                this.showThesis1 = true;
                this.item1 = res.data['data'][0];
            });
        },
        check2(){
            this.$http.post('/CompareView', this.input2).then(res=>{
                this.showThesis2 = true;
                this.item2 = res.data['data'][0];
            });
        },
        start(){
            console.log("start");
        }
    }
}
</script>
  

<style scoped>
.demo-rate-block {
    padding: 30px 0;
    text-align: center;
    border-right: solid 1px var(--el-border-color);
    display: inline-block;
    width: 100%;
    box-sizing: border-box;
}
.demo-rate-block .demonstration {
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin-bottom: 20px;
}
.demo-rate-block .card{
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin: auto;
    width: 50%;
    margin-top: 20px;
}
.el-input{
    text-align: center;
    width: 49%;
}

.slider-demo-block {
    display: flex;
    align-items: center;
}
.slider-demo-block .demonstration {
    font-size: 14px;
    color: var(--el-text-color-secondary);
    line-height: 44px;
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-bottom: 0;
}
.slider-demo-block .demonstration + .el-slider {
    flex: 0 0 80%;
}
.image{
  margin-top: 40px;
  height: 150px; 
  width: 250px;
}
</style>