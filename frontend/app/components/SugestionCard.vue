<script setup lang="ts">
const props = defineProps<{
    activity: any,
    userProfile: any,
    trip: any,
    text: string
}>();
</script>

<template>
    <div class="card suggestionCard">
        <UserProfileCard :user-profile="props.userProfile" style="margin: 0; box-shadow: none;" />
        <hr>
        <TripCard :trip="props.trip" :activity="props.activity" style="margin: 0; box-shadow: none;" />
        <hr>
        <!-- <div class="icon">&#xF36A;</div> -->
        <div class="text" @click="(e) => (e.target as HTMLElement).classList.toggle('show')">{{ props.text }}</div>
    </div>
</template>

<style scoped>
.suggestionCard {
    position: relative;
    border-radius: 10px;
    margin-bottom: 10px;
    overflow: hidden;

    >hr {
        margin: 0 24px;
        border: solid rgb(0 0 0 / .1);
        border-width: 1px 0 0 0;
    }

    >.text {
        margin: 20px 24px;

        &:not(.show) {
            height: 44px;
            line-clamp: 2;
            -webkit-line-clamp: 2;
            display: -webkit-box;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
    }

    >.icon {
        position: absolute;
        right: 25px;
        bottom: -15px;
        font-family: "remixicon";
        font-size: 64px;
        color: var(--theme-color);
        opacity: .1;
    }
}
</style>