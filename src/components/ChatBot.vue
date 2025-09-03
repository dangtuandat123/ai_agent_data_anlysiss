<template>
  <!-- Chat UI matching the UI Kit (Tailwind-based) -->
  <!-- Skip to content link (a11y) -->
  <a href="#chat" class="sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 focus:z-50 focus:rounded-md focus:bg-blue-600 focus:px-3 focus:py-1.5 focus:text-white">Bỏ qua đến nội dung</a>
  <main id="chat" class="w-full h-[100dvh] box-border p-2 sm:p-3 md:p-4 overflow-hidden bg-white text-gray-900">
    <div class="relative h-full flex gap-0 lg:gap-4 overflow-hidden">
      <!-- Desktop sidebar toggle (peer) -->
      <input id="desktop-history-toggle" type="checkbox" class="peer absolute opacity-0 pointer-events-none" aria-hidden="true" />

      <!-- Sidebar (Lịch sử chat - Desktop) -->
      <aside role="complementary" aria-label="Lịch sử chat" class="hidden lg:flex h-full flex-col rounded-xl border border-gray-200 bg-white shadow-sm overflow-hidden peer-checked:lg:hidden">
        <div class="sticky top-0 z-10 border-b border-gray-200 bg-white/90 px-4 py-3 backdrop-blur">
          <h2 class="text-sm font-semibold text-gray-800">Lịch sử chat</h2>
          <p class="text-xs text-gray-500">Các đoạn hội thoại gần đây</p>
        </div>
        <div class="flex-1 overflow-y-auto p-3 sm:p-4">
          <ul role="list" class="space-y-2" aria-label="Danh sách hội thoại">
            <li>
              <a href="#" aria-current="page" class="group flex items-start gap-3 rounded-md border border-transparent px-3 py-2 hover:border-gray-200 hover:bg-gray-50 aria-[current=page]:border-gray-200 aria-[current=page]:bg-gray-50">
                <i class="fa-regular fa-message mt-0.5 text-gray-400 group-hover:text-gray-600" aria-hidden="true"></i>
                <div class="min-w-0">
                  <p class="truncate text-sm font-medium text-gray-800">Tóm tắt tài liệu PDF</p>
                  <p class="truncate text-xs text-gray-500">Bạn có thể tóm tắt file này không?</p>
                </div>
              </a>
            </li>
            <li>
              <a href="#" class="group flex items-start gap-3 rounded-md border border-transparent px-3 py-2 hover:border-gray-200 hover:bg-gray-50">
                <i class="fa-regular fa-message mt-0.5 text-gray-400 group-hover:text-gray-600" aria-hidden="true"></i>
                <div class="min-w-0">
                  <p class="truncate text-sm font-medium text-gray-800">Sinh kế hoạch học tập</p>
                  <p class="truncate text-xs text-gray-500">Môn: FE, thời lượng: 4 tuần</p>
                </div>
              </a>
            </li>
            <li>
              <a href="#" class="group flex items-start gap-3 rounded-md border border-transparent px-3 py-2 hover:border-gray-200 hover:bg-gray-50">
                <i class="fa-regular fa-message mt-0.5 text-gray-400 group-hover:text-gray-600" aria-hidden="true"></i>
                <div class="min-w-0">
                  <p class="truncate text-sm font-medium text-gray-800">Dịch câu tiếng Việt → Anh</p>
                  <p class="truncate text-xs text-gray-500">Xin chào, bạn khoẻ không?</p>
                </div>
              </a>
            </li>
          </ul>
        </div>
      </aside>

      <!-- Chat Column -->
      <section class="flex-1 flex h-full flex-col rounded-xl bg-white shadow-sm overflow-hidden peer-checked:lg:-ml-4">
        <!-- Header -->
        <header class="sticky top-0 z-20 flex items-center justify-between gap-2 bg-white/90 px-2 py-1.5 sm:px-3 sm:py-2 backdrop-blur">
          <div class="min-w-0">
            <h1 class="truncate text-sm sm:text-base font-semibold leading-tight">AI Chatbot</h1>
            <p class="hidden sm:block text-[11px] sm:text-xs text-gray-500 leading-tight">UI Kit • HTML + Tailwind (CDN)</p>
          </div>
          <div class="flex items-center gap-1.5">
            <!-- Mobile History Button -->
            <label
              for="mobile-history-toggle"
              role="button"
              tabindex="0"
              aria-haspopup="dialog"
              aria-controls="mobile-history-panel"
              aria-label="Mở lịch sử chat"
              class="lg:hidden inline-flex shrink-0 items-center gap-1.5 rounded-md border border-gray-200 bg-white h-8 sm:h-9 px-2.5 py-0 text-xs sm:text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50"
            >
              <i class="fa-regular fa-clock" aria-hidden="true"></i>
              <span class="hidden sm:inline leading-none">Lịch sử</span>
            </label>

            <!-- Desktop History Button (right, desktop only) -->
            <label
              for="desktop-history-toggle"
              role="button"
              tabindex="0"
              aria-label="Ẩn/Hiện lịch sử chat"
              class="desktop-history-btn hidden lg:inline-flex shrink-0 items-center gap-1.5 rounded-md border border-gray-200 bg-white h-8 sm:h-9 px-2.5 py-0 text-xs sm:text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50"
            >
              <i class="fa-regular fa-rectangle-list" aria-hidden="true"></i>
              <span class="hidden sm:inline leading-none">Lịch sử</span>
            </label>

            <!-- Settings Menu (Dropdown, no JS) -->
            <div class="relative">
              <input id="settings-toggle" type="checkbox" class="peer sr-only" aria-hidden="true" />
              <label
                for="settings-toggle"
                role="button"
                tabindex="0"
                aria-label="Mở cài đặt"
                aria-haspopup="menu"
                aria-controls="settings-menu"
                class="inline-flex shrink-0 items-center gap-1.5 rounded-md border border-gray-200 bg-white h-8 sm:h-9 px-2.5 py-0 text-xs sm:text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50"
              >
                <i class="fa-solid fa-gear" aria-hidden="true"></i>
                <span class="hidden sm:inline leading-none">Cài đặt</span>
              </label>

              <div
                id="settings-menu"
                role="menu"
                aria-label="Cài đặt ứng dụng"
                class="pointer-events-none absolute left-1/2 z-30 mt-2 w-[calc(100vw-2rem)] -translate-x-1/2 overflow-hidden rounded-lg border border-gray-200 bg-white opacity-0 shadow-lg outline-none transition peer-checked:pointer-events-auto peer-checked:opacity-100 sm:left-auto sm:right-0 sm:w-80 sm:translate-x-0"
              >
                <div class="max-h-[60vh] overflow-y-auto p-3 sm:p-4">
                  <h2 class="mb-3 text-sm font-semibold text-gray-800">Cài đặt</h2>
                  <div class="space-y-2">
                    <div class="flex items-center justify-between rounded-md border border-gray-200 p-3">
                      <div class="min-w-0">
                        <p class="text-sm font-medium text-gray-800">Giọng điệu AI</p>
                        <p class="text-xs text-gray-500">Trung lập (mặc định)</p>
                      </div>
                      <span class="rounded-full bg-gray-100 px-2 py-1 text-xs text-gray-700">Balanced</span>
                    </div>
                    <div class="flex items-center justify-between rounded-md border border-gray-200 p-3">
                      <div class="min-w-0">
                        <p class="text-sm font-medium text-gray-800">Hiển thị thời gian</p>
                        <p class="text-xs text-gray-500">Trong bong bóng tin nhắn</p>
                      </div>
                      <span class="rounded-full bg-gray-100 px-2 py-1 text-xs text-gray-700">Bật</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </header>

        <!-- Chat Body -->
        <div class="flex-1 overflow-y-auto px-3 py-3 sm:px-4 sm:py-4" ref="messageWindow" role="log" aria-live="polite" aria-relevant="additions text">
          <ol id="chat-list" class="space-y-3 w-full sm:w-[min(55vw,100%)] mx-auto">
            <!-- Welcome (first-time) as AI bubble -->
            <li v-if="isWelcomeMessage" class="flex items-start gap-3">
              <div class="mt-1 hidden h-8 w-8 flex-none select-none items-center justify-center rounded-full bg-gray-200 text-gray-700 sm:inline-flex" aria-hidden="true">
                <i class="fa-solid fa-robot"></i>
              </div>
              <article class="relative pt-2 max-w-full flex-1">
                <div class="rounded-2xl rounded-tl-md bg-gray-100 px-3 py-2.5 text-sm text-gray-800 shadow-sm">
                  <p>Xin chào! Mình là trợ lý AI. Mình có thể giúp gì cho bạn hôm nay?</p>
                </div>
                <p class="mt-1 text-xs text-gray-500">AI</p>
              </article>
            </li>

            <!-- Dynamic messages -->
            <component v-for="(componentData, index) in components" :key="index" :is="componentData.component" v-bind="componentData.props" />

            <!-- AI Responding + Steps -->
            <li v-if="isShowLoadMessage" role="listitem" class="flex items-start gap-3">
              <div class="mt-1 hidden h-8 w-8 flex-none select-none items-center justify-center rounded-full bg-gray-200 text-gray-700 sm:inline-flex" aria-hidden="true">
                <i class="fa-solid fa-robot"></i>
              </div>
              <article class="max-w-full flex-1" aria-live="polite">
                <div class="inline-flex items-center rounded-2xl rounded-tl-md bg-gray-100 px-3 py-2.5 text-sm text-gray-800 shadow-sm">
                  <i class="fa-solid fa-wand-magic-sparkles text-blue-600" aria-hidden="true"></i>
                  <span>AI đang phản hồi…</span>
                </div>
                <div class="mt-3 ai-flow" role="group" aria-label="Tiến trình AI">
                  <div class="ai-chip"><span class="icon-wrap"><i class="icon-step fa-solid fa-magnifying-glass-chart" aria-hidden="true"></i><i class="icon-check fa-solid fa-check" aria-hidden="true"></i></span><span>Phân tích EDA</span></div>
                  <span class="ai-join" aria-hidden="true"></span>
                  <div class="ai-chip"><span class="icon-wrap"><i class="icon-step fa-solid fa-list-check" aria-hidden="true"></i><i class="icon-check fa-solid fa-check" aria-hidden="true"></i></span><span>Lên kế hoạch</span></div>
                  <span class="ai-join" aria-hidden="true"></span>
                  <div class="ai-chip"><span class="icon-wrap"><i class="icon-step fa-solid fa-code" aria-hidden="true"></i><i class="icon-check fa-solid fa-check" aria-hidden="true"></i></span><span>Tạo code</span></div>
                  <span class="ai-join" aria-hidden="true"></span>
                  <div class="ai-chip"><span class="icon-wrap"><i class="icon-step fa-solid fa-square-check" aria-hidden="true"></i><i class="icon-check fa-solid fa-check" aria-hidden="true"></i></span><span>Kiểm tra</span></div>
                </div>
              </article>
            </li>
            <!-- TypingIndicator -->
            <li v-if="isShowLoadMessage" role="listitem" class="flex items-start gap-3">
              <div class="mt-1 hidden h-8 w-8 flex-none select-none items-center justify-center rounded-full bg-gray-200 text-gray-700 sm:inline-flex" aria-hidden="true">
                <i class="fa-solid fa-robot"></i>
              </div>
              <article class="max-w-full flex-1">
                <div class="inline-flex items-center rounded-2xl rounded-tl-md bg-gray-100 px-3 py-2.5 text-sm text-gray-800 shadow-sm" aria-live="polite">
                  <span class="sr-only">AI đang nhập...</span>
                  <span aria-hidden="true" class="typing-dots">
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                  </span>
                </div>
                <p class="mt-1 text-xs text-gray-500">AI đang nhập…</p>
              </article>
            </li>
          </ol>
        </div>

        <!-- Input Bar -->
        <footer class="bg-white/90 px-3 py-2 sm:px-4">
          <form action="#" aria-label="Gửi tin nhắn" class="space-y-1.5 w-full sm:w-[min(55vw,100%)] mx-auto" @submit.prevent>
            <div role="group" aria-label="Thanh soạn tin" aria-describedby="input-hint" class="chatgpt-bar relative rounded-2xl ring-1 ring-gray-200 bg-gray-50 px-2.5 py-1.5 shadow-sm transition-colors hover:ring-gray-300 focus-within:ring-2 focus-within:ring-blue-500 min-h-[48px]">
              <!-- Attachment button -->
              <input ref="fileInput" id="file-input" type="file" class="sr-only" multiple @change="onFileChange" />
              <label for="file-input" role="button" tabindex="0" aria-label="Tải lên tệp" class="absolute left-2 top-1/2 -translate-y-1/2 inline-flex h-9 w-9 sm:h-10 sm:w-10 items-center justify-center rounded-full text-gray-600 hover:bg-gray-100">
                <i class="fa-solid fa-plus" aria-hidden="true"></i>
                <span class="sr-only">Chọn tệp từ máy</span>
              </label>

              <!-- Message textarea -->
              <label for="message" class="sr-only">Nội dung tin nhắn</label>
              <textarea
                id="message"
                ref="messageInput"
                name="message"
                v-model="prompt"
                placeholder="Nhập tin nhắn..."
                aria-label="Nội dung tin nhắn"
                @input="adjustRows"
                @keydown="onTextareaKeydown"
                :rows="rows"
                class="chatgpt-textarea block w-full bg-transparent border-0 pl-12 pr-12 py-2 text-[15px] leading-6 placeholder:text-gray-500 focus:outline-none focus:ring-0 overflow-y-auto resize-none min-h-10"
              ></textarea>

              <!-- Send button (right inside) -->
              <button type="button" @click="addMessageHuman" aria-label="Gửi tin nhắn" class="btn-send absolute right-2 top-1/2 -translate-y-1/2 inline-flex h-9 w-9 items-center justify-center rounded-full text-gray-600 hover:bg-gray-100 hover:text-gray-900 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500">
                <i class="fa-solid fa-paper-plane" aria-hidden="true"></i>
                <span class="sr-only">Gửi</span>
              </button>
            </div>

            <!-- Suggestion chips (sm+) -->
            <nav aria-label="Gợi ý nhanh" class="hidden sm:block mt-1.5 -mx-1 px-1 overflow-x-auto">
              <div class="flex items-center gap-2 whitespace-nowrap">
              <button type="button" class="inline-flex items-center gap-1.5 rounded-full bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50" @click="applySuggestion('Tóm tắt file PDF này giúp mình với?')">
                <i class="fa-regular fa-lightbulb text-gray-500" aria-hidden="true"></i>
                <span>Tóm tắt PDF</span>
              </button>
              <button type="button" class="inline-flex items-center gap-1.5 rounded-full bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50" @click="applySuggestion('Tạo kế hoạch học tập front-end trong 4 tuần')">
                <i class="fa-regular fa-calendar text-gray-500" aria-hidden="true"></i>
                <span>Kế hoạch học tập</span>
              </button>
              <button type="button" class="inline-flex items-center gap-1.5 rounded-full bg-white px-2.5 py-1.5 text-xs font-medium text-gray-700 ring-1 ring-inset ring-gray-300 shadow-sm hover:bg-gray-50" @click="applySuggestion('Dịch đoạn văn sau sang tiếng Anh: Xin chào, bạn khoẻ không?')">
                <i class="fa-solid fa-language text-gray-500" aria-hidden="true"></i>
                <span>Dịch nhanh</span>
              </button>
              </div>
            </nav>

            <!-- Selected Files Preview (rich) -->
            <div v-if="selectedFiles.length" aria-label="Tệp đã chọn" class="!mt-2" id="selected-files" role="region">
              <div class="inline-flex w-[min(100vw,100%)] items-start gap-2 rounded-2xl bg-white p-2.5 sm:p-3 ring-1 ring-gray-200 shadow-sm">
                <i class="fa-solid fa-paperclip mt-1.5 text-gray-500" aria-hidden="true"></i>
                <div class="min-w-0 flex-1">
                  <div class="mb-1 flex items-center justify-between gap-2">
                    <p class="text-xs font-medium text-gray-700">Tệp đã chọn ({{ selectedFiles.length }})</p>
                    <button type="button" @click="clearFiles" aria-label="Xóa tất cả" class="inline-flex items-center gap-1 rounded px-2 py-0.5 text-[11px] font-medium text-gray-600 ring-1 ring-inset ring-gray-200 hover:bg-gray-50">
                      <i class="fa-regular fa-trash-can" aria-hidden="true"></i>
                      <span>Xóa tất cả</span>
                    </button>
                  </div>
                  <ul class="divide-y divide-gray-200" role="list">
                    <li v-for="(file, index) in selectedFiles" :key="index" class="flex items-center gap-3 py-1.5 first:pt-0 last:pb-0" role="listitem">
                      <div :class="['flex h-8 w-8 flex-none items-center justify-center rounded ring-1 ring-inset', fileMeta(file).bgClass, fileMeta(file).ringClass, fileMeta(file).textClass]">
                        <i :class="fileMeta(file).icon" aria-hidden="true"></i>
                      </div>
                      <div class="min-w-0">
                        <p class="truncate max-w-[240px] sm:max-w-[360px] text-sm font-medium text-gray-900">{{ file.name }}</p>
                        <p class="text-xs text-gray-500">{{ fileMeta(file).label }}</p>
                      </div>
                      <button type="button" aria-label="Bỏ tệp này" @click="removeFile(index)" class="ml-auto inline-flex h-7 w-7 items-center justify-center rounded-md text-gray-500 ring-1 ring-inset ring-gray-200 hover:bg-gray-100 hover:text-gray-700">
                        <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                      </button>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <p id="input-hint" class="hidden text-xs text-gray-500 sm:block">Mẹo: Enter để gửi • Shift+Enter để xuống dòng.</p>
          </form>
        </footer>
      </section>
    </div>

    <!-- Mobile History Drawer (no JS) -->
    <div class="lg:hidden">
      <input id="mobile-history-toggle" type="checkbox" class="peer sr-only" aria-hidden="true" />
      <!-- Overlay -->
      <label for="mobile-history-toggle" class="pointer-events-none fixed inset-0 z-40 bg-black/40 opacity-0 transition peer-checked:pointer-events-auto peer-checked:opacity-100" aria-hidden="true"></label>
      <!-- Panel -->
      <aside id="mobile-history-panel" role="dialog" aria-modal="true" aria-label="Lịch sử chat" class="fixed inset-y-0 left-0 z-50 w-[92%] max-w-xs translate-x-[-100%] overflow-hidden rounded-r-xl border-r border-gray-200 bg-white shadow-xl transition-transform duration-200 ease-out peer-checked:translate-x-0">
        <div class="sticky top-0 z-10 border-b border-gray-200 bg-white/90 px-4 py-3 backdrop-blur">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-sm font-semibold text-gray-800">Lịch sử chat</h2>
              <p class="text-xs text-gray-500">Các đoạn hội thoại gần đây</p>
            </div>
            <label for="mobile-history-toggle" role="button" aria-label="Đóng lịch sử" class="inline-flex h-8 w-8 items-center justify-center rounded-md border border-gray-200 text-gray-700 hover:bg-gray-50">
              <i class="fa-solid fa-xmark" aria-hidden="true"></i>
            </label>
          </div>
        </div>
        <div class="flex-1 overflow-y-auto p-3 sm:p-4">
          <ul role="list" class="space-y-2" aria-label="Danh sách hội thoại">
            <li>
              <a href="#" aria-current="page" class="group flex items-start gap-3 rounded-md border border-transparent px-3 py-2 hover:border-gray-200 hover:bg-gray-50 aria-[current=page]:border-gray-200 aria-[current=page]:bg-gray-50">
                <i class="fa-regular fa-message mt-0.5 text-gray-400 group-hover:text-gray-600" aria-hidden="true"></i>
                <div class="min-w-0">
                  <p class="truncate text-sm font-medium text-gray-800">Tóm tắt tài liệu PDF</p>
                  <p class="truncate text-xs text-gray-500">Bạn có thể tóm tắt file này không?</p>
                </div>
              </a>
            </li>
            <li>
              <a href="#" class="group flex items-start gap-3 rounded-md border border-transparent px-3 py-2 hover:border-gray-200 hover:bg-gray-50">
                <i class="fa-regular fa-message mt-0.5 text-gray-400 group-hover:text-gray-600" aria-hidden="true"></i>
                <div class="min-w-0">
                  <p class="truncate text-sm font-medium text-gray-800">Sinh kế hoạch học tập</p>
                  <p class="truncate text-xs text-gray-500">Môn: FE, thời lượng: 4 tuần</p>
                </div>
              </a>
            </li>
            <li>
              <a href="#" class="group flex items-start gap-3 rounded-md border border-transparent px-3 py-2 hover:border-gray-200 hover:bg-gray-50">
                <i class="fa-regular fa-message mt-0.5 text-gray-400 group-hover:text-gray-600" aria-hidden="true"></i>
                <div class="min-w-0">
                  <p class="truncate text-sm font-medium text-gray-800">Dịch câu tiếng Việt → Anh</p>
                  <p class="truncate text-xs text-gray-500">Xin chào, bạn khoẻ không?</p>
                </div>
              </a>
            </li>
          </ul>
        </div>
      </aside>
    </div>
  </main>
