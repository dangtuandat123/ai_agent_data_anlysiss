<template>
    <div>
      <div class="particles" id="particlesContainer"></div>
      <div class="data-streams" id="dataStreams"></div>
      <div class="orb orb1"></div>
      <div class="orb orb2"></div>
      <div class="orb orb3"></div>
  
      <!-- Navigation -->
      <nav style="display: none;">
        <div class="nav-container">
          <a href="#top" class="logo">DataAnalysis AI</a>
          <ul class="nav-links">
            <li><a href="#features">Features</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#stats">Stats</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
          <div class="nav-bottom">
            <a href="#" class="cyber-button">Dùng ngay</a>
          </div>
        </div>
      </nav>
  
      <!-- Mobile Menu -->
      <div style="display: none;" class="mobile-menu-overlay" id="mobileMenuOverlay"></div>
      <div class="mobile-menu" id="mobileMenu">
        <div class="mobile-menu-header">
          <a href="#top" class="mobile-menu-logo">NexusFlow</a>
          <button class="mobile-menu-close" id="mobileMenuClose">✕</button>
        </div>
        <div class="mobile-menu-cta">
          <a href="#" class="cyber-button">Access Terminal</a>
        </div>
        <nav class="mobile-menu-nav">
          <ul>
            <li><a href="#features">Features</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#stats">Stats</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </div>
  
      <!-- Chat Window Section -->
      <section class="section_nav_bar_chat_window" style="padding: 7px; height: 100vh;">
        <div v-bind:class="{ 'nav_bar_chat_window': true, 'show': isNavBarShow }"></div>
  
        <div class="chat-window">
          <div style="z-index: 1000;">
            <a @click="toggleNavBar" class="btn-menuchat">☰</a>
          </div>
          <div class="message-window" ref="messageWindow" style="height: 100%; margin-top: 40px;">
            <div v-show="isWelcomeMessage" style="display: flex; justify-content: center; align-items: center; width: 100%; height: 100%;">
              <a href="#top" class="logo">Chào! Tôi có thể giúp gì cho bạn?</a>
            </div>
            <component v-for="(componentData, index) in components" :key="index" :is="componentData.component" v-bind="componentData.props" />
            <LoadMessage :class="{ show: isShowLoadMessage }" />
          </div>
          
          <div style="display: flex; justify-content: center; align-items: center; line-height: 0px;">
            <div class="prompt_input" style="width: 60%;">
              <label for="message">Prompt</label>
              <textarea id="message" name="message" placeholder="Nhập yêu cầu của bạn..." required v-model="prompt" @input="adjustRows" :rows="rows"></textarea>
            </div>
            <button @click="addMessageHuman" class="button_send">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                <path fill="none" d="M0 0h24v24H0z"></path>
                <path fill="currentColor" d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"></path>
              </svg>
              <span></span>
            </button>
            <ButtonUploadFile @click="triggerFileInput" />
            <input ref="fileInput" type="file" @change="onFileChange" style="display: none;" multiple />
          </div>
          
          <!-- File List -->
          <div v-show="selectedFiles.length > 0" style="display: flex; justify-content: center; align-items: center; line-height: 0px; position: relative; right: 59px; margin-top: 7px;">
            <div class="list-file-window" style="width: 60%;">
              <div v-for="(file, index) in selectedFiles" :key="index" class="file-item" style="margin: 5px 0px;">
                <span>{{ file.name }}</span>
                <svg @click="removeFile(index)" class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" style="margin-left: 4px;" viewBox="0 0 24 24">
                  <path fill-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm7.707-3.707a1 1 0 0 0-1.414 1.414L10.586 12l-2.293 2.293a1 1 0 1 0 1.414 1.414L12 13.414l2.293 2.293a1 1 0 0 0 1.414-1.414L13.414 12l2.293-2.293a1 1 0 0 0-1.414-1.414L12 10.586 9.707 8.293Z" clip-rule="evenodd" />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import MessageAI from './MessageAI.vue';
  import MessageHuman from './MessageHuman.vue';
  import axios from 'axios';
  import ButtonUploadFile from './ButtonUploadFile.vue';
  import LoadMessage from './LoadMessage.vue';
  
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
      ButtonUploadFile,
      LoadMessage,
    },
    mounted() {
      this.scrollToBottom();
    },
    methods: {
      adjustRows(event) {
        const ta = event.target;
        const style = window.getComputedStyle(ta);
        let lineHeight = parseFloat(style.lineHeight);
        if (isNaN(lineHeight)) {
          const fontSize = parseFloat(style.fontSize) || 16;
          lineHeight = fontSize * 1.2;
        }
  
        const paddingTop = parseFloat(style.paddingTop) || 0;
        const paddingBottom = parseFloat(style.paddingBottom) || 0;
        ta.style.height = 'auto';
        ta.style.overflowY = 'hidden';
        const contentHeight = ta.scrollHeight - paddingTop - paddingBottom;
        const computedRows = Math.round(contentHeight / lineHeight);
        const maxHeight = this.maxRows * lineHeight + paddingTop + paddingBottom;
  
        if (computedRows > this.maxRows) {
          ta.style.height = maxHeight + 'px';
          ta.style.overflowY = 'auto';
        } else {
          ta.style.height = contentHeight + 'px';
        }
      },
  
      toggleNavBar() {
        this.isNavBarShow = !this.isNavBarShow;
      },
  
      async addMessageHuman() {
        if (this.prompt !== '') {
          this.components.push({
            component: 'MessageHuman',
            props: { message: this.prompt, listFile: this.selectedFiles.map(file => file.name) }
          });
          this.isShowLoadMessage = true;
          this.isWelcomeMessage = false;
          if (this.selectedFiles.length > 0) {
            this.file_name_list = await this.uploadFiles();
          }
          this.selectedFiles = [];
          this.messageToAgent();
          this.prompt = '';
          this.rows = 1;
          this.scrollToBottom();
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
            props: { message: response.data.message }
          });
          this.isShowLoadMessage = false;
          this.scrollToBottom();
        } catch (error) {
          console.error('Có lỗi khi gọi API:', error);
        }
      },
  
      triggerFileInput() {
        this.$refs.fileInput.click();
      },
  
      onFileChange(event) {
        const files = Array.from(event.target.files);
        this.selectedFiles = [...this.selectedFiles, ...files];
      },
  
      removeFile(index) {
        this.selectedFiles.splice(index, 1);
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
  
  <style scoped>
  .section_nav_bar_chat_window {
    display: flex;
  }
  </style>
  