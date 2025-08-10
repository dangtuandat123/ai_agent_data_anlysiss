<template>
    <div class="message-list-ai">
        <div class="message-item">
            <div class="message-content">
                <template v-if="message.iscode">
                    <!-- Hiển thị mã nguồn -->
                    <CodeComponentAI :code="localCode" @update:code="updateCode" />

                    <!-- Hiển thị hình ảnh -->
                    <ImageComponentAI v-if="message.type === 'img'" :imgBase64="message.img_base64" />

                    <!-- Hiển thị bảng HTML -->
                    <div v-if="message.type === 'table_html'" v-html="message.table_html" class="table-container"></div>
                    
                    <div class="button">
                        <!-- Nút xuất CSV -->
                        <button @click="exportToCSV" v-if="message.type === 'table_html'" class="button_export_csv">Xuất CSV</button>
                    </div>

                    <!-- Hiển thị message -->
                    <MessageComponentAI :message="message.message" />
                    <ButtonCopy @click="copyText" />

                </template>

                <template v-else>
                    <!-- Nếu không phải code, chỉ render message bình thường -->
                    <MessageComponentAI :message="message.message" />
                    <ButtonCopy @click="copyText" />
                </template>
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
        },

        // Phương thức xuất bảng thành CSV với định dạng UTF-8
        exportToCSV() {
            const table = this.$el.querySelector('.table-container table');
            if (!table) {
                alert('Không tìm thấy bảng!');
                return;
            }

            // Lấy tất cả các hàng trong bảng
            const rows = table.querySelectorAll('tr');
            let csv = [];
            rows.forEach(row => {
                const cells = row.querySelectorAll('th, td');
                let rowData = [];
                cells.forEach(cell => {
                    rowData.push('"' + cell.textContent.trim().replace(/"/g, '""') + '"'); // Đảm bảo không có dấu " trong dữ liệu
                });
                csv.push(rowData.join(','));
            });

            // Tạo tệp CSV từ dữ liệu bảng với mã hóa UTF-8
            const csvContent = '\uFEFF' + csv.join('\n'); // Thêm BOM để đảm bảo UTF-8
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);

            link.setAttribute('href', url);
            link.setAttribute('download', 'table_data.csv');
            link.click();

            URL.revokeObjectURL(url);
        }
    }
};
</script>

<style>
/* Kiểu dáng cho bảng */
.table-container table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0 0px 0px;
    font-family: 'Arial', sans-serif;
    background-color: #f9f9f9;
    border-radius: 20px;
    border: 0px;
    
}
.table-container{
    overflow: auto;
}
.table-container th,
.table-container td {
    border: 1px solid #ddd;
    padding: 12px 15px;
    text-align: left;
    border: 0px;
}

.table-container th {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    font-size: 16px;
}

.table-container tr:nth-child(even) {
    background-color: #cbc8c8;
}

.table-container th:hover {
    background-color: #3d8b3f;
}

.table-container td {
    font-size: 14px;
    color: #333;
}

.table-container th:first-child {
    border-top-left-radius: 20px;
}

.table-container th:last-child {
    border-top-right-radius: 20px;
}

.table-container th:first-child,
.table-container td:first-child {
    text-align: center;
}

.button_export_csv {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 5px 20px;
    border-radius: 0.4rem;
    cursor: pointer;
    font-size: 14px;
    margin-top: 10px;
}

.button_export_csv:hover {
    background-color: #218838;
}
</style>
