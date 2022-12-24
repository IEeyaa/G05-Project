<template>
    <el-select v-model="graphType" class="selector" placeholder="选择图表类型">
        <el-option
        v-for="item in chartOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        />
    </el-select>
    <el-select v-model="contents" class="selector" placeholder="选择可视化内容">
        <el-option
        v-for="item in typeOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        />
    </el-select>
    <!-- "关键词"：显示关键词选择器 -->
    <el-select v-model="selectPage" class="selector" placeholder="Select" v-if="contents=='keywords'">
        <el-option
        v-for="item in keywordOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        />
    </el-select>
    <!-- "日期"：显示日期选择器 -->
    <div class="date-picker" v-if="contents=='date'">
        <el-date-picker
            v-model="selectDate"
            type="monthrange"
            range-separator="To"
            start-placeholder="Start month"
            end-placeholder="End month"
            value-format="YYYY-MM"
        />
    </div>

    <el-button class="button" @click="generate">生成</el-button>
    <div id="chart"></div>
</template>

<script>
import { ref } from 'vue'
import * as echarts from 'echarts'
export default {
    data(){
        return{
            graphType: ref(''),
            selectDate: ref(''),
            contents: ref(''),
            selectPage: ref(''),
            first: 1,
            chartOptions: [ //图标选项
            { value: 'bar', label: '柱状图' },
            { value: 'pie', label: '饼图' },
            { value: 'line', label: '折线图' }
            ],
            typeOptions: [ //图表展示内容选项
            { value: 'date', label: '日期' },
            { value: 'keywords', label: '关键词' }
            ],
            keywordOptions: [
            { value: '1', label: '1-20' },
            { value: '2', label: '21-40' },
            { value: '3', label: '41-60' },
            { value: '4', label: '61-80' },
            { value: '5', label: '81-100' },
            { value: '6', label: '101-120' },
            { value: '7', label: '121-140' },
            { value: '8', label: '141-160' },
            { value: '9', label: '161-180' }
            ],
        }
    },
    methods: {
        generate(){
            var arr = new Array()
            if(this.first == 1){
                this.myChart = echarts.init(document.getElementById('chart')) //初始化
                this.first = 0
            }
            if(this.contents == 'date'){
                var start = this.selectDate[0] //开始月份
                var end = this.selectDate[1] //结束月份
                console.log(start);
                this.$http.get('/StatisticsDateView', {
                    params: {'start_month': start, 'end_month': end}
                    }).then(res=>{
                        arr = res.data['data']
                        var options = { //图表的配置
                            dataset: { //数据
                                source: arr
                            },
                            tooltip: {
                                show: true
                            },
                            xAxis: { type: 'category' },
                            yAxis: {},
                            series: [
                                {
                                type: this.graphType //图表类型
                                }
                            ]
                        }
                        this.myChart.setOption(options)
                        window.onresize = function () {//自适应大小
                            this.myChart.resize();
                        };
                        return;
                });
            }else{
                this.$http.get('/StatisticsKeyView', {
                    params: {'page': this.selectPage}
                    }).then(res=>{
                        arr = res.data['data']
                        var options = { //图表的配置
                            dataset: { //数据
                                source: arr
                            },
                            tooltip: {
                                show: true
                            },
                            xAxis: { type: 'category' },
                            yAxis: {},
                            series: [
                                {
                                type: this.graphType //图表类型
                                }
                            ]
                        }
                        this.myChart.setOption(options)
                        window.onresize = function () {//自适应大小
                            this.myChart.resize();
                        };
                        return;
                });
            }
        }
    }
}
</script>
  
<style scoped>

#chart {
    margin: 1.5% 25% 0%;
    width: 800px;
    height: 500px;
}

.date-picker {
    margin: 1.5% 25% 0%;
    display: flex;
    width: 50%;
    padding: 0;
    flex-wrap: wrap;
}

.selector {
    margin: 1.5% 25% 0%;
}

.button {
    margin: 1.5% 25% 0%;
}

body {
    margin: 0px;
    padding: 0;
}

</style>