</template>

<script>
import MessageAI from './MessageAI.vue';
import MessageHuman from './MessageHuman.vue';
import axios from 'axios';
// UI components (messages)

const apiClient = axios.create({
  baseURL: 'http://localhost:5000',
  withCredentials: true
});

export default {
  data() {
    return {
      isNavBarShow: true,
      components: [],
      prompt: '',
      rows: 1,
      minRows: 1,
      maxRows: 5,
      isShowLoadMessage: false,
      isWelcomeMessage: true,
      selectedFiles: [],
      file_name_list: [],
    };
  },
  components: {
    MessageAI,
    MessageHuman,
  },
  mounted() {
    this.scrollToBottom();
    this.$nextTick(() => {
      const ta = this.$refs.messageInput;
      if (ta) this.autoResize(ta);
    });
  },
  methods: {
    autoResize(ta) {
      if (!ta) return;
      // Reset to let scrollHeight reflect content
      ta.style.height = 'auto';
      const style = window.getComputedStyle(ta);
      const lineHeight = parseFloat(style.lineHeight) || 20;
      const paddingTop = parseFloat(style.paddingTop) || 0;
      const paddingBottom = parseFloat(style.paddingBottom) || 0;
      const minHeight = lineHeight + paddingTop + paddingBottom; // 1 line baseline
      const maxHeight = (this.maxRows * lineHeight) + paddingTop + paddingBottom;
      const natural = ta.scrollHeight; // includes padding
      const desired = Math.max(minHeight, Math.min(natural, maxHeight));
      ta.style.height = desired + 'px';
      ta.style.overflowY = (natural > maxHeight) ? 'auto' : 'hidden';
      ta.scrollTop = 0; // ensure placeholder stays at top when empty
    },
    onTextareaKeydown(e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        this.addMessageHuman();
      }
    },
    applySuggestion(text) {
      this.prompt = text;
      this.$nextTick(() => {
        const ta = this.$refs.messageInput;
        if (ta) {
          ta.dispatchEvent(new Event('input', { bubbles: true }));
          ta.focus();
        }
      });
    },
    adjustRows(event) {
      const ta = event.target;
      this.autoResize(ta);
    },

    formatTime(d = new Date()) {
      const hh = String(d.getHours()).padStart(2, '0');
      const mm = String(d.getMinutes()).padStart(2, '0');
      return `${hh}:${mm}`;
    },

    async addMessageHuman() {
      if (this.prompt !== '') {
        this.components.push({
          component: 'MessageHuman',
          props: { message: this.prompt, listFile: this.selectedFiles.map(file => file.name), time: this.formatTime() }
        });
        this.isShowLoadMessage = true;
        this.isWelcomeMessage = false;

        if (this.selectedFiles.length > 0) {
          this.file_name_list = await this.uploadFiles();
        }
        setTimeout(() => {
        console.log("Hành động sau khi trì hoãn");
      }, 1000);

        this.selectedFiles = [];

        this.messageToAgent();

        this.prompt = '';
        this.rows = 1;
        this.$nextTick(() => {
          const ta = this.$refs.messageInput;
          if (ta) {
            ta.style.height = '';
            this.autoResize(ta);
          }
          this.scrollToBottom();
        });
      }
    },


    scrollToBottom() {
      this.$nextTick(() => {
        const messageWindow = this.$refs.messageWindow;
        if (messageWindow) {
          messageWindow.scrollTop = messageWindow.scrollHeight;
        }
      });
    },

    async messageToAgent() {
      try {
        const response = await apiClient.post('/api/chattest', {
          prompt: this.prompt,
          file_name_list: this.file_name_list
        });
        this.components.push({
          component: 'MessageAI',
          props: { message: response.data.message, time: this.formatTime() }
        });
        this.isShowLoadMessage = false;
        this.scrollToBottom();
      } catch (error) {
        console.error('Có lỗi khi gọi API:', error);
      }
    },

    onFileChange(event) {
      const files = Array.from(event.target.files);
      this.selectedFiles = [...this.selectedFiles, ...files];
    },

    removeFile(index) {
      this.selectedFiles.splice(index, 1);
    },

    clearFiles() {
      this.selectedFiles = [];
    },

    fileMeta(file) {
      const type = file.type || '';
      const sizeKB = file.size ? Math.round(file.size / 1024) : 0;
      const ext = (file.name.split('.').pop() || '').toLowerCase();
      const label = (() => {
        if (type.startsWith('image/')) return `${ext.toUpperCase()} • ${sizeKB} KB`;
        if (type === 'application/pdf') return `PDF • ${sizeKB} KB`;
        if (ext === 'doc' || ext === 'docx') return `DOCX • ${sizeKB} KB`;
        if (ext === 'csv') return `CSV • ${sizeKB} KB`;
        if (ext === 'xls' || ext === 'xlsx') return `${ext.toUpperCase()} • ${sizeKB} KB`;
        return `${ext.toUpperCase()} • ${sizeKB} KB`;
      })();
      if (type === 'application/pdf' || ext === 'pdf') {
        return { icon: 'fa-solid fa-file-pdf', bgClass: 'bg-red-50', ringClass: 'ring-red-100', textClass: 'text-red-600', label };
      }
      if (ext === 'doc' || ext === 'docx') {
        return { icon: 'fa-solid fa-file-word', bgClass: 'bg-blue-50', ringClass: 'ring-blue-100', textClass: 'text-blue-600', label };
      }
      if (ext === 'csv') {
        return { icon: 'fa-solid fa-file-csv', bgClass: 'bg-lime-50', ringClass: 'ring-lime-100', textClass: 'text-lime-700', label };
      }
      if (ext === 'xls' || ext === 'xlsx') {
        return { icon: 'fa-solid fa-file-excel', bgClass: 'bg-green-50', ringClass: 'ring-green-100', textClass: 'text-green-600', label };
      }
      if (type.startsWith('image/')) {
        return { icon: 'fa-solid fa-file-image', bgClass: 'bg-emerald-50', ringClass: 'ring-emerald-100', textClass: 'text-emerald-600', label };
      }
      return { icon: 'fa-regular fa-file', bgClass: 'bg-gray-50', ringClass: 'ring-gray-200', textClass: 'text-gray-600', label };
    },

    async uploadFiles() {
      if (this.selectedFiles.length === 0) return;
      let formData = new FormData();
      this.selectedFiles.forEach(file => formData.append("files", file));

      try {
        const res = await apiClient.post('/upload', formData, {
          headers: { "Content-Type": "multipart/form-data" }
        });
        return res.data.file_name_list;
      } catch (err) {
        console.error("Lỗi upload:", err);
      }
    }
  }
};
</script>

