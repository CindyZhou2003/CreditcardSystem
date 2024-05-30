

<template>
  <el-scrollbar height="100%" style="width: 100%; height: 100%">
    <!--出纳员信息显示卡片-->
    <div style="margin-left:20px; display: flex;flex-wrap: wrap; justify-content: start;">
      <div class="cashierBox" v-for="cashier in cashiers" :key="cashier.id">
        <div>
          <!-- 卡片标题 -->
          <div style="font-size: 25px; font-weight: bold;">No. {{cashier.id}}</div>
          <el-divider />
          <!-- 卡片内容 -->
          <div style="margin-left: 10px; text-align: start; font-size: 16px;">
            <p style="padding: 2px;"><span style="font-weight: bold">账户名：</span>{{cashier.account}}</p>
            <p style="padding: 2px;"><span style="font-weight: bold">姓名：</span>{{cashier.name}}</p>
            <p style="padding: 2px;"><span style="font-weight: bold">身份证：</span>null</p>
            <p style="padding: 2px;"><span style="font-weight: bold">性别：</span>{{cashier.sex}}</p>
            <p style="padding: 2px;"><span style="font-weight: bold">电话：</span>{{cashier.phone}}</p>
            <p style="padding: 2px;">
              <el-tag v-if="cashier.ifTrade">账户交易权限</el-tag>
              <el-tag v-if="cashier.ifManage" style="margin-left: 10px">账户管理权限</el-tag>
            </p>
          </div>
          <el-divider />
          <!-- 卡片操作 -->
          <div style="margin-top: 10px; display:flex">
            <el-button type="primary">
              修改信息
            </el-button>
            <el-button type="success">
              修改权限
            </el-button>
            <el-button type="danger">
              删除
            </el-button>
          </div>
        </div>
      </div>
      <el-button class="newCashierBox" @click="newCardVisible = true">
        <el-icon style="height: 50px; width: 50px;">
          <Plus style="height: 100%; width: 100%;" />
        </el-icon>
      </el-button>
    </div>
  </el-scrollbar>
</template>
<script>
export default{
  data(){
    return{
      cashiers: [
        {
          id: 1,
          account: '炸毛的王昊元',
          name: '王昊元',
          sex: '男',
          phone:'18962391106',
          ifTrade: true,
          ifManage: true
        },
        {
          id: 2,
          account: '飞翔的猪',
          name: '王元豪',
          sex: '男',
          phone:'18962391107',
          ifTrade: true,
          ifManage: false
        },
        {
          id: 3,
          account: 'Cold',
          name: '李四',
          sex: '女',
          phone:'18962391190',
          ifTrade: true,
          ifManage: true
        },
        {
          id: 4,
          account: 'Flesic',
          name: '张三',
          sex: '男',
          phone:'18962391767',
          ifTrade: true,
          ifManage: false
        },
      ]
    }
  }
}
</script>

<style scoped>
.cashierBox {
  height:380px;
  width: 275px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-align: center;
  margin-top: 40px;
  margin-left: 28px;
  margin-right: 10px;
  padding: 15px 10px 8px 8px;
}
.newCashierBox {
  height: 380px;
  width: 275px;
  margin-top: 40px;
  margin-left: 28px;
  margin-right: 10px;
  padding: 15px 10px 8px 8px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-align: center;
}
</style>