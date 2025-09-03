<template>
  <div class="w-full rounded-2xl rounded-tl-md overflow-hidden shadow-sm min-w-0">
    <!-- Header bar -->
    <div class="flex items-center justify-between gap-2 bg-slate-800 text-slate-100 px-3 py-2 border-b border-slate-700">
      <div class="flex items-center gap-2 text-xs font-medium">
        <i :class="langIcon" aria-hidden="true"></i>
        <span>{{ langLabel }}</span>
      </div>
      <div class="flex items-center gap-1.5">
        <!-- Copy code button -->
        <button type="button" @click="copyCode" aria-label="Sao chép mã" class="inline-flex h-8 sm:h-9 items-center gap-1.5 rounded-md bg-white/10 px-3 text-xs font-medium text-white ring-1 ring-inset ring-white/10 shadow-sm hover:bg-white/15 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400">
          <i class="fa-regular fa-copy" aria-hidden="true"></i>
          <span>Copy</span>
        </button>
        <!-- Run again (UI only) -->
        <div class="relative inline-block">
          <input :id="runId" type="checkbox" class="peer sr-only" aria-hidden="true" />
          <label :for="runId" role="button" tabindex="0" :aria-controls="runPanelId" aria-label="Run code (demo)" class="inline-flex h-8 sm:h-9 items-center gap-1.5 rounded-md bg-white/10 px-3 text-xs font-medium text-white ring-1 ring-inset ring-white/10 shadow-sm hover:bg-white/15 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400">
            <i class="fa-solid fa-play" aria-hidden="true"></i>
            <span>Run again</span>
          </label>
          <div :id="runPanelId" role="dialog" aria-modal="false" aria-label="Kết quả chạy (demo)" class="pointer-events-none absolute right-0 top-9 z-20 w-[min(92vw,26rem)] overflow-hidden rounded-md border border-gray-200 bg-white text-xs text-gray-700 shadow-lg opacity-0 transition peer-checked:pointer-events-auto peer-checked:opacity-100">
            <div class="border-b border-gray-200 p-3">
              <p class="text-[11px] text-gray-500">Chạy code (UI demo, không thực thi)</p>
            </div>
            <div class="bg-slate-900 p-3 font-mono text-[12px] leading-6 text-slate-100 max-h-48 overflow-auto">$ ./run.sh</div>
          </div>
        </div>

        <!-- Edit code (overlay) -->
        <button type="button" @click="openEdit" class="inline-flex h-8 sm:h-9 items-center gap-1.5 rounded-md bg-white/10 px-3 text-xs font-medium text-white ring-1 ring-inset ring-white/10 shadow-sm hover:bg-white/15 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400">
          <i class="fa-solid fa-pen" aria-hidden="true"></i>
          <span>Sửa code</span>
        </button>

        <!-- Zoom code -->
        <a :href="`#${zoomId}`" role="button" aria-label="Phóng to code" class="inline-flex h-8 sm:h-9 items-center gap-1.5 rounded-md bg-white/10 px-3 text-xs font-medium text-white ring-1 ring-inset ring-white/10 shadow-sm hover:bg-white/15 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400">
          <i class="fa-solid fa-up-right-and-down-left-from-center" aria-hidden="true"></i>
          <span>Phóng to</span>
        </a>
      </div>
    </div>

    <!-- Code area -->
    <div class="bg-gradient-to-b from-slate-950 to-slate-900 max-h-[250px] overflow-auto overflow-x-auto">
      <pre class="m-0 p-3 text-[13px] leading-6"><code class="hljs !bg-transparent !text-slate-100" v-html="highlight.html"></code></pre>
    </div>
  </div>

  <!-- Code Zoom Lightbox (CSS-only via :target) -->
  <div :id="zoomId" class="lightbox pointer-events-none fixed inset-0 z-50 flex items-center justify-center bg-black/60 opacity-0">
    <a href="#" class="absolute inset-0" aria-label="Đóng phóng to"></a>
    <div class="relative w-[min(95vw,1100px)] max-h-[85vh] overflow-hidden rounded-lg bg-white shadow-2xl ring-1 ring-black/10">
      <div class="flex items-center justify-between border-b border-gray-200 px-3 py-2">
        <h3 class="text-sm font-medium text-gray-800">Mã nguồn ({{ langLabel }})</h3>
        <a href="#" role="button" aria-label="Đóng" class="inline-flex h-8 w-8 items-center justify-center rounded-md border border-gray-200 text-gray-700 hover:bg-gray-50">
          <i class="fa-solid fa-xmark" aria-hidden="true"></i>
        </a>
      </div>
      <div class="bg-slate-900 max-h-[calc(85vh-44px)] overflow-auto p-3">
        <pre class="m-0 text-[13px] leading-6"><code class="hljs !bg-transparent !text-slate-100" v-html="highlight.html"></code></pre>
      </div>
    </div>
  </div>

  <!-- Edit Overlay (Vue-driven) -->
  <div v-if="isEditMode" class="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
    <div class="relative w-[min(95vw,1100px)] max-h-[85vh] overflow-hidden rounded-lg bg-white shadow-2xl ring-1 ring-black/10">
      <div class="flex items-center justify-between border-b border-gray-200 px-3 py-2">
        <h3 class="text-sm font-medium text-gray-800">Sửa mã ({{ langLabel }})</h3>
        <button type="button" @click="closeEdit" aria-label="Đóng" class="inline-flex h-8 w-8 items-center justify-center rounded-md border border-gray-200 text-gray-700 hover:bg-gray-50">
          <i class="fa-solid fa-xmark" aria-hidden="true"></i>
        </button>
      </div>
      <div class="max-h-[calc(85vh-44px)] overflow-auto p-3 bg-slate-900">
        <textarea v-model="localCode" class="w-full h-[60vh] resize-none rounded-md bg-slate-900 text-slate-100 font-mono text-[13px] leading-6 p-3 ring-1 ring-slate-700 focus:outline-none"></textarea>
      </div>
      <div class="flex items-center justify-end gap-2 border-t border-gray-200 px-3 py-2 bg-white">
        <button type="button" @click="saveEdit" class="inline-flex items-center gap-1.5 rounded-md bg-blue-600 px-3 py-1.5 text-xs font-medium text-white shadow-sm hover:bg-blue-700">
          <i class="fa-solid fa-floppy-disk" aria-hidden="true"></i>
          <span>Lưu</span>
        </button>
        <button type="button" @click="closeEdit" class="inline-flex items-center gap-1.5 rounded-md bg-white px-3 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50">
          <i class="fa-solid fa-xmark" aria-hidden="true"></i>
          <span>Hủy</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import hljs from 'highlight.js';
