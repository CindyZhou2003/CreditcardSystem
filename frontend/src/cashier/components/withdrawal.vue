<template>
    <el-scrollbar height="100%" style="width: 100%;">

    <!-- 标题和搜索框 -->
    <div style="margin-top: 20px; margin-left: 40px; font-size: 2em; font-weight: bold;">
        账户取款
        <el-input v-model="toSearch" :prefix-icon="Search"
            style=" width: 15vw;min-width: 150px; margin-left: 30px; margin-right: 30px; float: right; ;"
            clearable />
    </div>

    <!-- 取款操作 -->
    <div style="width:30%;margin-left:30px; padding-top:5vh;">
        <!-- <el-input v-model="this.toQuery" style="display:inline; " placeholder="输入借书证ID"></el-input> -->
        <el-button style="margin-left: 10px;" type="primary" @click="this.WithdrawlVisible = true">取款服务</el-button>
        <!-- <el-button style="margin-left: 10px;" type="primary" @click="this.TimeDepositVisible = true">定期存款</el-button>
        <el-button style="margin-left: 10px;" type="primary" @click="this.TotalDepositVisble = true">累计存款</el-button> -->
    </div>

    <!-- 取款记录 -->
    <el-table v-if="isShow" :data="fitlerTableData" height="600"
        :default-sort="{ prop: 'withdrawl_record_id', order: 'ascending' }" :table-layout="'auto'"
        style="width: 100%; margin-left: 50px; margin-top: 30px; margin-right: 50px; max-width: 80vw;">
        <el-table-column prop="withdrawl_record_id" label="取款记录ID" sortable/>
        <el-table-column prop="account_id" label="账户ID" sortable/>
        <el-table-column prop="withdrawl_date" label="取款日期" />
        <el-table-column prop="withdrawl_amount" label="取款金额" />
        <el-table-column prop="cashier_id" label="出纳员ID" />
        <!-- <el-table-column label="操作">
            <template #default="scope">
                <el-button :disabled="scope.row.returnTime !== '0' " link type="primary" size="small" @click="returnBook(scope.row)" v-model="returnBookVisible">还书</el-button>
            </template>
        </el-table-column> -->
    </el-table>

        <el-dialog v-model="WithdrawlVisible" title="取款服务" width="30%" align-center>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                账户ID：
                <el-input v-model="newWithdrawlInfo.account_id" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                密码：
                <el-input v-model="newWithdrawlInfo.password" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                取款金额：
                <el-input v-model="newWithdrawlInfo.withdrawl_amount" style="width: 12.5vw;" clearable />
            </div>

            <template #footer>
                <span>
                    <el-button @click="WithdrawlVisible = false">取消</el-button>
                    <el-button type="primary" @click="ConfirmNewBook"
                        :disabled="newWithdrawlInfo.account_id.length === 0 || newWithdrawlInfo.password.length === 0">确定</el-button>
                </span>
            </template>
        </el-dialog>



    </el-scrollbar>


</template>

<script>
import axios from 'axios';
import { Delete, Edit, Search } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

export default {
    data() {
        return {
            isShow: false, // 结果表格展示状态
            tableData: [{ // 列表项
                withdrawl_record_id: 1,
                account_id: 1,
                withdrawl_date: 1,
                withdrawl_amount : 100.00,
                cashier_id: 1
            }],
            WithdrawlVisible:false,
            Search,
            toSearch: '', // 搜索内容
            newWithdrawlInfo: { // 待新建存款信息
                account_id: '',
                password: '',
                withdrawl_amount: 0
            }
        }
    },
    computed: {
        fitlerTableData() { // 搜索规则
            return this.tableData.filter(
                (tuple) =>
                    (this.toSearch == '') || // 搜索框为空，即不搜索
                    tuple.bookID == this.toSearch || // 图书号与搜索要求一致
                    tuple.borrowTime.toString().includes(this.toSearch) || // 借出时间包含搜索要求
                    tuple.returnTime.toString().includes(this.toSearch) // 归还时间包含搜索要求
            )
        }
    },
    methods: {
        async QueryDeposits() {
            this.tableData = [
            { // 列表项
                withdrawl_record_id: 1,
                account_id: 1,
                withdrawl_date: 1,
                withdrawl_amount : 100.00,
                cashier_id: 1
            }
        ]
            // this.tableData = [] // 清空列表
            // let response = await axios.get('/borrow', { params: { cardID: this.toQuery } }) // 向/borrow发出GET请求，参数为cardID=this.toQuery
            // let borrows = response.data // 获取响应负载
            // borrows.forEach(borrow => { // 对于每一个借书记录
            //     this.tableData.push(borrow) // 将它加入到列表项中
            // });
            this.isShow = true // 显示结果列表
        },
        // returnBook(data) {
        //     console.log(data)
        //     axios.post("/borrow",
        //         { // 请求体
        //             method:"return",
        //             cardId:data.cardID,
        //             bookId:data.bookID,
        //             borrowTime:data.borrowTime,
        //             returnTime:data.returnTime            
        //         })
        //         .then(response => {
        //             ElMessage.success("还书成功") // 显示消息提醒
        //             this.returnBookVisible = false // 将对话框设置为不可见
        //             this.QueryBorrows() // 重新查询借书证以刷新页面
        //         })
        // }
    },
    mounted() { // 当页面被渲染时
        this.QueryDeposits() // 查询存款记录
    }

}
</script>

<style scoped>

</style>