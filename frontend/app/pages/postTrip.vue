<script setup lang="ts">
const future14days = getNextDay(14);
const activityId = ref("");

const dayBe = ref(future14days[0]?.beStr);
const text = ref("");
function postTrip() {
    const waiting: any = useUI().waiting();
    new API("/api/trip").post({
        activity_id: activityId.value,
        date: dayBe.value,
        text: text.value,
        is_public: false
    }).then((data: any) => {
        useRouter().replace({
            path: "/suggestions",
            query: { tripId: data.trip_id }
        });
    }).catch(() => {
        useUI().alert("匹配失败！");
    }).finally(() => {
        waiting.close();
    });
}

const as = ref<any>(null);
onMounted(() => {
    const id = useRoute().query.activityId;
    if (!id) return;
    new API("/api/activity/byid").get({ id }).then((data: any) => {
        as.value.setTargetActivity(data);
    });
});
</script>

<template>
    <div class="pageRoot" style="padding: 0 10px;">
        <TitleBar title="添加行程" />
        <UserProfileCard style="margin: 0 0 10px 0;" />
        <ActivitySelector ref="as" @activity-id="(id) => activityId = id" />
        <select v-model="dayBe" class="text-input">
            <option v-for="day of future14days" :key="day.timestamp" :value="day.beStr">{{ day.displayStr }}</option>
        </select>
        <textarea v-model="text" class="text-input" placeholder="自我介绍 / 对搭子的要求"></textarea>
        <div class="button" @click="postTrip">匹配搭子</div>
    </div>
</template>

<style scoped>
select {
    width: 100%;
    margin-bottom: 10px;
}

textarea {
    width: calc(100% - 30px);
    height: 150px;
    resize: none;
    margin-bottom: 10px;
}
</style>