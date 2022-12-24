<template>
  <el-container>
    <el-header>
    </el-header>

    <el-main>
      <el-row :gutter="20">
        <el-col :span="20" :offset="2">
          <el-row>
            <el-button type="primary" :icon="Document" @click="toSort('thesis_id', 1)" round>Normal</el-button>
            <el-button type="success" :icon="Star" @click="toSort('title', 1)" round>Title</el-button>
            <el-button type="info" :icon="Calendar" @click="toSortTime('publication_date', -1)" round>New</el-button>
            <el-button type="warning" :icon="Trophy" @click="toSort('citation_num', -1)" round>Greatest</el-button>
          </el-row>
          <h1 style="margin-left:10px; margin-top: 40px;">{{ display }}</h1>
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
                :total="4127"
                @current-change="pageswitch()"
                v-model:current-page="currentPage"
              />

        </el-col>
        <el-col :span="2"></el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<style scoped>
#date, #author {
    font-size: small;
    color: grey;
}
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
.el-button{
  margin-left: 10px;
  margin-top: 20px;
}
.image{
  margin-top: 40px;
  height: 150px; 
  width: 250px;
}
.el-card{
  margin-bottom: 50px;
}

</style>

<script>
export const strcut = (str) => {
        if(str.length >= 200) str = str.substring(0, 200) + "...";
        return str;
    }
export default {
    data(){
        return {
            currentPage: 1,
            data: null,
            display: "Normal Display",
            favor: {
              thesis_id: "",
              user_name: "",
            },
        };
    },

    created(){
        this.getUsers();
    },

    methods: {
        async getUsers(){
            this.pageswitch();
        },

        async toInfor(id){
          this.$router.push({
            path: '/Infor',
            query: {
              id: id
            }
          })
        },
        async toLink(link){
          window.open(link, '_blank')
        },
        async pageswitch(){
            this.$http.get('/HomeView', {
              params: {'page': this.currentPage}
            }).then(res=>{
                this.data = res.data['data'];
            });
        },

        async toSort(rule, direction){
          this.data = this.data.sort((a, b) => (a[rule] > b[rule])?direction:-direction);
          if(rule == "thesis_id") this.display = "Normal Display";
          else if(rule == "title") this.display = "Title Sorting";
          else if(rule == "citation_num") this.display = "Most References";
        },

        async toSortTime(rule, direction){
          this.data = this.data.sort((a, b) => (new Date(a[rule]).getTime() > new Date(b[rule]).getTime())?direction:-direction);
          this.display = "New Paper";
        },

        async like(thesis_id){
            this.favor['user_name'] = (this.$cookies.get('name') == null) ? -1 : this.$cookies.get('name');
            this.favor['thesis_id'] = thesis_id;
            this.$http.post('/HomeView', this.favor).then(res=>{
              if(res.data['message'] == "success") alert("收藏成功");
              else alert(res.data['message']);
            });
        }
    },
}
</script>


<script setup>
  import {Document,Calendar,Trophy,Star} from '@element-plus/icons-vue'
</script>