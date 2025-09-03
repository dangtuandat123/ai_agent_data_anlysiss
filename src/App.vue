<template>
  
  <div style="height: 100%">
   
    <router-view></router-view>
    
  </div>

</template>

<script>
// import '../src/assets/css/templatemo-nexus-style.css'

export default {
  async mounted() {
    try {
      // await import('./assets/js/templatemo-nexus-scripts.js');

     
    } catch (error) {
      console.error('Lỗi khi tải script:', error);
    }
  }
}
</script>

<style></style>
