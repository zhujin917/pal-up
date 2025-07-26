<script setup lang="ts">
const props = defineProps<{
    type?: string,
    height?: string
}>();
const emit = defineEmits<{
    (event: 'close'): void
}>();

const open = ref(false);

function showModal() {
    open.value = true;
}
function close() {
    open.value = false;
}
function handleBackdropClick() {
    if (props.type != "waiting") close();
}

watch(open, (val) => {
    if (!val) emit("close");
});

defineExpose({ open, showModal, close });
</script>

<template>
    <div class="ui-dialog" :class="{ open }">
        <div class="backdrop" @click="handleBackdropClick"></div>
        <div :class="props.type ?? 'dialog'" :style="{ height }">
            <slot></slot>
        </div>
    </div>
</template>

<style scoped>
.ui-dialog {
    position: fixed;
    width: 100vw;
    height: 100vh;
    left: 0;
    top: 0;
    z-index: 100;
    pointer-events: none;
    opacity: 0;
    transition: opacity .2s;

    >.backdrop {
        position: absolute;
        width: 100%;
        height: 100%;
        background-color: rgb(0 0 0 / .2);
    }

    >.dialog {
        position: absolute;
        left: 50%;
        bottom: 0;
        width: calc(var(--max-width) - 42px);
        transform: translate(-50%, 100px);
        padding: 20px;
        height: fit-content;
        border-radius: 20px 20px 0 0;
        border: 1px solid rgb(0 0 0 / .05);
        background-color: #fff;
        overflow: hidden;
        box-shadow: 0 10px 30px rgb(0 0 0 / .25);
        transition: transform .2s;
        display: flex;
        flex-direction: column;
    }

    >.waiting {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        padding: 22px;
        width: 30px;
        height: 30px;
        border-radius: 10px;
        border: 1px solid rgb(0 0 0 / .05);
        background-color: #fff;
        box-shadow: 0 10px 30px rgb(0 0 0 / .25);
    }

    &.open {
        opacity: 1;
        pointer-events: all;

        >.dialog {
            transform: translate(-50%, 0);
        }
    }
}
</style>