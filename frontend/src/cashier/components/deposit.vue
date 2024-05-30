<template>
    <el-scrollbar height="100%" style="width: 100%;">

    <!-- 标题和搜索框 -->
    <div style="margin-top: 20px; margin-left: 40px; font-size: 2em; font-weight: bold;">
        账户存款
        <el-input v-model="toSearch" :prefix-icon="Search"
            style=" width: 15vw;min-width: 150px; margin-left: 30px; margin-right: 30px; float: right; ;"
            clearable />
    </div>

    <!-- 存款操作 -->
    <div style="width:70%;margin-left:30px; padding-top:5vh;">
        <!-- <el-input v-model="this.toQuery" style="display:inline; " placeholder="输入借书证ID"></el-input> -->
        <el-button style="margin-left: 10px;" type="primary" @click="this.DemandDepositVisible = true">活期存款</el-button>
        <el-button style="margin-left: 10px;" type="primary" @click="this.TimeDepositVisible = true">定期存款</el-button>
        <el-button style="margin-left: 10px;" type="primary" @click="this.TotalDepositVisble = true">累计存款</el-button>
    </div>

    <!-- 存款记录 -->
    <el-table v-if="isShow" :data="fitlerTableData" height="600"
        :default-sort="{ prop: 'deposit_record_id', order: 'ascending' }" :table-layout="'auto'"
        style="width: 100%; margin-left: 50px; margin-top: 30px; margin-right: 50px; max-width: 80vw;">
        <el-table-column prop="deposit_record_id" label="存款记录ID" sortable/>
        <el-table-column prop="account_id" label="账户ID" sortable/>
        <el-table-column prop="deposit_type" label="存款类型" />
        <el-table-column prop="auto_renew_status" label="是否自动续期" />
        <el-table-column prop="deposit_start_date" label="存款起始日期" />
        <el-table-column prop="deposit_end_date" label="存款终止日期" />
        <el-table-column prop="deposit_amount" label="存款金额" />
        <el-table-column prop="cashier_id" label="出纳员ID" />
        <!-- <el-table-column label="操作">
            <template #default="scope">
                <el-button :disabled="scope.row.returnTime !== '0' " link type="primary" size="small" @click="returnBook(scope.row)" v-model="returnBookVisible">还书</el-button>
            </template>
        </el-table-column> -->
    </el-table>

        <el-dialog v-model="DemandDepositVisible" title="活期存款" width="30%" align-center>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                账户ID：
                <el-input v-model="newDepositInfo.account_id" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                密码：
                <el-input v-model="newDepositInfo.password" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                存款金额：
                <el-input v-model="newDepositInfo.deposit_amount" style="width: 12.5vw;" clearable />
            </div>

            <template #footer>
                <span>
                    <el-button @click="DemandDepositVisible = false">取消</el-button>
                    <el-button type="primary" @click="ConfirmNewBook"
                        :disabled="newDepositInfo.account_id.length === 0 || newDepositInfo.password.length === 0">确定</el-button>
                </span>
            </template>
        </el-dialog>

        <el-dialog v-model="TimeDepositVisible" title="定期存款" width="30%" align-center>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                账户ID：
                <el-input v-model="newTimeDepositInfo.account_id" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                密码：
                <el-input v-model="newTimeDepositInfo.password" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                存款金额：
                <el-input v-model="newTimeDepositInfo.deposit_amount" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                存款期限：
                <el-input v-model="newTimeDepositInfo.deposit_term" style="width: 12.5vw;" clearable />
            </div>
            <div style="margin-left: 2vw; font-weight: bold; font-size: 1rem; margin-top: 20px; ">
                是否自动续期：
                <el-radio v-model="newTimeDepositInfo.is_auto_renew" label="1">是</el-radio>
                <el-radio v-model="newTimeDepositInfo.is_auto_renew" label="2">否</el-radio>
            </div>

            <template #footer>
                <span>
                    <el-button @click="TimeDepositVisible = false">取消</el-button>
                    <el-button type="primary" @click="ConfirmNewBook"
                        :disabled="newTimeDepositInfo.account_id.length === 0 || newTimeDepositInfo.password.length === 0">确定</el-button>
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
                deposit_record_id: 1,
                account_id: 1,
                deposit_type: "活期存款",
                auto_renew_status: "/",
                deposit_start_date: 0,
                deposit_end_date: 1,
                deposit_amount : 100.00,
                cashier_id: 1
            }],
            DemandDepositVisible:false,
            TimeDepositVisible:false,
            TotalDepositVisible:false,
            Search,
            toSearch: '', // 搜索内容
            newDepositInfo: { // 待新建存款信息
                account_id: '',
                password: '',
                deposit_amount: 0
            },
            newTimeDepositInfo: {
                account_id: '',
                password: '',
                deposit_amount: 0,
                deposit_term: 0,
                is_auto_renew: false
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
                deposit_record_id: 1,
                account_id: 1,
                deposit_type: "活期存款",
                auto_renew_status: "/",
                deposit_start_date: 0,
                deposit_end_date: 1,
                deposit_amount : 100.00,
                cashier_id: 1
                },
                { // 列表项
                deposit_record_id: 1,
                account_id: 1,
                deposit_type: "活期存款",
                auto_renew_status: "/",
                deposit_start_date: 0,
                deposit_end_date: 1,
                deposit_amount : 100.00,
                cashier_id: 1
                },
                { // 列表项
                deposit_record_id: 1,
                account_id: 1,
                deposit_type: "活期存款",
                auto_renew_status: "/",
                deposit_start_date: 0,
                deposit_end_date: 1,
                deposit_amount : 100.00,
                cashier_id: 1
                },
                { // 列表项
                deposit_record_id: 1,
                account_id: 1,
                deposit_type: "活期存款",
                auto_renew_status: "/",
                deposit_start_date: 0,
                deposit_end_date: 1,
                deposit_amount : 100.00,
                cashier_id: 1
                },
                { // 列表项
                deposit_record_id: 1,
                account_id: 1,
                deposit_type: "活期存款",
                auto_renew_status: "/",
                deposit_start_date: 0,
                deposit_end_date: 1,
                deposit_amount : 100.00,
                cashier_id: 1
                },
                { // 列表项
                deposit_record_id: 1,
                account_id: 1,
                deposit_type: "活期存款",
                auto_renew_status: "/",
                deposit_start_date: 0,
                deposit_end_date: 1,
                deposit_amount : 100.00,
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
        returnBook(data) {
            console.log(data)
            axios.post("/borrow",
                { // 请求体
                    method:"return",
                    cardId:data.cardID,
                    bookId:data.bookID,
                    borrowTime:data.borrowTime,
                    returnTime:data.returnTime            
                })
                .then(response => {
                    ElMessage.success("还书成功") // 显示消息提醒
                    this.returnBookVisible = false // 将对话框设置为不可见
                    this.QueryBorrows() // 重新查询借书证以刷新页面
                })
        }
    },
    mounted() { // 当页面被渲染时
        this.QueryDeposits() // 查询存款记录
    }

}
</script>

<style scoped>

</style>