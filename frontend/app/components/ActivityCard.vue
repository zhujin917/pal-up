<script setup lang="ts">
defineProps<{
    activity: IActivity
}>();

function getDayStr(str: string) {
    const date = new Date(str);
    return `${date.getMonth() + 1}月${date.getDate()}日`;
}
</script>

<template>
    <div class="card activity">
        <div class="name">{{ activity.title }}</div>
        <div class="introduction">{{ activity.introduction }}</div>
        <div class="bottom">
            <div v-if="activity.begin_time == activity.end_time" class="date">{{ getDayStr(activity.begin_time) }}</div>
            <div v-else class="date">{{ getDayStr(activity.begin_time) + "-" + getDayStr(activity.end_time) }}</div>
            <!-- <div class="peopleNum">{{ 0 }} 人想去</div> -->
        </div>
        <div class="icon">&#xED3B;</div>
    </div>
</template>

<style scoped>
.activity {
    position: relative;
    margin: 5px 5px 10px 5px;
    padding: 18px 20px;
    border-radius: 12px;
    overflow: hidden;

    >.name {
        font-size: 18px;
        font-weight: bolder;
    }

    >.introduction {
        font-size: 16px;
        line-height: 22px;
        max-height: 44px;
        line-clamp: 2;
        -webkit-line-clamp: 2;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        margin: 10px 0;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    >.bottom {
        display: flex;
        flex-direction: row;
        font-size: 14px;
        color: rgb(0 0 0 / 0.6);

        >.date {
            flex: 1 1 0;
        }
    }

    >.icon {
        position: absolute;
        bottom: -10px;
        right: 15px;
        font-family: "remixicon";
        font-size: 64px;
        color: var(--theme-color);
        opacity: .1;
    }
}
</style>