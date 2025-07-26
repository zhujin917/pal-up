<script setup lang="ts">
const props = defineProps<{
    trip: any,
    activity?: any
}>();
</script>

<template>
    <div class="card tripCard">
        <header>
            <span v-if="props.trip.is_public" class="is_public true">公开</span>
            <span v-else class="is_public false">私有</span>
            <span class="activityTitle">{{ props.activity?.title ?? props.trip?.activity?.title }}</span>
            <span class="time">{{ props.trip.time }}</span>
        </header>
        <div class="text" :class="{ noHide: props.activity }">{{ props.trip.text }}</div>
        <div class="icon">&#xEBAD;</div>
    </div>
</template>

<style scoped>
.tripCard {
    position: relative;
    margin: 0 10px 10px 10px;
    padding: 20px 24px;
    border-radius: 10px;
    overflow: hidden;

    >header {
        display: flex;
        align-items: center;

        >.is_public {
            font-size: 13px;
            margin-right: 6px;
            padding: 2px 6px;
            border-radius: 3px;
            color: white;

            &.true {
                background-color: green;
            }

            &.false {
                background-color: #606060;
            }
        }

        >.activityTitle {
            font-size: 18px;
            font-weight: 400;
            flex: 1 1 0;
        }

        >.time {
            font-size: 15px;
            opacity: .8;
        }
    }

    >.text {
        margin-top: 10px;

        &:not(.noHide) {
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
        bottom: -15px;
        right: 20px;
        font-family: "remixicon";
        font-size: 64px;
        color: var(--theme-color);
        opacity: .1;
    }
}
</style>