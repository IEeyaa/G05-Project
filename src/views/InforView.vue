<template>
    <body>
        <div class="layout">
            <h1 id="title">{{ data['title'] }}</h1>
            <p id="date">{{ data['publication_date'] }}</p>
            <p id="author">{{ data['author'] }}</p>
            <p id="abstract">{{ data['abstract'] }}</p>
            <el-button type="warning" :icon="Star" @click="like(data['thesis_id'])" round>Like</el-button>
            <el-tag class="tag" v-for="tag in tags" :key="tag" >{{ tag }}</el-tag>
        </div>
        <div class="relatedpaper">
            <h2>相关论文</h2><el-divider border-style="dashed" />
            <el-card shadow="hover" class="paper" @click="info">
                <h4 class="papertitle">SuperFusion: Multilevel LiDAR-Camera Fusion for Long-Range HD Map Generation and Prediction</h4>
                <p class="paperdate">28 Nov 2022  ·  Hao Dong, Xianjing Zhang, Xuan Jiang, Jun Zhang, Jintao Xu, Rui Ai, Weihao Gu, Huimin Lu, Juho Kannala, Xieyuanli Chen</p>
                <p class="paperabstract">High-definition (HD) semantic map generation of the environment is an essential component of autonomous driving. Existing methods have achieved good performance in this task by fusing different sensor modalities, such as LiDAR and camera. However, current works are based on raw data or network feature-level fusion and only consider short-range HD map...</p>
            </el-card>
            <el-card shadow="hover" class="paper" @click="info">
                <h4 class="papertitle">Human-level play in the game of Diplomacy by combining language models with strategic reasoning</h4>
                <p class="paperdate">Science 2022  ·  Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff, Jonathan Gray, Hengyan Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath, Minae Kwon, Adam Lerer, Mike Lewis, Alexander H. Miller, Sash Mitts, Aditya Renduchintala, Stephen Roller, Dirk Rowe, Weiyan Shi, Joe Spisak, Alexander Wei, David Wu, Hugh Zhang, Markus Zijlstra</p>
                <p class="paperabstract">In this paper, we determine the optimal convergence rates for strongly convex and smooth distributed optimization in two settings: centralized and decentralized communications over a network. For centralized (i.e. master/slave) algorithms, we show that distributing Nesterov&#x27;s accelerated gradient descent is optimal and achieves a precision $\varepsilon &gt; 0$ in time $O(\sqrt{\kappa_g}(1+\Delta\tau)\ln(1/\varepsilon))$, where $\kappa_g$ is the condition number of the (global) function to optimize, $\Delta$ is the diameter of the network, and $\tau$ (resp. $1$) is the time needed to communicate values between two neighbors (resp. perform local computations). For decentralized algorithms based on gossip, we provide the first optimal algorithm, called the multi-step dual accelerated (MSDA) method, that achieves a precision $\varepsilon &gt; 0$ in time $O(\sqrt{\kappa_l}(1+\frac{\tau}{\sqrt{\gamma}})\ln(1/\varepsilon))$, where $\kappa_l$ is the condition number of the local functions and $\gamma$ is the (normalized) eigengap of the gossip matrix used for communication between nodes. We then verify the efficiency of MSDA against state-of-the-art methods for two problems: least-squares regression and classification by logistic regression.</p>
            </el-card>
            <el-card shadow="hover" class="paper" @click="info">
                <h4 class="papertitle">SuperFusion: Multilevel LiDAR-Camera Fusion for Long-Range HD Map Generation and Prediction</h4>
                <p class="paperdate">28 Nov 2022  ·  Hao Dong, Xianjing Zhang, Xuan Jiang, Jun Zhang, Jintao Xu, Rui Ai, Weihao Gu, Huimin Lu, Juho Kannala, Xieyuanli Chen</p>
                <p class="paperabstract">High-definition (HD) semantic map generation of the environment is an essential component of autonomous driving. Existing methods have achieved good performance in this task by fusing different sensor modalities, such as LiDAR and camera. However, current works are based on raw data or network feature-level fusion and only consider short-range HD map...</p>
            </el-card>
            <el-card shadow="hover" class="paper" @click="info">
                <h4 class="papertitle">Human-level play in the game of Diplomacy by combining language models with strategic reasoning</h4>
                <p class="paperdate">Science 2022  ·  Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff, Jonathan Gray, Hengyan Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath, Minae Kwon, Adam Lerer, Mike Lewis, Alexander H. Miller, Sash Mitts, Aditya Renduchintala, Stephen Roller, Dirk Rowe, Weiyan Shi, Joe Spisak, Alexander Wei, David Wu, Hugh Zhang, Markus Zijlstra</p>
                <p class="paperabstract">Despite much progress in training AI systems to imitate human language, building agents that use language to communicate intentionally with humans in interactive environments remains a major challenge. We introduce Cicero, the first AI agent to achieve human-level performance in Diplomacy, a strategy game involving both cooperation and competition that emphasizes...</p>
            </el-card>
            <el-card shadow="hover" class="paper" @click="info">
                <h4 class="papertitle">SuperFusion: Multilevel LiDAR-Camera Fusion for Long-Range HD Map Generation and Prediction</h4>
                <p class="paperdate">28 Nov 2022  ·  Hao Dong, Xianjing Zhang, Xuan Jiang, Jun Zhang, Jintao Xu, Rui Ai, Weihao Gu, Huimin Lu, Juho Kannala, Xieyuanli Chen</p>
                <p class="paperabstract">High-definition (HD) semantic map generation of the environment is an essential component of autonomous driving. Existing methods have achieved good performance in this task by fusing different sensor modalities, such as LiDAR and camera. However, current works are based on raw data or network feature-level fusion and only consider short-range HD map...</p>
            </el-card>
            <el-card shadow="hover" class="paper" @click="info">
                <h4 class="papertitle">Human-level play in the game of Diplomacy by combining language models with strategic reasoning</h4>
                <p class="paperdate">Science 2022  ·  Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff, Jonathan Gray, Hengyan Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath, Minae Kwon, Adam Lerer, Mike Lewis, Alexander H. Miller, Sash Mitts, Aditya Renduchintala, Stephen Roller, Dirk Rowe, Weiyan Shi, Joe Spisak, Alexander Wei, David Wu, Hugh Zhang, Markus Zijlstra</p>
                <p class="paperabstract">Despite much progress in training AI systems to imitate human language, building agents that use language to communicate intentionally with humans in interactive environments remains a major challenge. We introduce Cicero, the first AI agent to achieve human-level performance in Diplomacy, a strategy game involving both cooperation and competition that emphasizes...</p>
            </el-card>
        </div>
    </body>
</template>

<script>
export default {
    data(){
        return {
            data: null,
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
            this.$http.post('/InforView',{thesis_id: this.$route.query.id}).then(res=>{
                this.data = res.data['data'][0];
                this.tags = res.data['data'][1]['keywords'];
            })
        },
        async like(thesis_id){
            this.favor['user_name'] = (this.$cookies.get('name') == null) ? -1 : this.$cookies.get('name');
            this.favor['thesis_id'] = thesis_id;
            this.$http.post('/HomeView', this.favor).then(res=>{
              if(res.data['message'] == "success") alert("收藏成功");
              else alert(res.data['message']);
            });
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