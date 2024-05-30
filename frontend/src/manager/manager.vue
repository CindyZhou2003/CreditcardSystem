<template>
  <div class="main">
    <el-container>
      <el-aside class="aside">
        <el-menu active-text-color="#ffd04b" background-color="#444444" default-active="1" text-color="#fff"
                 style="height:100%; width: 100%; overflow: hidden" :router="true">
          <!-- list title -->
          <div style="color: white; background-color: #181818;
          width: 100%; height: 10vh; display: flex; align-items: center; justify-content: center;">管理员</div>
          <!-- menu-list in left-side-->
          <el-menu-item index="/manager/home">
            <el-icon> <Avatar /> </el-icon>
            <span>出纳员管理</span>
          </el-menu-item>

          <el-menu-item index="/manager/credit_card_examiner">
            <el-icon> <Avatar /> </el-icon>
            <span>信用卡审核员管理</span>
          </el-menu-item>

          <!--just for test-->
          <el-menu-item index="/manager/transfer_record">
            <el-icon> <Avatar /> </el-icon>
            <span>交易记录</span>
          </el-menu-item>

          <div style="height: 30px"></div>
          <a href="/cashier" style="margin-left: 40px;">
            <el-button type="danger">
              退出
            </el-button>
          </a>
        </el-menu>

      </el-aside>
      <el-container>
        <el-header style="height: 0vh;"></el-header>
        <el-main style="height: 100%; width: 100%; ">
          <el-scrollbar height="100%">
            <RouterView class="content" style="height: 100vh; max-height: 100%; background-color: white; color: black;" />
          </el-scrollbar>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  methods: {
    LogOut() {
      this.$router.push('/another-page');
    }
  }
}
</script>

<style scoped>
#app {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: #dcdcdc;
  width: 100vw;
  height: 100vh;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  min-height: 100%;
  height: auto;
  background-color: #dcdcdc;

}

.title {
  background-color: #ffffff;
  height: 60px;
}

.aside {
  min-height: 100vh;
  width: 200px;
  background-color: black;
}
</style>
