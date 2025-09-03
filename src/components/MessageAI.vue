<template>
  <!-- AI message: left aligned with avatar, supports code/image/table/text -->
  <li role="listitem" class="flex items-start gap-3">
    <div class="mt-1 hidden h-8 w-8 flex-none select-none items-center justify-center rounded-full bg-gray-200 text-gray-700 sm:inline-flex" aria-hidden="true">
      <i class="fa-solid fa-robot"></i>
    </div>
    <article class="relative pt-2 max-w-full flex-1 min-w-0">
      <template v-if="message.iscode">
        <!-- Code block -->
        <CodeComponentAI :code="localCode" @update:code="updateCode" @run-again="handleRunAgain" />

        <!-- Image block (UI Kit style) -->
        <div v-if="message.type === 'img'" class="inline-flex w-[min(92vw,100%)] flex-col gap-2 rounded-2xl rounded-tl-md bg-white p-2.5 sm:p-3 text-sm text-gray-900 ring-1 ring-gray-200 shadow-sm hover:ring-gray-300 mt-3">
          <div class="relative">
            <img :src="imageSrcAI" alt="Ảnh do AI tạo" class="h-auto w-full rounded-lg border border-gray-200" />
            <a :href="`#${imgZoomId}`" aria-label="Phóng to ảnh" class="absolute inset-0 cursor-zoom-in"></a>
          </div>
          <div class="mt-3 flex flex-wrap items-center gap-2">
            <a :href="`#${imgZoomId}`" role="button" aria-label="Phóng to ảnh" class="inline-flex items-center gap-1.5 rounded-md bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
              <i class="fa-solid fa-up-right-and-down-left-from-center" aria-hidden="true"></i>
              <span>Phóng to ảnh</span>
            </a>
            <button type="button" @click="downloadImage" aria-label="Tải ảnh" class="inline-flex items-center gap-1.5 rounded-md bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
              <i class="fa-solid fa-download" aria-hidden="true"></i>
              <span>Tải ảnh</span>
            </button>
          </div>
        </div>

        <!-- HTML table block -->
        <div v-if="message.type === 'table_html'" ref="tableWrapper" class="max-w-full overflow-x-auto">
          <div v-html="message.table_html" class="table-container max-w-full overflow-x-auto"></div>
        </div>
        <div class="mt-2 flex flex-wrap items-center gap-2" v-if="message.type === 'table_html'">
          <a :href="`#${tableZoomId}`" role="button" aria-haspopup="dialog" :aria-controls="tableZoomId" aria-label="Phóng to bảng" class="inline-flex items-center gap-1.5 rounded-md bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
            <i class="fa-solid fa-up-right-and-down-left-from-center" aria-hidden="true"></i>
            <span>Phóng to</span>
          </a>
          <button @click="exportToCSV" class="inline-flex items-center gap-2 rounded-md bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
            <i class="fa-solid fa-file-arrow-down" aria-hidden="true"></i>
            <span>Xuất CSV</span>
          </button>
        </div>

        <!-- Message text (markdown rendered) -->
        <div class="mt-2 rounded-2xl rounded-tl-md bg-gray-100 px-3 py-2.5 text-sm text-gray-800 shadow-sm break-words">
          <MessageComponentAI :message="message.message" />
        </div>
        <div class="mt-1 flex items-center gap-2">
          <button type="button" @click.stop="copyMessage" class="inline-flex h-8 w-8 items-center justify-center rounded-full bg-white text-gray-600 ring-1 ring-inset ring-gray-200 shadow-sm hover:bg-gray-50">
            <i class="fa-regular fa-copy" aria-hidden="true"></i>
            <span class="sr-only">Sao chép nội dung</span>
          </button>
        </div>
      </template>

      <template v-else>
        <!-- Simple AI bubble -->
        <div class="rounded-2xl rounded-tl-md bg-gray-100 px-3 py-2.5 text-sm text-gray-800 shadow-sm break-words">
          <MessageComponentAI :message="message.message" />
        </div>
        <div class="mt-1 flex items-center gap-2">
          <button type="button" @click.stop="copyMessage" class="inline-flex h-8 w-8 items-center justify-center rounded-full bg-white text-gray-600 ring-1 ring-inset ring-gray-200 shadow-sm hover:bg-gray-50">
            <i class="fa-regular fa-copy" aria-hidden="true"></i>
            <span class="sr-only">Sao chép nội dung</span>
          </button>
        </div>
      </template>
      <p class="mt-1 text-xs text-gray-500">AI<span v-if="time"> • {{ time }}</span></p>

      <!-- Image Lightbox (CSS-only :target) -->
      <div v-if="message.type === 'img'" :id="imgZoomId" class="lightbox pointer-events-none fixed inset-0 z-50 flex items-center justify-center bg-black/60 opacity-0">
        <a href="#" class="absolute inset-0" aria-label="Đóng phóng to"></a>
        <div class="relative w-[min(95vw,1100px)] max-h-[85vh] overflow-hidden rounded-lg bg-white shadow-2xl ring-1 ring-black/10">
          <div class="flex items-center justify-between border-b border-gray-200 px-3 py-2">
            <h3 class="text-sm font-medium text-gray-800">Ảnh</h3>
            <a href="#" role="button" aria-label="Đóng" class="inline-flex h-8 w-8 items-center justify-center rounded-md border border-gray-200 text-gray-700 hover:bg-gray-50">
              <i class="fa-solid fa-xmark" aria-hidden="true"></i>
            </a>
          </div>
          <div class="max-h-[calc(85vh-44px)] overflow-auto p-3">
            <img :src="imageSrcAI" alt="Ảnh phóng to" class="h-auto w-full rounded-lg border border-gray-200" />
          </div>
        </div>
      </div>

      <!-- Table Lightbox (if table_html) -->
      <div v-if="message.type === 'table_html'" :id="tableZoomId" class="lightbox pointer-events-none fixed inset-0 z-50 flex items-center justify-center bg-black/60 opacity-0">
        <a href="#" class="absolute inset-0" aria-label="Đóng phóng to"></a>
        <div class="relative w-[min(95vw,1100px)] max-h-[85vh] overflow-hidden rounded-lg bg-white shadow-2xl ring-1 ring-black/10">
          <div class="flex items-center justify-between gap-2 border-b border-gray-200 px-3 py-2">
            <h3 class="text-sm font-medium text-gray-800">Bảng số liệu</h3>
            <div class="flex items-center gap-2">
              <button @click="exportToCSV" class="inline-flex items-center gap-1.5 rounded-md bg-white px-3 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
                <i class="fa-solid fa-file-arrow-down" aria-hidden="true"></i>
                <span>Xuất CSV</span>
              </button>
              <a href="#" role="button" aria-label="Đóng" class="inline-flex h-8 w-8 items-center justify-center rounded-md border border-gray-200 text-gray-700 hover:bg-gray-50">
                <i class="fa-solid fa-xmark" aria-hidden="true"></i>
              </a>
            </div>
          </div>
          <div class="max-h-[calc(85vh-44px)] overflow-auto p-3">
            <div v-html="message.table_html" ref="tableOverlay" class="table-container max-w-full overflow-x-auto"></div>
          </div>
        </div>
      </div>
    </article>
  </li>
