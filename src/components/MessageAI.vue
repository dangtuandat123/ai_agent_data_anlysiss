<template>
    <div class="message-list-ai">
        <div class="message-item">
            <!-- Render markdown -->
            <div class="message-content" v-html="renderedMarkdown"></div>

            <div class="button">
                <ButtonCopy @click="copyText" />
            </div>
        </div>
    </div>
</template>

<script>
import ButtonCopy from './ButtonCopy.vue';
import { marked } from 'marked';
import DOMPurify from 'dompurify';

export default {
    props: ['message'],
    components: { ButtonCopy },
    computed: {
        renderedMarkdown() {
            // Chuyển markdown -> HTML và lọc an toàn
            const rawHtml = marked(this.message || '');
            return DOMPurify.sanitize(rawHtml);
        }
    },
    methods: {
        async copyText() {
            if (!this.message) return;
            try {
                await navigator.clipboard.writeText(this.message);
                console.log("Copied!");
            } catch (err) {
                console.error("Copy failed", err);
            }
        }
    }
};
</script>

<style scoped>


.button {
    display: flex;
    margin-top: 4px;
}

.section_nav_bar_chat_window {
    display: flex;
}

.message-list-ai {
  margin-bottom: 15px;
  padding: 10px;
  border-radius: 10px;
  /* border: 1px solid var(--border-color); */

  /* trạng thái ban đầu khi mới mount */
  opacity: 0;
  transform: translateY(10px);
  animation: messageFadeIn 0.8s ease-out forwards;
}

@keyframes messageFadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


.message-content {
    word-break: break-word;
}
</style>