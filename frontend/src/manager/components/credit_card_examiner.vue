<template>
  <el-scrollbar height="100%" style="width: 100%; height: 100%">
    <!--信用卡审核员信息显示卡片-->
    <div style="margin-left:20px; display: flex;flex-wrap: wrap; justify-content: start;">
      <!--list-->
      <div class="examinerBox" v-for="examiner in examiners" :key="examiner.id">
        <div>
          <!-- 卡片标题 -->
          <div style="font-size: 25px; font-weight: bold;">No. {{examiner.id}}</div>

          <el-divider />

          <!-- 卡片内容 -->
          <div style="margin-left: 10px; text-align: start; font-size: 16px;">
            <p style="padding: 2px;"><span style="font-weight: bold">账户名：</span>{{examiner.account}}</p>
            <p style="padding: 2px;"><span style="font-weight: bold">姓名：</span>{{examiner.name}}</p>
            <p style="padding: 2px;"><span style="font-weight: bold">身份证：</span>null</p>
            <p style="padding: 2px;"><span style="font-weight: bold">性别：</span>{{examiner.sex}}</p>
            <p style="padding: 2px;"><span style="font-weight: bold">电话：</span>{{examiner.phone}}</p>
            <p style="padding: 2px;">
              <el-tag v-if="examiner.ifTrade">账户交易权限</el-tag>
              <el-tag v-if="examiner.ifManage" style="margin-left: 10px">账户管理权限</el-tag>
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
      <!--dialog boxes-->
      <el-button class="newExaminerBox" @click="newExaminerVisible = true">
        <el-icon style="height: 50px; width: 50px;">
          <Plus style="height: 100%; width: 100%;" />
        </el-icon>
      </el-button>
    </div>
  </el-scrollbar>
</template>
<script>
import {Plus} from "@element-plus/icons-vue";

export default{
  components: {Plus},
  data(){
    return{
      examiners: [
        {
          id: 1,
          account: '山茶元',
          name: '神茶园',
          sex: '男',
          phone:'18962391106',
          ifTrade: true,
          ifManage: true
        },
      ]
    }
  }
}
</script>

<style scoped>
.examinerBox {
  height:380px;
  width: 275px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-align: center;
  margin-top: 40px;
  margin-left: 28px;
  margin-right: 10px;
  padding: 15px 10px 8px 8px;
}
.newExaminerBox {
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