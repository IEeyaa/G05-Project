<template>
    <el-button style="margin-left: 100px; margin-top: 30px;" type="info" :icon="Paperclip" @click="dialogTableVisible = true" plain>
        更改评价体系
    </el-button>
    <el-dialog v-model="dialogTableVisible" title="评价体系">
        <div class="slider-demo-block">
            <span class="demonstration">关键词联系</span>
            <el-slider v-model="value.key_word" :step="10" />
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
                    <el-button type="primary" style="width:150px" @click="toInfor(item1['thesis_id'])">详情</el-button>
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
                    <el-button type="primary" style="width:150px" @click="toInfor(item2['thesis_id'])">详情</el-button>
                </el-card>
            </div>
        </el-col>
    </el-row>
    <div style="text-align: center">
        <el-input v-model="key_word" 
        style="margin-top: 30px;margin-bottom: 30px;height: 60px;" 
        placeholder="请输入比较关键词" />
    </div>
    <div style="text-align: center"><el-button style="margin-top: 10px;" @click="start" round>开始比较</el-button></div>

    <el-dialog v-model="showCompResult" title="比较报告">
        <div style="text-align:center">
            <strong>两篇论文的相似度为：{{ this.result.similarity.toFixed(4)*100 }}%</strong>
        </div>
        <strong>可视化报告如下</strong>
        <el-row :gutter="20">
            <el-col :span="4"></el-col>
            <el-col :span="8">
                <div class="demo-rate-block">
                    <strong class="title">论文1</strong>
                    <span class="title">关键词评分</span>
                    <el-rate
                        v-model="result.key_rating1"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.key_rating1 + " scores" }}</el-rate>
                    <span class="title">引用量评分</span>
                    <el-rate
                        v-model="result.citation_rating1"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.citation_rating1 + " scores" }}</el-rate>
                    <span class="title">发表时间评分</span>
                    <el-rate
                        v-model="result.date_rating1"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.date_rating1 + " scores" }}</el-rate>
                    <span class="title">综合评分</span>
                    <el-rate
                        v-model="result.final_rating1"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.final_rating1 + " scores" }}</el-rate>
                </div>
            </el-col>
            <el-col :span="8">
                <div class="demo-rate-block">
                    <strong class="title">论文2</strong>
                    <span class="title">关键词评分</span>
                    <el-rate
                        v-model="result.key_rating2"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.key_rating2 + " scores" }}</el-rate>
                    <span class="title">引用量评分</span>
                    <el-rate
                        v-model="result.citation_rating2"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.citation_rating2 + " scores" }}</el-rate>
                    <span class="title">发表时间评分</span>
                    <el-rate
                        v-model="result.date_rating2"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.date_rating2 + " scores" }}</el-rate>
                    <span class="title">综合评分</span>
                    <el-rate
                        v-model="result.final_rating2"
                        disabled
                        show-score
                        text-color="#ff9900"
                    >{{ result.final_rating2 + " scores" }}</el-rate>
                </div>
            </el-col>
            <el-col :span="4"></el-col>
        </el-row>
        <strong>表格报告如下</strong>
        <el-row :gutter="20">
            <el-col :span="4"></el-col>
            <el-col :span="16">
                <div style="text-align:center">
                    <strong class="title">论文1</strong>
                </div>
                <el-table :data="tableData1" style="width: 100%; margin-top: 10px; margin-bottom: 10px;">
                    <el-table-column prop="name" label="名称" width="100" />
                    <el-table-column prop="dis" label="描述" width="260" />
                    <el-table-column prop="score" label="得分" />
                </el-table>
                <div style="text-align:center">
                    <strong class="title">论文2</strong>
                </div>
                <el-table :data="tableData2" style="width: 100%; margin-top: 10px; margin-bottom: 10px;">
                    <el-table-column prop="name" label="名称" width="100" />
                    <el-table-column prop="dis" label="描述" width="260" />
                    <el-table-column prop="score" label="得分" />
                </el-table>
            </el-col>
            <el-col :span="4"></el-col>
        </el-row>
        <div style="text-align:center"><el-button style="margin-top: 10px;" @click="(showCompResult = false)" round>确认</el-button></div>
    </el-dialog>
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
                key_word: 30,
                citation: 30,
                time: 30,
            },
            key_word: "",
            compare_infor:{
                thesis_id1: null,
                thesis_id2: null,
                value: null,
                key_word: null,
            },
            item1: null,
            item2: null,
            showThesis1: false,
            showThesis2: false,
            showCompResult: false,
            result: null,
            tableData1: null,
            tableData2: null,
        }
    },
    methods: {
        async toInfor(id){
          this.$router.push({
            path: '/Infor',
            query: {
              id: id
            }
          })
        },
        getstar(){
            return 1;
        },
        strcut(str){
            if(str.length >= 100) str = str.substring(0, 100) + "...";
            return str;
        },
        check1(){
            this.$http.post('/InforView', this.input1).then(res=>{
                this.showThesis1 = true;
                this.item1 = res.data['data'];
            });
        },
        check2(){
            this.$http.post('/InforView', this.input2).then(res=>{
                this.showThesis2 = true;
                this.item2 = res.data['data'];
            });
        },
        start(){
            this.compare_infor.thesis_id1 = this.input1.thesis_id;
            this.compare_infor.thesis_id2 = this.input2.thesis_id;
            this.compare_infor.value = this.value;
            this.compare_infor.key_word = this.key_word;
            this.$http.post('/CompareThesis', this.compare_infor).then(res=>{
                this.showCompResult= true;
                this.result = res.data['data'];
                var a = this.value.key_word;
                var b = this.value.citation;
                var c = this.value.time;
                // 防止全0导致除数失误
                if(a+b+c == 0){
                    a = 1;
                    b = 1;
                    c = 1;
                }
                this.result.final_rating1 = (((this.result.key_rating1*a) + (this.result.citation_rating1*b) + (this.result.date_rating1*c))/(a+b+c)).toFixed(2);
                this.result.final_rating2 = (((this.result.key_rating2*a) + (this.result.citation_rating2*b) + (this.result.date_rating2*c))/(a+b+c)).toFixed(2);
                this.tableData1 = [
                    {
                        name: '关键词',
                        dis: this.key_word,
                        score: this.result.key_rating1,
                    },
                    {
                        name: '引用量',
                        dis: this.item1.citation_num,
                        score: this.result.citation_rating1,
                    },
                    {
                        name: '发表时间',
                        dis: this.item1.publication_date,
                        score: this.result.date_rating1,
                    },
                    {
                        name: '综合评分',
                        dis: '三项权重:'+ a + " " + b + " " + c,
                        score: this.result.final_rating1,
                    },
                ],
                this.tableData2 = [
                    {
                        name: '关键词',
                        dis: this.key_word,
                        score: this.result.key_rating2,
                    },
                    {
                        name: '引用量',
                        dis: this.item2.citation_num,
                        score: this.result.citation_rating2,
                    },
                    {
                        name: '发表时间',
                        dis: this.item2.publication_date,
                        score: this.result.date_rating2,
                    },
                    {
                        name: '综合评分',
                        dis: '三项权重:'+ a + " " + b + " " + c,
                        score: this.result.final_rating2,
                    },
                ]
            });
        }
    }
}
</script>
  

<style scoped>
.demo-rate-block {
    padding: 30px 0;
    text-align: center;
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
.demo-rate-block .title{
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin-bottom: 20px;
    margin-top: 20px;
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
.el-rate{
    margin:auto
}

</style>