<style>
/* Subtle scrollbar */
* { scrollbar-width: thin; scrollbar-color: rgb(209 213 219) transparent; }
*::-webkit-scrollbar { height: 8px; width: 8px; }
*::-webkit-scrollbar-thumb { background: rgb(209 213 219); border-radius: 999px; }

/* Desktop History toggle effects (no JS) */
@media (min-width: 1024px) {
  #desktop-history-toggle ~ aside {
    width: 20rem;
    transition: width 300ms ease, transform 300ms ease, opacity 300ms ease;
  }
  #desktop-history-toggle:checked ~ aside {
    display: flex !important;
    width: 0;
    transform: translateX(-0.5rem);
    opacity: 0;
    pointer-events: none;
  }
  #desktop-history-toggle ~ section {
    flex: 1 1 0%;
    transition: all 300ms ease;
  }
}

/* Image Lightbox (if used) */
.lightbox:target { opacity: 1 !important; pointer-events: auto !important; }

/* Typing indicator */
.typing-dots { display: inline-flex; align-items: center; gap: 0.35rem; }
.typing-dots .dot { width: 0.42rem; height: 0.42rem; border-radius: 9999px; background: rgb(148 163 184); opacity: 0.7; animation: typingBounce 1.2s ease-in-out infinite; }
.typing-dots .dot:nth-child(2) { animation-delay: .15s; }
.typing-dots .dot:nth-child(3) { animation-delay: .3s; }
@keyframes typingBounce { 0%, 80%, 100% { transform: translateY(0); opacity: .6; } 40% { transform: translateY(-4px); opacity: 1; } }

