<template>
    <div class="message-text" v-html="sanitizedMessage"></div>
  </template>
  
  <script>
  import { marked } from 'marked';
  import DOMPurify from 'dompurify';
  
  export default {
    props: ['message'],
    computed: {
      sanitizedMessage() {
        const rawHtml = marked(this.message || '');
        return DOMPurify.sanitize(rawHtml);
      }
    }
  };
  </script>
  