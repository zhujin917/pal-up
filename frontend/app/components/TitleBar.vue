<script setup lang="ts">
const props = defineProps<{
    title: string
}>();

function back() {
    const route = useRoute();
    if (route.path == "/suggestions") useRouter().replace("/my");
    else if (route.path == "/postTrip") useRouter().replace("/activities");
    else useRouter().back();
}
</script>

<template>
    <div class="titleBar">
        <div class="back" @click="back">&#xEA64;</div>
        <div class="title">{{ props.title }}</div>
    </div>
</template>

<style scoped>
.titleBar {
    position: relative;
    left: 0;
    top: 0;
    width: 100%;
    height: 60px;

    >.back {
        position: absolute;
        left: 10px;
        top: 50%;
        transform: translateY(-50%);
        font-family: "remixicon";
        font-size: 26px;
    }

    >.title {
        text-align: center;
        font-weight: bolder;
        font-size: 18px;
        line-height: 60px;
    }
}
</style>