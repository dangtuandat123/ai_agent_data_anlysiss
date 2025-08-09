<template>
    <div style="display: flex; align-items: center; margin-bottom: 5px; margin-top: 5px;">
      <img src="https://logos-world.net/wp-content/uploads/2021/10/Python-Emblem.png" alt="" style="height: 18px;">
      <strong>Python</strong>
      <div class="button_action">
        <button class="button_edit_code">
          Run Again
        </button>
        <button class="button_edit_code" @click="toggleEditMode">
          {{ isEditMode ? 'Lưu' : 'Chỉnh sửa' }}
        </button>
        <!-- Nút Copy Code -->
        <ButtonCopy style="margin-bottom: 5px; margin-left: 5px;" @click="copyCode"/>
      </div>
    </div>
  
    <div class="code_div" :style="{
        border: '1px solid rgba(229, 231, 235, 0.2)',
        borderRadius: '20px',
        padding: '10px',
        background: '#282c34',
        fontSize: '17px',
        marginBottom: '5px',
        overflowX: 'hidden',
        overflowY: isEditMode ? 'hidden' : 'auto',  // Thay đổi overflow-y khi chỉnh sửa
        maxHeight: '290px'
    }">
      <pre v-if="!isEditMode"><code v-html="highlightedCode"></code></pre>
      <textarea v-if="isEditMode" v-model="localCode"
        style="width: 100%; height: 100%; background: #282c34; color: white; font-size: 17px; border: none; outline: none; resize: none; height: 290px;"></textarea>
    </div>
  </template>
  
  <script>
  import hljs from 'highlight.js';
  import 'highlight.js/styles/monokai-sublime.css';
  import ButtonCopy from './ButtonCopy.vue';
  
  export default {
    components: { ButtonCopy },
    props: ['code'],
    data() {
      return {
        isEditMode: false,
        localCode: this.code,
      };
    },
    computed: {
      highlightedCode() {
        return hljs.highlightAuto(this.localCode).value;
      }
    },
    methods: {
      toggleEditMode() {
        if (this.isEditMode) {
          this.$emit('update:code', this.localCode);
        }
        this.isEditMode = !this.isEditMode;
      },
      // Phương thức sao chép mã vào clipboard
      copyCode() {
        const textToCopy = this.isEditMode ? this.localCode : this.code;
        navigator.clipboard.writeText(textToCopy)
          
      }
    }
  };
  </script>
  
  <style scoped>
  :root {
    --primary-grey: #e5e7eb;
    --primary-orange: #f97316;
    --primary-purple: #7c3aed;
    --secondary-amber: #fbbf24;
    --dark-bg: #1a0b2e;
    --darker-bg: #0f051a;
    --card-bg: rgba(229, 231, 235, 0.03);
    --border-color: rgba(229, 231, 235, 0.2);
    --text-primary: #ffffff;
    --text-secondary: #a1a1aa;
    --primary-cyan: #00ffff;
    --primary-pink: #ff00ff;
    --card-bg-btn: rgba(123, 23, 90, 0.254);
  }
  
  .code_div::-webkit-scrollbar-thumb {
    background-color: #888 !important;
    border-radius: 3px !important;
  }
  
  .button_action{
    display: flex;
    align-items: center;
    margin-left: auto;
  }
  
  .button_edit_code {
    margin-left: auto;
    background-color: #1698d0;
    color: white;
    border: none;
    padding: 5px 15px;
    border-radius: 0.4rem;
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
    background-color: #28ccd8;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }
  
  .button_edit_code:active {
    transform: translateY(2px);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  }
  </style>
  