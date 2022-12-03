<template>
    <body>
        <div class="layout">
            <h1 id="title">TorchScale: Transformers at Scale</h1>
            <p id="date">23 Nov 2022</p>
            <p id="author">Shuming Ma, Hongyu Wang, Shaohan Huang, Wenhui Wang, Zewen Chi, Li Dong, Alon Benhaim, Barun Patra, Vishrav Chaudhary, Xia Song, Furu Wei</p>
            <p id="abstract">Large Transformers have achieved state-of-the-art performance across many tasks. Most open-source libraries on scaling Transformers focus on improving training or inference with better parallelization. In this work, we present TorchScale, an open-source toolkit that allows researchers and developers to scale up Transformers efficiently and effectively. TorchScale has the implementation of several modeling techniques, which can improve modeling generality and capability, as well as training stability and efficiency. Experimental results on language modeling and neural machine translation demonstrate that TorchScale can successfully scale Transformers to different sizes without tears. The library is available at https://aka.ms/torchscale.</p>
            <el-tag class="tag">Language Modeling</el-tag>
            <el-tag class="tag">Machine Translation</el-tag>
            <el-tag class="tag">Translation</el-tag>
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
    methods: {
        info(event) {
        if (event) {
            this.$router.push("/info");
        }
        },
  },
};
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