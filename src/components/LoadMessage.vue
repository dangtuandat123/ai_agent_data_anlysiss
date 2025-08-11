<template>
    <div class="loader"></div>

</template>

<script>

export default {

};
</script>

<style scoped>
:root {
    --primary-grey: #ffffff;
    --primary-orange: #f97316;
    --primary-purple: #ffbae5;
    --secondary-amber: #fbbf24;
    --dark-bg: #1a0b2e;
    --darker-bg: #0f051a;
    --card-bg: rgba(229, 231, 235, 0.03);
    --border-color: rgba(229, 231, 235, 0.2);
    --text-primary: #ffffff;
    --text-secondary: #a1a1aa;
    --primary-cyan: #00ffff;
    --primary-pink: #fbff88;
    --card-bg-btn: rgba(123, 23, 90, 0.254);
}

.loader {
    width: fit-content;
    font-weight: bold;
    font-size: 15PX;
    color: #0000;
    background: linear-gradient(90deg, #ffffff 25%, #83ffae 0 50%, #fdff6e 0 75%, #00eaff 0) 0 0/400% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    animation: l10 3s infinite cubic-bezier(0.3, 1, 0, 1);

    /* hiệu ứng xuất hiện & biến mất */
    opacity: 0;
    transform: scale(0.9);
    transition: opacity 1s ease, transform 1s ease;
    margin-bottom: 0px;
    padding: 10px;

    border: 1px solid var(--border-color);


    border-radius: 15px;
    font-weight: 600;
    text-transform: uppercase;
    text-shadow: 0 0 10px var(--primary-cyan);
}

.loader.show {
    opacity: 1;
    transform: scale(1);
    margin-bottom: 50px;
}

.loader:before {
    content: "Đang suy nghĩ...";
}

@keyframes l10 {
    25% {
        background-position: calc(1 * 100% / 3) 0;
    }

    50% {
        background-position: calc(2 * 100% / 3) 0;
    }

    75% {
        background-position: calc(3 * 100% / 3) 0;
    }

    100% {
        background-position: calc(4 * 100% / 3) 0;
    }
}
</style>