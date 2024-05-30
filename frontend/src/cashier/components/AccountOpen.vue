

<template>
  <el-scrollbar height="100%" style="width: 100%;">
    <div style="margin-top: 20px; margin-left:20px; font-size: 2em; font-weight: bold;">
    账户开设
    </div>
  <div style="width:30%;margin:0 auto; padding-top:5vh;">
    <div style="height: 20px"></div>
    <div style = "margin-left: 3vw; font-weight: bold; font-size: 1rem; margin-top: 5px;">
      身份证：
      <el-input v-model="accountNum" style="width: 12.5vw; margin-left: 1rem" clearable/>
    </div>
    <div style="height: 20px"></div>
    <div style = "margin-left: 4.3vw; font-weight: bold; font-size: 1rem; margin-top: 5px;">
      密码：
      <el-input v-model="password" style="width: 12.5vw; margin-left: 1rem" type="password" clearable/>
    </div>
    <div style="height: 20px"></div>
    <div style = "margin-left: 4.3vw; font-weight: bold; font-size: 1rem; margin-top: 5px; ">
      <el-button type="primary" style="margin-left: 57px" @click="openAccount()">开设账户</el-button>
    </div>
    <div class="accountBox" v-if="isShow">
      <div style="font-size: 25px; font-weight: bold;">新开设账户ID： {{account.id}}</div>

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
    </div>
  </div>
  </el-scrollbar>
</template>

<script>

export default {
  data(){
    return{
      accountNum: '',
      password: '',
      isShow: false,
      account:
          {
            id: 3,
            password: '',
            idCard: '330782200408076216',
            //cardType: '',
            balance: 0.00,
            curDeposit: 0.0,
            uncreditedDeposit: 0.0,
            isFrozen: false,
            isLost: false
          }
    }
  },
  methods:{
    openAccount(){
      this.isShow = true;
    }
  }
}
</script>

<style scoped>
.accountBox {
  height:270px;
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