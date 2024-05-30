<template>
  <el-scrollbar height="100%" style="width: 100%; height: 100%">
    <div style="margin-top: 20px; margin-left:20px; font-size: 2em; font-weight: bold;">
      账户状态管理
    </div>
    <div style="width:30%;margin:0 auto; padding-top:5vh;">

      <el-input  v-model="toQuery" style="display:inline; " placeholder="输入账户ID"></el-input>
      <el-button style="margin-left: 10px;" type="primary" @click="get()">查询</el-button>
      <div class="accountBox" v-if="isShow">
        <div style="font-size: 25px; font-weight: bold;">账户ID： {{account.id}}</div>

        <el-divider />

<!--        <p style="padding: 2.5px;"><span style="font-weight: bold">类型：</span>{{account.cardType}}</p>-->
        <p style="padding: 2.5px;"><span style="font-weight: bold">余额：￥</span>{{account.balance}}</p>
        <p style="padding: 2.5px;"><span style="font-weight: bold">定期存款：￥</span>{{account.curDeposit}}</p>
        <p style="padding: 2.5px;"><span style="font-weight: bold">待定存款：￥</span>{{account.uncreditedDeposit}}</p>
        <p style="padding: 2.5px;"><span style="font-weight: bold">身份证：</span>{{account.idCard}}</p>
        <p style="padding: 2.5px;">
          <el-tag v-if="account.isFrozen">已冻结</el-tag>
          <el-tag v-else>未冻结</el-tag>
          <el-tag v-if="account.isLost" style="margin-left: 10px">已挂失</el-tag>
          <el-tag v-else>未挂失</el-tag>
        </p>

        <el-divider />

        <div style="margin-top: 10px; margin-left: 75px; display:flex">
          <el-button v-if = "account.isFrozen" type="primary">解冻 </el-button>
          <el-button v-else type="primary">冻结 </el-button>
          <el-button v-if = "account.isLost" type="primary">补发 </el-button>
          <el-button v-else type="primary">挂失 </el-button>
        </div>
      </div>
    </div>
  </el-scrollbar>
</template>

<script>
  export default {
    data() {
      return {
        toQuery: '',
        isShow: false,
        account:
          {
            id: 3,
            password: '',
            idCard: '330782200408076216',
            //cardType: '',
            balance: 100.00,
            curDeposit: 44.0,
            uncreditedDeposit: 56.0,
            isFrozen: false,
            isLost: true
          }
      }
    },
    methods: {
      get(){
        this.isShow = true
      }
    }
  }
</script>

<style scoped>
.accountBox {
  height:350px;
  width: 300px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-align: center;
  margin-top: 80px;
  margin-left: 0px;
  margin-right: 10px;
  padding: 7.5px;
  padding-right: 10px;
  padding-top: 15px;
}
</style>