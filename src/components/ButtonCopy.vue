<template>

    <button class="button">

        <span class="text">Copy</span>
        <img src="https://cdn-icons-png.flaticon.com/128/9428/9428873.png" style="height: 17px; width: 17px; position: relative; left: 0px;filter: brightness(0) invert(1);">

    </button>


</template>

<script>
export default {

};
</script>

<style scoped>
/* From Uiverse.io by simontheonlyone */
.button {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 25px;
    height: 25px;
    border: none;
    cursor: pointer;
    border-radius: 0.4em;
    background: rgba(235, 252, 254, 0.156);
}

.container {
    position: relative;
    width: 25px;
    height: 25px;
    background: none;
    overflow: hidden;
}



.active_line {
    content: "";
    position: absolute;
    bottom: 0;
    width: 0.9em;
    height: auto;
    background-color: #999;
    border: none;
    border-radius: 1em;
    transition: all 0.15s linear;
}

.button:active .active_line,
.button:focus .active_line {
    width: 2.3em;
    background-color: rgb(41, 126, 255);
}

.button:focus .container {
    animation: wow 1s forwards;
}

@keyframes wow {
    20% {
        scale: 0.8;
    }

    30% {
        scale: 1;
        transform: translateY(0);
    }

    50% {
        transform: translateY(-6px);
    }

    65% {
        transform: translateY(4px);
    }

    80% {
        transform: translateY(0);
    }

    100% {
        scale: 1;
    }
}

.text {
    content: "";
    position: absolute;
    top: -4.5em;
    width: auto;
    padding: 5px;
    height: 2.6em;
    background-color: #666;
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    border-radius: 5px;
    text-shadow: 0 0 10px rgb(0, 0, 0);
    opacity: 0;
    transition: all 0.25s linear;
}

/* .button:hover .text {
    opacity: 1;
} */
</style>