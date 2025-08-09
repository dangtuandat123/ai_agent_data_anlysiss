<template>
    <div class="message-list-ai">
        <div class="message-item">
            <!-- Render markdown hoặc nội dung message -->
            <div class="message-content" v-html="renderedMessage"></div>
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
import hljs from 'highlight.js'; // Import Highlight.js
import 'highlight.js/styles/monokai-sublime.css'; // Import style theme của Highlight.js

export default {

    props: ['message'],
    components: { ButtonCopy },
    computed: {
        renderedMessage() {
            // Kiểm tra nếu message là mã code
            if (this.message.iscode) {
                // Render cả code và message. Code được render dưới dạng <pre><code>...</code></pre> và message dưới dạng HTML
                const messageHtml = marked(this.message.message || '');
                const codeHtml = this.highlightCode(this.message.code || '');  // Hiển thị code với Highlight.js
                const rawhtmlMessage = DOMPurify.sanitize(messageHtml);
                const img_base64 = this.message.img_base64 


                return `
            <div class="message-content">
                <div style="display: flex; align-items: center; margin-bottom:5px">
                    <img src="https://logos-world.net/wp-content/uploads/2021/10/Python-Emblem.png"  alt="" style="height: 18px;">
                    <strong>Python</strong>
                </div>
                <div class="code_div" style="border: 1px solid rgba(229, 231, 235, 0.2); border-radius: 10px; padding: 10px;background: #282c34; font-size:17px;margin-bottom:5px;overflow-x: hidden;overflow-y: auto;max-height: 290px;">
                    <pre><code>${codeHtml}</code></pre>
                </div>
                 <div style="display: flex; align-items: center; margin-bottom:5px;width: 100%;height: auto;max-width: 100%; padding:10px 10% 10px 10%">
                    <img src="data:image/png;base64,${img_base64}" alt="" style="width: 100%;height: auto;max-width: 100%; border-radius:10px">
                </div>
                <div class="message-text">${rawhtmlMessage}</div> <!-- Message được render dưới dạng HTML -->
               
                

            </div>
            <style>
                .code_div::-webkit-scrollbar-thumb {
                    background-color: #888 !important;
                    /* Màu sắc của phần tay cầm thanh cuộn */
                    border-radius: 3px !important;
                    /* Bo tròn tay cầm */
                }
            </style>
        `;
            }

            // // Kiểm tra nếu message là file (hoặc nội dung Markdown)
            // else if (this.message.isfile) {
            //     const rawHtml = marked(this.message.message || '');
            //     // Làm sạch HTML từ Markdown và trả về
            //     return DOMPurify.sanitize(rawHtml);
            // }

            // Nếu không phải code hay file, chỉ đơn giản là trả về message bình thường
            else {
                const rawHtml = marked(this.message.message || '');

                return DOMPurify.sanitize(rawHtml);
            }
        }

    },
    methods: {
        // Hàm highlight mã nguồn với Highlight.js
        highlightCode(code) {
            return hljs.highlightAuto(code).value;  // Chọn ngôn ngữ tự động và highlight code
        },

        async copyText() {
            if (!this.message) return;
            try {
                await navigator.clipboard.writeText(this.message.message);
                console.log("Copied!");
            } catch (err) {
                console.error("Copy failed", err);
            }
        }
    },
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

.button {
    display: flex;
    margin-top: 4px;
}

.message-list-ai {
    margin-bottom: 15px;
    padding: 10px;
    border-radius: 10px;
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

/* .code_div {
    background-color: #2d2d2d !important;
    padding: 10px!important;
    border-radius: 5px!important;
    font-size: 14px!important;
    color: #f8f8f2!important;
    border: 1px solid var(--border-color)!important;
    padding: 10px!important;

} */

.message-text {
    margin-top: 10px;
    color: #f5f5f5;
}
</style>
