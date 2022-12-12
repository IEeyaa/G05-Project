<template>
    <el-select v-model="value1" class="selector" placeholder="Select">
        <el-option
        v-for="item in selectOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        />
    </el-select>
    <div class="date-picker">
        <el-date-picker
            v-model="value2"
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
            value1: ref(''),
            value2: ref(''),
            first: 1,
            selectOptions: [ //选择器的选项
            {
                value: 'bar',
                label: '柱状图',
            },
            {
                value: 'pie',
                label: '饼图',
            },
            {
                value: 'line',
                label: '折线图',
            }
            ]
        }
    },
    methods: {
        generate(){
            if(this.first == 1){
                this.myChart = echarts.init(document.getElementById('chart')) //初始化
                this.first = 0
            }
            var start = this.value2[0].split('-'); //开始月份
            var end = this.value2[1].split('-'); //结束月份
            var arr = new Array()
            var k = 0
            for(var i=start[0]; i<=end[0]; i++){ //获取所有月份
                if(start[0] == end[0]){
                    var m = start[1]
                    var n = end[1]
                }else if(i == start[0]){
                    m = start[1]
                    n = 12
                }else if(i == end[0]){
                    m = 1
                    n = end[1]
                }else{
                    m = 1
                    n = 12
                }
                for(var j=m; j<=n; j++){
                    var val = ''
                    if(j < 10){
                        val = i+"-0"+parseInt(j)
                    }else{
                        val = i+"-"+j
                    }
                    arr[k++] = [val, parseInt(j)]
                }
            }
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
                    type: this.value1 //图表类型
                    }
                ]
            }
            this.myChart.setOption(options)
            window.onresize = function () {//自适应大小
                this.myChart.resize();
            };
        }
    }
}
</script>
  
<style scoped>

#chart {
    margin: 0% 25%;
    width: 800px;
    height: 500px;
}

.date-picker {
    margin: 3% 25%;
    display: flex;
    width: 50%;
    padding: 0;
    flex-wrap: wrap;
}

.selector {
    margin: 3% 25% 0%;
}

.button {
    margin: 0% 25%;
}

body {
    margin: 0px;
    padding: 0;
}

</style>