</template>

<script>
import CodeComponentAI from './CodeComponentAI.vue';
import MessageComponentAI from './MessageComponentAI.vue';
// Copy action handled via inline UI panel

export default {
    props: ['message', 'time'],
    components: { CodeComponentAI, MessageComponentAI },
    data() {
        const uid = Math.random().toString(36).slice(2);
        return {
            localCode: this.message.code,
            copyId: `copy-ai-${uid}`,
            copyPanelId: `copy-panel-ai-${uid}`,
            tableZoomId: `table-zoom-${uid}`,
            imgZoomId: `img-zoom-${uid}`,
        };
    },
    computed: {
        computedText() {
            return (this.message && this.message.message) ? this.message.message : '';
        },
        imageSrcAI() {
            return this.message && this.message.img_base64
                ? `data:image/png;base64,${this.message.img_base64}`
                : '';
        },
    },
    methods: {
        async copyText() {
            // Deprecated in favor of copyMessage (kept for backward compatibility)
            return this.copyMessage();
        },
        async copyMessage() {
            if (!this.message) return;
            const text = this.computedText;
            try {
                if (navigator.clipboard && window.isSecureContext) {
                    await navigator.clipboard.writeText(text);
                } else {
                    const ta = document.createElement('textarea');
                    ta.value = text;
                    ta.style.position = 'fixed';
                    ta.style.opacity = '0';
                    document.body.appendChild(ta);
                    ta.select();
                    document.execCommand('copy');
                    document.body.removeChild(ta);
                }
            } catch (err) {
                console.error('Copy failed', err);
            }
        },
        updateCode(newCode) {
            this.localCode = newCode;
            this.$emit('update:code', newCode);
            console.log("Code updated:", newCode);
        },
        handleRunAgain() {
            console.log('Run Again button clicked! ' + this.localCode);
        },

        exportToCSV() {
            const root = this.$refs.tableOverlay || this.$refs.tableWrapper;
            const table = root ? root.querySelector('table') : null;
            if (!table) {
                alert('Không tìm thấy bảng!');
                return;
            }
            const rows = table.querySelectorAll('tr');
            const csv = [];
            rows.forEach(row => {
                const cells = row.querySelectorAll('th, td');
                const rowData = [];
                cells.forEach(cell => {
                    rowData.push('"' + cell.textContent.trim().replace(/"/g, '""') + '"');
                });
                csv.push(rowData.join(','));
            });
            const csvContent = '\uFEFF' + csv.join('\n');
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'table_data.csv';
            document.body.appendChild(a);
            a.click();
            a.remove();
            setTimeout(() => URL.revokeObjectURL(url), 0);
        },
        downloadImage() {
            try {
                const b64 = (this.message && this.message.img_base64) ? this.message.img_base64 : '';
                if (!b64) return;
                const byteString = atob(b64);
                const len = byteString.length;
                const bytes = new Uint8Array(len);
                for (let i = 0; i < len; i++) bytes[i] = byteString.charCodeAt(i);
                const blob = new Blob([bytes], { type: 'image/png' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'image.png';
                document.body.appendChild(a);
                a.click();
                a.remove();
                setTimeout(() => URL.revokeObjectURL(url), 0);
            } catch (err) {
                console.error('Download image error:', err);
            }
        }
    }
};
</script>

<style>
/* Neutral table styling so v-html tables look tidy */
.table-container { overflow: auto; }
.table-container table { width: 100%; border-collapse: collapse; margin: 12px 0 0 0; }
.table-container th, .table-container td { padding: 10px 12px; border: 1px solid #e5e7eb; text-align: left; }
.table-container thead th { background: #f8fafc; color: #334155; font-weight: 600; font-size: 14px; }
.table-container tbody tr:nth-child(even) { background: #f9fafb; }
.table-container th[scope="row"] { color: #111827; font-weight: 600; }
</style>
