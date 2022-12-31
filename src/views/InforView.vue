<template>
    <body>
        <div class="layout">
            <h1 id="title">{{ data['title'] }}</h1>
            <p id="citation">{{ "被引用次数: " + data['citation_num']}}</p>
            <p id="date">{{ data['publication_date'] }}</p>
            <p id="author">{{ data['author'] }}</p>
            <p id="abstract">{{ data['abstract'] }}</p>
            <el-button type="warning" :icon="Star" @click="like(data['thesis_id'])" round>Like</el-button>
            <el-tag class="tag" v-for="tag in tags" :key="tag" >{{ tag }}</el-tag>
            <div style="margin-top: 50px;"><el-button type="primary" style="width:100px; height:30px;" @click="toLink(data['link'])">PDF</el-button></div>
        </div>
        <div class="relatedpaper">
            <h2>相关论文</h2><el-divider border-style="dashed" />
            <el-card v-for="item in linkData" :key="item" shadow="hover" class="paper" @click="info">
                <h4 class="papertitle">{{ item['title'] }}</h4>
                <p class="paperdate">{{ item['publication_date'] + "  " + item['author']}}</p>
                <p class="paperabstract">{{ item['abstract'] }}</p>
                <el-button type="primary" style="width:150px" @click="toInfor(item['thesis_id'])">详情</el-button>
            </el-card>
        </div>
    </body>
</template>

<script>
export default {
    inject: ['reload'],
    data(){
        return {
            data: null,
            linkData: null,
            tags: null,
            favor: {
              thesis_id: "",
              user_name: "",
            },
        };
    },

    created(){
        this.getInfor();
    },
    methods: {
        async getInfor(){
            this.$http.get('/InforView', {
              params: {'thesis_id': this.$route.query.id}
            }).then(res=>{
                this.data = res.data['data'][0];
                this.tags = res.data['data'][1];
                this.linkData = res.data['similarity'];
            });
        },
        async toLink(link){
          window.open(link, '_blank')
        },
        async like(thesis_id){
            this.favor['user_name'] = (this.$cookies.get('name') == null) ? -1 : this.$cookies.get('name');
            this.favor['thesis_id'] = thesis_id;
            this.$http.post('/HomeView', this.favor).then(res=>{
              if(res.data['message'] == "success") alert("收藏成功");
              else alert(res.data['message']);
            });
        },
        async toInfor(id){
          this.$router.push({
            name: 'information',
            query: {
              id: id
            }
          })
        },
    },
}
</script>

<script setup>
  import {Star} from '@element-plus/icons-vue'
</script>

<style scoped>
.layout {
  position: static;
  margin: 5% 5% 2%;
  background: #fff;
  text-align: left;
  line-height: 30px;
}
.relatedpaper{
  position: static;
  float: left;
  margin: 0px;
  padding: 5%;
  background: #fff;
}
.paper {
  position: static;
  margin: 20px 0px;
  width: auto;
  background: #fff;
  text-align: left;
  line-height: 20px;
}
h2 {
    text-align: left;
    padding-left: 10px;
}
.paperdate {
    font-size: x-small;
}
.paperabstract {
    font-size: smaller;
}
.tag {
    margin: 0px 10px;
}
body {
  margin: 0px;
  padding: 0;
}
#date, #author {
    font-size: small;
    color: grey;
}
</style>