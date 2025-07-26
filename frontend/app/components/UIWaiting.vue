<script setup lang="ts">
const props = defineProps<{
    id: string
}>();

const dialog = ref<any>(null);

onMounted(() => {
    setTimeout(() => {
        dialog.value?.showModal();
    }, 100);
});

function close() {
    return new Promise<void>((resolve) => {
        dialog.value?.close();
        setTimeout(() => {
            document.getElementById(props.id)?.remove();
            resolve();
        }, 250);
    });
}

defineExpose({ close });
</script>

<template>
    <UIDialog ref="dialog" type="waiting">
        <LoaderPattern width="30" height="30" color="var(--theme-color)" style="position: absolute" />
    </UIDialog>
</template>

<style>
div#ui-waiting div.dialog {
    line-height: 0;
    padding: 22px;
}
</style>