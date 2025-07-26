<script setup lang="ts">
const future14days = getNextDay(14);
const city = ref<any>(localStorage.getItem("city"));

const dialog = ref<any>(null);
const activities = ref<Array<IActivity>>([]);
function fetchActivities() {
    new API("/api/activity").get({ city: city.value }).then((data: any) => {
        activities.value = data;
    });
}
onMounted(fetchActivities);
const searchKeyword = ref("");

const dialog2 = ref<any>(null);
const aTitle = ref("");
const aIntro = ref("");
const aBegin = ref(future14days[0]?.beStr);
const aEnd = ref(future14days[0]?.beStr);
function postActivity() {
    new API("/api/activity").post({
        title: aTitle.value,
        introduction: aIntro.value,
        city: city.value,
        begin_time: aBegin.value,
        end_time: aEnd.value
    }).finally(() => {
        fetchActivities();
        dialog2.value.open = false;
    });
}

const targetActivity = ref<IActivity | null>(null);
const emit = defineEmits<{
    (event: 'activityId', value: string): void
}>();
function setTargetActivity(a: IActivity) {
    targetActivity.value = a;
    dialog.value.open = false;
    emit("activityId", targetActivity.value.id);
}

defineExpose({ setTargetActivity });
</script>

<template>
    <div class="activitySelector">
        <div v-if="!targetActivity" class="empty" @click="dialog.open = true">添加活动</div>
        <ActivityCard v-else :activity="targetActivity" @click="dialog.open = true" />
        <UIDialog ref="dialog" height="calc(100% - 100px)" class="dialog">
            <header>
                <input v-model="searchKeyword" type="text" class="text-input" placeholder="搜索">
                <div @click="dialog2.open = true">&#xEA11;</div>
            </header>
            <div class="activities">
                <ActivityCard v-for="activity of activities" v-show="activity.title.includes(searchKeyword)"
                    :key="activity.id" :activity="activity" @click="setTargetActivity(activity)" />
            </div>
        </UIDialog>
        <UIDialog ref="dialog2" height="calc(60% - 100px)" class="dialog2">
            <div class="title">新活动</div>
            <input v-model="aTitle" type="text" class="text-input" placeholder="名称">
            <textarea v-model="aIntro" class="text-input" placeholder="简介"></textarea>
            <select v-model="aBegin" class="text-input">
                <option v-for="day of future14days" :key="day.timestamp" :value="day.beStr">
                    {{ day.displayStr }}
                </option>
            </select>
            <select v-model="aEnd" class="text-input">
                <option v-for="day of future14days" :key="day.timestamp" :value="day.beStr">
                    {{ day.displayStr }}
                </option>
            </select>
            <div class="button" @click="postActivity">确定</div>
        </UIDialog>
    </div>
</template>

<style scoped>
.activitySelector {
    >.empty {
        height: 90px;
        line-height: 90px;
        border-radius: 10px;
        text-align: center;
        background-color: rgb(0 0 0 / .08);
        margin-bottom: 10px;
        color: rgb(0 0 0 / .5);
    }

    >.dialog {
        header {
            display: flex;
            align-items: center;
            margin-bottom: 25px;

            .text-input {
                flex: 1 1 0;
            }

            div {
                font-family: "remixicon";
                font-size: 26px;
                color: var(--theme-color);
                margin: 0 6px 0 18px;
            }
        }

        .activities {
            flex: 1 1 0;
            overflow: auto;
        }
    }

    >.dialog2 {
        .title {
            font-size: 17px;
            text-align: center;
            margin-bottom: 20px;
        }

        .text-input {
            margin-bottom: 10px;
        }

        textarea {
            resize: none;
            height: 100px;
        }
    }
}
</style>