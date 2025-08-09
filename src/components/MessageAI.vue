<template>
    <div class="message-list-ai">
        <div class="message-item">
            <div class="message-content">
                <template v-if="message.iscode">
                    <!-- Hiển thị mã nguồn -->
                    <CodeComponentAI :code="localCode" @update:code="updateCode" />

                    <!-- Hiển thị hình ảnh -->
                    <ImageComponentAI :imgBase64="message.img_base64" />

                    <!-- Hiển thị message -->
                    <MessageComponentAI :message="message.message" />
                </template>

                <template v-else>
                    <!-- Nếu không phải code, chỉ render message bình thường -->
                    <MessageComponentAI :message="message.message" />
                </template>
            </div>

            <div class="button">
                <ButtonCopy @click="copyText" />
            </div>
        </div>
    </div>
</template>

<script>
import CodeComponentAI from './CodeComponentAI.vue';
import MessageComponentAI from './MessageComponentAI.vue';
import ImageComponentAI from './ImageComponentAI.vue';
import ButtonCopy from './ButtonCopy.vue';

export default {
    props: ['message'],
    components: { CodeComponentAI, MessageComponentAI, ImageComponentAI, ButtonCopy },
    data() {
        return {
            // Tạo bản sao của message để tránh thay đổi trực tiếp prop
            localCode: this.message.code,
        };
    },
    methods: {
        async copyText() {
            if (!this.message) return;
            try {
                await navigator.clipboard.writeText(this.message.message);
                console.log("Copied!");
            } catch (err) {
                console.error("Copy failed", err);
            }
        },
        updateCode(newCode) {
            // Cập nhật mã code mới trong bản sao
            this.localCode = newCode;
            // Emit sự thay đổi để thông báo với component cha
            this.$emit('update:code', newCode);
            console.log("Code updated:", newCode);
        }
    }
};
</script>

<style scoped>
/* Các style cho MessageListAI */
.message-list-ai {
    margin-bottom: 15px;
    /* padding: 10px; */
    border-radius: 10px;
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

.message-text {
    margin-top: 10px;
    color: #f5f5f5;
}
</style>
