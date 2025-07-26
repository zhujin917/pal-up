<script setup lang="ts">
onMounted(() => {
    useRouter().replace(localStorage.getItem("account") ? "/activities" : "/login");
});
</script>

<template>
    <div class="loading">
        <img class="icon" src="@/assets/img/PalUp.png">
        <LoaderPattern class="loader" color="#0292FE" />
    </div>
</template>

<style scoped>
div.loading {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    z-index: 114514;

    >.icon {
        width: 100px;
        height: 100px;
        margin-bottom: 100px;
    }

    >.loader {
        width: 30px;
        height: 30px;
    }
}
</style>