import 'highlight.js/styles/github-dark.css';

export default {
  props: ['code'],
  data() {
    const uid = Math.random().toString(36).slice(2);
    return {
      localCode: this.code,
      runId: `run-code-${uid}`,
      runPanelId: `run-code-panel-${uid}`,
      zoomId: `code-zoom-${uid}`,
      isEditMode: false,
    };
  },
  computed: {
    highlight() {
      const res = hljs.highlightAuto(this.localCode || '');
      return { html: res.value, language: res.language || 'code' };
    },
    langLabel() {
      const map = { python: 'Python', javascript: 'JavaScript', typescript: 'TypeScript', json: 'JSON', bash: 'Bash' };
      return map[this.highlight.language] || this.highlight.language.toUpperCase();
    },
    langIcon() {
      if (this.highlight.language === 'python') return 'fa-brands fa-python text-blue-300';
      if (this.highlight.language === 'javascript' || this.highlight.language === 'typescript') return 'fa-brands fa-js text-yellow-300';
      return 'fa-solid fa-code text-slate-300';
    }
  },
  methods: {
    runAgain() {
      this.$emit('run-again');
    },
    copyCode() {
      try {
        const text = this.localCode || '';
        if (navigator.clipboard && window.isSecureContext) {
          navigator.clipboard.writeText(text);
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
      } catch (e) {
        console.error('Copy code failed', e);
      }
    },
    openEdit() { this.isEditMode = true; },
    closeEdit() { this.isEditMode = false; },
    saveEdit() {
      this.$emit('update:code', this.localCode);
      this.isEditMode = false;
    }
  }
};
</script>

<style scoped>
/* Presentation entirely via Tailwind classes */
</style>
