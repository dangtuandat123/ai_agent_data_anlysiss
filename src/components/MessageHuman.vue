<template>
  <!-- User message: right aligned bubble, optional files block -->
  <li role="listitem" class="flex justify-end">
    <article class="relative pt-2 max-w-full text-right min-w-0">
      <!-- Files preview in message (if any) -->
      <div v-if="listFile && listFile.length" class="inline-flex w-[min(92vw,100%)] flex-col gap-2 rounded-2xl rounded-tr-md bg-white p-2.5 sm:p-3 text-sm text-gray-900 ring-1 ring-gray-200 shadow-sm hover:ring-gray-300">
        <ul class="divide-y divide-gray-200">
          <li v-for="(file, index) in listFile" :key="index" class="flex items-center gap-3 py-1.5 first:pt-0 last:pb-0">
            <div :class="['flex h-10 w-10 flex-none items-center justify-center rounded-md ring-1 ring-inset', fileMeta(file).bgClass, fileMeta(file).ringClass, fileMeta(file).textClass]">
              <i :class="fileMeta(file).icon" aria-hidden="true"></i>
            </div>
            <div class="min-w-0 text-left">
              <p class="truncate max-w-[240px] sm:max-w-[360px] font-medium">{{ truncateFileName(file) }}</p>
              <p class="text-xs text-gray-500">{{ fileMeta(file).label }}</p>
            </div>
            <a href="#" :download="file" role="button" :aria-label="`Tải xuống ${file}`" class="ml-auto inline-flex items-center gap-1.5 rounded-md bg-white px-2 py-1 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
              <i class="fa-solid fa-file-arrow-down" aria-hidden="true"></i>
              <span>Tải xuống</span>
            </a>
          </li>
        </ul>
      </div>

      <!-- Message bubble -->
      <div class="inline-block rounded-2xl rounded-tr-md bg-white px-3 py-2.5 text-sm font-medium text-gray-900 ring-1 ring-gray-200 shadow-sm mt-1">
        <p>{{ message }}</p>
      </div>
      <div class="mt-1 flex justify-end gap-2">
        <!-- Copy panel (UI-only) -->
        <div class="relative inline-block">
          <input :id="copyId" type="checkbox" class="peer sr-only" aria-hidden="true" />
          <label :for="copyId" role="button" tabindex="0" aria-label="Mở panel sao chép" :aria-controls="copyPanelId" class="inline-flex h-8 w-8 items-center justify-center rounded-full bg-white text-gray-600 ring-1 ring-inset ring-gray-200 shadow-sm hover:bg-gray-50">
            <i class="fa-regular fa-copy" aria-hidden="true"></i>
            <span class="sr-only">Sao chép nội dung</span>
          </label>
          <div :id="copyPanelId" role="dialog" aria-modal="false" aria-label="Sao chép nội dung" class="pointer-events-none absolute right-0 top-9 z-20 w-64 rounded-md border border-gray-200 bg-white p-3 text-xs text-gray-700 shadow-lg opacity-0 transition peer-checked:pointer-events-auto peer-checked:opacity-100">
            <p class="mb-2 text-[11px] text-gray-500">Chọn và copy nội dung:</p>
            <textarea readonly :value="message" class="w-full resize-none rounded border border-gray-200 bg-gray-50 p-2 text-xs leading-5"></textarea>
          </div>
        </div>
      </div>
      <p class="mt-1 text-right text-xs text-gray-500">Bạn<span v-if="time"> • {{ time }}</span></p>
    </article>
  </li>
</template>

<script>
export default {
  props: ['message', 'listFile', 'time'],
  data() {
    const uid = Math.random().toString(36).slice(2);
    return {
      copyId: `copy-user-${uid}`,
      copyPanelId: `copy-panel-user-${uid}`,
    };
  },
  methods: {
    // Icon/màu/label theo phần mở rộng
    fileMeta(fileName) {
      const ext = (fileName.split('.').pop() || '').toLowerCase();
      const label = ext ? ext.toUpperCase() : 'FILE';
      if (ext === 'pdf') {
        return { icon: 'fa-solid fa-file-pdf', bgClass: 'bg-red-50', ringClass: 'ring-red-100', textClass: 'text-red-600', label: `PDF` };
      }
      if (ext === 'doc' || ext === 'docx') {
        return { icon: 'fa-solid fa-file-word', bgClass: 'bg-blue-50', ringClass: 'ring-blue-100', textClass: 'text-blue-600', label: `DOCX` };
      }
      if (ext === 'png' || ext === 'jpg' || ext === 'jpeg' || ext === 'gif' || ext === 'webp') {
        return { icon: 'fa-solid fa-file-image', bgClass: 'bg-emerald-50', ringClass: 'ring-emerald-100', textClass: 'text-emerald-600', label: `IMAGE` };
      }
            if (ext === 'csv') {
                return { icon: 'fa-solid fa-file-csv', bgClass: 'bg-lime-50', ringClass: 'ring-lime-100', textClass: 'text-lime-700', label: 'CSV' };
            }
            if (ext === 'xls' || ext === 'xlsx') {
                return { icon: 'fa-solid fa-file-excel', bgClass: 'bg-green-50', ringClass: 'ring-green-100', textClass: 'text-green-600', label: ext.toUpperCase() };
            }
      return { icon: 'fa-regular fa-file', bgClass: 'bg-gray-50', ringClass: 'ring-gray-200', textClass: 'text-gray-600', label };
    },
    // Cắt tên giữ đuôi
    truncateFileName(fileName, maxLength = 40) {
      const dot = fileName.lastIndexOf('.');
      if (dot === -1) return fileName.length > maxLength ? fileName.slice(0, maxLength) + '…' : fileName;
      const name = fileName.slice(0, dot);
      const ext = fileName.slice(dot);
      if (name.length > maxLength) return name.slice(0, maxLength) + '…' + ext;
      return fileName;
    }
  }
};
</script>

<style scoped>
/* Presentation handled by Tailwind classes */
</style>
