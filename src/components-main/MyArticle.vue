<template>
  <div style="background-color: rgba(239, 250, 246, 0.53)">
    <br />

    <br />
    <div style="width: 80%; margin-left: 1%" class="main">
      <el-card shadow="hover" v-for="(message, index) in Messages" :key="index">
        <div style="height: 100px">
          <div style="width: 14%;height: 100%;border-radius: 100px;display: inline-block;">
            <img
              style="width: 100%; height: 100%; border-radius: 100px"
              src="@/assets/default-paper-cover.png"
              class="image"
            />
          </div>
          <div style="display: inline-block; margin-left: 5%; width: 60%">
            <p class="message" style="font-weight: bold">{{ message.title }}</p>
            <p style="font-weight: lighter" class="message">
              {{ message.abstract }}
            </p>
            <p class="message">
              引用：
              <i class="el-icon-view"></i>
              {{ message.citation_num }}
              &nbsp;&nbsp; 日期：
              <i class="el-icon-star-off"></i>
              {{ message.publication_date }}
              &nbsp;&nbsp; 作者：
              <i class="el-icon-coordinate"></i>
              {{ message.author }}
              &nbsp;&nbsp;
            </p>
          </div>

          <div style="width: 18%; height: 100%; display: inline-block">
            <div style="display: inline-block; width: 48%">
              <el-button
                type="warning"
                round
                style="height: 50%; width: 100%; display: inline-block"
              >
                <el-icon><Delete /></el-icon>
              </el-button>
              <br /><br />
            </div>

            <div style="display: inline-block; width: 48%">
              <el-button
                type="primary"
                round
                style="height: 50%; width: 100%; display: inline-block"
              >
                <el-icon><Edit /></el-icon>
              </el-button>
              <br /><br />
            </div>
            <p style="text-align: center">{{ message.data }}</p>
          </div>
        </div>
        <br />
      </el-card>
    </div>
    <br />
    <div class="footer" style="margin: 0 auto; width: 100%">
      <div class="block">
        <el-pagination
          background
          layout="total, prev, pager, next, jumper"
          :total="total"
        >
        </el-pagination>
      </div>
    </div>
  </div>
</template>


<script>
import { Delete, Edit } from "@element-plus/icons-vue";
export default {
  components: {
    Delete,
    Edit,
  },
  name: "MyArticle",
  data() {
    return {
      total: 2,
      user_id: "",
      Messages: null
    };
  },
  created(){
      this.getInfor();
  },
  methods: {
      async getInfor(){
          this.$http.post('/UserView',{user_name: this.$cookies.get('name')}).then(res=>{
              this.Messages = res.data['data'];
              this.total = this.Messages.length;
          })
      },
  },
}
</script>

<style scoped>
.message {
  width: 25em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