/* ChatGPT-like input bar */
.chatgpt-bar { position: relative; }
.chatgpt-bar .btn-send { opacity: .5; }
.chatgpt-bar:has(textarea:not(:placeholder-shown)) .btn-send { opacity: 1; pointer-events: auto; }
.chatgpt-textarea { scrollbar-width: thin; }
.chatgpt-textarea::-webkit-scrollbar { width: 6px; }
.chatgpt-textarea::-webkit-scrollbar-thumb { background: rgb(209 213 219); border-radius: 999px; }

/* AI responding steps (ai-flow) */
.ai-flow { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem; }
.ai-chip { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 0.75rem; border-radius: 9999px; font-size: 13px; line-height: 1.2; font-weight: 500; background: #f1f5f9; border: 1px solid #e2e8f0; color: #334155; animation: aiChipState 8s linear infinite both; }
.ai-flow .ai-chip { --delay: 0s; animation-delay: var(--delay); }
.ai-flow .ai-chip:nth-of-type(2) { --delay: 2s; }
.ai-flow .ai-chip:nth-of-type(3) { --delay: 4s; }
.ai-flow .ai-chip:nth-of-type(4) { --delay: 6s; }
.ai-chip .icon-wrap { position: relative; width: 18px; height: 18px; display: inline-block; }
.ai-chip .icon-wrap .icon-step, .ai-chip .icon-wrap .icon-check { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; }
.ai-chip .icon-wrap .icon-step { opacity: .95; color: #334155; animation: aiChipIconStep 8s linear infinite both; animation-delay: var(--delay); }
.ai-chip .icon-wrap .icon-check { opacity: 0; color: #16a34a; animation: aiChipIconCheck 8s linear infinite both; animation-delay: var(--delay); }
@keyframes aiChipState { 0% { background: #f1f5f9; border-color: #e2e8f0; color: #334155; opacity: .95; } 5% { background: #eff6ff; border-color: #bfdbfe; color: #1d4ed8; box-shadow: 0 0 0 2px rgba(59,130,246,0.10) inset, 0 2px 8px rgba(59,130,246,0.08); } 10%, 100% { background: #ecfdf5; border-color: #86efac; color: #065f46; box-shadow: 0 0 0 1px rgba(22,163,74,0.15) inset; } }
@keyframes aiChipIconStep { 0% { opacity: .9; } 10%, 100% { opacity: 0; } }
@keyframes aiChipIconCheck { 0% { opacity: 0; transform: scale(.9); } 10%, 100% { opacity: 1; transform: scale(1); } }
.ai-join { width: 36px; height: 3px; border-radius: 9999px; background: #e2e8f0; position: relative; overflow: hidden; }
.ai-join::after { content: ""; position: absolute; inset: 0; width: 0%; background: #86efac; animation: aiJoinFill 8s linear infinite both; }
.ai-flow > .ai-join { --delay: 1s; }
.ai-flow > .ai-join:nth-of-type(2) { --delay: 3s; }
.ai-flow > .ai-join:nth-of-type(3) { --delay: 5s; }
.ai-join::after { animation-delay: var(--delay); }
@keyframes aiJoinFill { 0% { width: 0%; } 25%, 100% { width: 100%; } }
@media (max-width: 639px) { .ai-join { display: none; } .ai-chip { font-size: 12px; padding: 0.45rem 0.625rem; } }
</style>
