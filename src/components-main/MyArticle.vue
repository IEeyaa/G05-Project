<template>
  <div style="background-color: rgba(239, 250, 246, 0.53)">
    <br />

    <br />
    <div style="width: 80%; margin-left: 1%" class="main">
      <el-card shadow="hover" v-for="(message, index) in Messages" :key="index">
        <div style="height: 100px">
          <div
            style="
              width: 14%;
              height: 100%;
              border-radius: 100px;
              display: inline-block;
            "
          >
            <img
              style="width: 100%; height: 100%; border-radius: 100px"
              src="@/assets/default-paper-cover.png"
              class="image"
            />
          </div>
          <div style="display: inline-block; margin-left: 5%; width: 60%">
            <p class="message" style="font-weight: bold">{{ message.name }}</p>
            <p style="font-weight: lighter" class="message">
              {{ message.info }}
            </p>
            <p class="message">
              阅读：
              <i class="el-icon-view"></i>
              {{ message.number }}
              &nbsp;&nbsp; 收藏：
              <i class="el-icon-star-off"></i>
              {{ message.favorite }}
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
import { Delete, Edit } from "@element-plus/icons";
export default {
  components: {
    Delete,
    Edit,
  },
  name: "MyArticle",
  data() {
    return {
      total: 2,
      Messages: [
        {
          info: "人工智能技术能够对青年意识形态工作发挥重要推动作用",
          name: "人工智能嵌入青年意识形态工作:价值、风险及其化解",
          number: 240,
          data: "2022-10-25",
          favorite: 2,
          author: "翟中杰",
        },
        {
          info: "在高速发展的现代社会，我们的医疗教育以及生活的方方面面都融合着人工智能",
          name: "大数据结合云计算的人工智能创新发展研究",
          number: 755,
          data: "2022-10-28",
          favorite: 35,
          author: "张海清",
        },
      ],
    };
  },
};
</script>

<style scoped>
.message {
  width: 25em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
