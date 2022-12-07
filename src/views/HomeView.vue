<template>
  <el-container>
    <el-header>
    </el-header>

    <el-main>
      <el-row :gutter="20">
        <el-col :span="20" :offset="2">
          <el-row>
            <el-button type="primary" :icon="Edit" round>Top</el-button>
            <el-button type="success" :icon="Check" round>Social</el-button>
            <el-button type="info" :icon="Message" round>New</el-button>
            <el-button type="warning" :icon="Star" round>Greatest</el-button>
          </el-row>
          <h1 style="margin-left:10px">Container</h1>
          <el-scrollbar height="600px">
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
          </el-scrollbar>
        </el-col>
        <el-col :span="2"></el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<style scoped>
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

.el-card{
  margin-top: 50px;
}

</style>

<script>
export default {
    data(){
        return {
            data: null
        };
    },

    created(){
        this.getUsers();
    },

    methods: {
        async getUsers(){
            this.$http.get('/InforView').then(res=>{
                console.log(res.data['data']);
                this.data = res.data['data'];
            });
        },

        async toInfor(id){
          console.log("woc");
          this.$router.push({
            path: '/Infor',
            query: {
              id: id
            }
          })
        }
    },
}
</script>


<script setup>
  import {Check,Edit,Message,Star} from '@element-plus/icons-vue'
</script>