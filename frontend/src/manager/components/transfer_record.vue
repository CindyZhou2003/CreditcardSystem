<template>
    <el-scrollbar height="100%" style="width: 100%;">

        <!-- 标题 -->
        <div style="margin-top: 20px; margin-left: 40px; font-size: 2em; font-weight: bold;">
            交易记录查询
          <el-input v-model="toSearch" :prefix-icon="Search"
                style=" width: 15vw;min-width: 150px; margin-left: 30px; margin-right: 30px; float: right; ;"
                clearable />
        </div>

        <!-- 查询框 -->
        <div style="width:60%;display: flex;margin:0 auto; padding-top:5vh;">
          <el-input v-model="this.toQueryInID" style="display:inline; " placeholder="输入付款人账号"></el-input>
          <el-input v-model="this.toQueryYear" style="display:inline; " placeholder="输入查询账单年份"></el-input>
          <el-input v-model="this.toQueryMonth" style="display:inline; " placeholder="输入查询账单月份"></el-input>
          <el-button style="margin-left: 10px;" type="primary" @click="QueryMonthBill">查询</el-button>
        </div>

        <!-- 结果表格 -->
        <p>total amount: {{total_amount}}</p>
        <el-table v-if="isShow" :data=tableData height="600"
          :default-sort="{ prop: 'transfer_id', order: 'ascending' }" :table-layout="'auto'"
          style="width: 100%; margin-left: 50px; margin-top: 30px; margin-right: 50px; max-width: 80vw;">
          <el-table-column prop="transfer_id" label="交易 ID" />
          <el-table-column prop="account_out_id" label="收款人账号" sortable />
          <el-table-column prop="transfer_amount" label="交易金额" sortable />
          <el-table-column prop="transfer_date" label="交易时间" sortable />
        </el-table>

    </el-scrollbar>
</template>

<script>
import axios from 'axios';
import { Search } from '@element-plus/icons-vue'
import {ElMessage} from "element-plus";

export default {
  data() {
    return {
      isShow: false, // 结果表格展示状态
      total_amount: 0,
      tableData: [{ // 列表项
        transfer_id: 1,
        account_in_id: 1,
        account_out_id: 1,
        transfer_amount: 0,
        transfer_date: "2024-03-04 21:49:00"
      }],
      toQueryInID: '1', // 待查询内容(对某一借书证号进行查询)
      toQueryYear: '2024',
      toQueryMonth: '5',
      toSearch: '', // 待搜索内容(对查询到的结果进行搜索)
      Search
    }
  },
  methods: {
    async QueryMonthBill() {
      this.tableData = [] // 清空列表
      try {
        const response = await axios.get('/creditcard/show_month_bill', {
          params: {
            account_in_id: this.toQueryInID,
            year: this.toQueryYear,
            month: this.toQueryMonth,
          }
        });
      if(response.data.status==='success') {
        this.total_amount = response.data.total_amount;
        const records = response.data.list; // 获取响应负载
        records.forEach(record => {
          this.tableData.push({
            transfer_id: record.pk,
            account_in_id: record.fields.account_in_id,
            account_out_id: record.fields.account_out_id,
            transfer_amount: record.fields.transfer_amount,
            transfer_date: record.fields.transfer_date,
          });
        });
        this.isShow = true; // 显示结果列表
      } else {
        console.error('Response data status failed');
        throw new Error(response.data.message ||'Response error');
      }
      } catch (error) {
        console.error('Error fetching data:', error);
        ElMessage.error('数据获取失败，请稍后重试！');
      }
    }
  },
}
</script>