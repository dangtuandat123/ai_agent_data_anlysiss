<template>
  <div class="relative">
    <!-- Hiển thị ảnh -->
    <div class="flex items-center mb-1 w-full h-auto max-w-full py-2.5 relative">
      <img :src="imageSrc" alt="Ảnh do AI tạo" class="w-full h-auto max-w-full rounded-lg border border-gray-200" />

      <!-- Nút tải ảnh xuống ở góc dưới bên trái -->
      <a :href="imageSrc" download="image.png" class="absolute bottom-2 left-2 inline-flex items-center gap-1.5 rounded-md bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
        <i class="fa-solid fa-download" aria-hidden="true"></i>
        <span>Tải ảnh</span>
      </a>
      <!-- Nút phóng to -->
      <a :href="`#${zoomId}`" aria-label="Phóng to ảnh" class="absolute bottom-2 left-28 inline-flex items-center gap-1.5 rounded-md bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
        <i class="fa-solid fa-up-right-and-down-left-from-center" aria-hidden="true"></i>
        <span>Phóng to</span>
      </a>
    </div>

    <!-- Lightbox overlay (CSS-only via :target) -->
    <div :id="zoomId" class="lightbox pointer-events-none fixed inset-0 z-50 flex items-center justify-center bg-black/60 opacity-0">
      <a href="#" class="absolute inset-0" aria-label="Đóng phóng to"></a>
      <div class="relative w-[min(95vw,1100px)] max-h-[85vh] overflow-hidden rounded-lg bg-white shadow-2xl ring-1 ring-black/10">
        <div class="flex items-center justify-between border-b border-gray-200 px-3 py-2">
          <h3 class="text-sm font-medium text-gray-800">Ảnh</h3>
          <a href="#" role="button" aria-label="Đóng" class="inline-flex h-8 w-8 items-center justify-center rounded-md border border-gray-200 text-gray-700 hover:bg-gray-50">
            <i class="fa-solid fa-xmark" aria-hidden="true"></i>
          </a>
        </div>
        <div class="max-h-[calc(85vh-44px)] overflow-auto p-3">
          <img :src="imageSrc" alt="Ảnh phóng to" class="h-auto w-full rounded-lg border border-gray-200" />
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
  props: ['imgBase64'],
  data() {
    return {
      zoomId: `img-zoom-${Math.random().toString(36).slice(2)}`
    };
  },
  computed: {
    imageSrc() {
      return 'data:image/png;base64,' + this.imgBase64;
    }
  }
};
</script>

<style scoped>
/* No extra styles; Tailwind classes used */
</style>
