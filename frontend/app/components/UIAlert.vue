<script setup lang="ts">
const props = defineProps<{
    id: string,
    text: string,
    title: string
}>();

const dialog = ref<any>(null);

onMounted(() => {
    setTimeout(() => {
        dialog.value?.showModal();
    }, 100);
});

function handleClose() {
    setTimeout(() => {
        document.getElementById(props.id)?.remove();
    }, 250);
}
</script>

<template>
    <UIDialog ref="dialog" width="300px" @close="handleClose">
        <div class="header">
            <div>{{ title }}</div>
            <small>{{ text }}</small>
        </div>
        <div class="buttons">
            <div class="button" @click="dialog.close()">好</div>
        </div>
    </UIDialog>
</template>

<style scoped>
.header {
    text-align: center;
    margin-bottom: 30px;

    >div {
        font-size: 20px;
        font-weight: 400;
        margin-bottom: 20px;
    }

    >small {
        font-size: 16px;
    }
}
</style>