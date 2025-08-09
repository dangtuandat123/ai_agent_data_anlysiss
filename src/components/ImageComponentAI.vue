<template>
  <div style="position: relative;">
    <!-- Hiển thị ảnh -->
    <div style="display: flex; align-items: center; margin-bottom: 5px; width: 100%; height: auto; max-width: 100%; padding: 10px 0px 10px 0px; position: relative;">
      <img :src="'data:image/png;base64,' + imgBase64" alt="" style="width: 100%; height: auto; max-width: 100%; border-radius: 20px">
      
      <!-- Nút tải ảnh xuống ở góc dưới bên trái -->
      <a :href="'data:image/png;base64,' + imgBase64" download="image.png" style="position: absolute; bottom: 10px; left: 3px;">
        <button class="button_edit_code">Tải ảnh xuống</button>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  props: ['imgBase64']
};
</script>

<style scoped>
.button_edit_code {
    margin-left: auto;
    background-color: #04ae67;
    color: white;
    border: none;
    padding: 5px 15px;
    border-radius: 20px;
    cursor: pointer;
    font-size: 13px;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 5px;
    transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    margin-left: 5px;
}

/* Hiệu ứng khi hover */
.button_edit_code:hover {
    background-color: #03a108;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.button_edit_code:active {
    transform: translateY(2px);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}



</style>
