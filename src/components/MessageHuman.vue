<template>

    <div class="message-list-human">
        <div class="message-item"></div>
        <div class="message-item message-item2">
            <div class="file_upload button_send" style="align-items: start; position: unset;" v-show="listFile.length > 0"
                >
                <div class="svg-wrapper" style="display: flex; margin-bottom: 8px;">
 
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" style="transform: none;"
                        xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M10 3v4a1 1 0 0 1-1 1H5m4 10v-2m3 2v-6m3 6v-3m4-11v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z" />
                    </svg>
                    <p style="color: white;">file upload</p>
                </div>

                <div v-for="(file, index) in listFile" :key="index">
                    <!-- Cắt tên file nếu quá dài và thêm dấu ba chấm -->
                    <span>{{ truncateFileName(file) }}</span>
                </div>
            </div>
            <div class="message-content">
                <p>{{ message }}</p>
            </div>

        </div>
    </div>

</template>

<script>
export default {
    props: ['message', 'listFile'],
    methods: {
        // Hàm cắt tên file nhưng vẫn giữ đuôi file
        truncateFileName(fileName, maxLength = 40) {
            const ext = fileName.slice(fileName.lastIndexOf('.'));  // Lấy phần đuôi file
            const name = fileName.slice(0, fileName.lastIndexOf('.')); // Lấy phần tên file (không có đuôi)

            // Nếu phần tên file dài quá, cắt lại và thêm dấu ba chấm, giữ đuôi file nguyên
            if (name.length > maxLength) {
                return name.substring(0, maxLength) + '...' + ext;
            }
            return fileName;  // Nếu tên file không dài thì giữ nguyên
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

.section_nav_bar_chat_window {
    display: flex;

}



.message-list-human {
    margin-bottom: 15px;
    display: flex;


}

.message-list-human .message-item2 {
    background-color: rgba(255, 0, 200, 0.1);
    border-radius: 20px;
    backdrop-filter: blur(30px);
    border-top-right-radius: 5px;

    padding: 15px;


}

.message-list-human .message-item {
    flex: 1;
}

.file_upload {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
    border-radius: 12px;
    backdrop-filter: blur(10px);
    border-top-right-radius: 5px;
    padding: 8px;
    border: 1px solid var(--border-color);


    border-radius: 15px;
    font-weight: 600;
    text-transform: uppercase;
    text-shadow: 0 0 10px var(--primary-cyan);
}
.file_upload svg{
    text-shadow: 0 0 10px var(--primary-cyan);
}
</style>