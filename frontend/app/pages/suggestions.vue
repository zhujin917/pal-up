<script setup lang="ts">
const suggestions = ref<any>([]);
const isPublic = ref(true);

onMounted(() => {
    const waiting: any = useUI().waiting();
    Promise.all([
        new API("/api/suggestions").get({
            trip_id: useRoute().query.tripId
        }).then((data: any) => {
            suggestions.value = data;
        }), new API("/api/trip/is_public").get({
            trip_id: useRoute().query.tripId
        }).then((data: any) => {
            isPublic.value = data;
        })
    ]).then(() => {
        waiting.close();
    });
});

function exposeTrip() {
    const waiting: any = useUI().waiting();
    new API("/api/trip/is_public").post({
        trip_id: useRoute().query.tripId,
        is_public: true
    }).finally(() => {
        waiting.close();
        useRouter().replace("/my");
    });
}

function delTrip() {
    const waiting: any = useUI().waiting();
    new API("/api/trip").delete({
        trip_id: useRoute().query.tripId
    }).finally(() => {
        waiting.close();
        useRouter().replace("/my");
    });
}
</script>

<template>
    <div class="suggestions">
        <TitleBar title="匹配建议" />
        <div class="del" @click="delTrip">删除行程</div>
        <main>
            <SugestionCard v-for="(suggestion, i) of suggestions" :key="i" :activity="suggestion.activity"
                :trip="suggestion.trip" :text="suggestion.suggestion" :user-profile="suggestion.user" />
            <div v-if="suggestions.length == 0" class="empty">空</div>
            <div v-if="!isPublic" class="button" @click="exposeTrip">没找到合适的搭子，公布我的行程</div>
        </main>
    </div>
</template>

<style scoped>
.suggestions {
    display: flex;
    flex-direction: column;
    padding: 0 10px;
    height: 100%;

    >.del {
        position: absolute;
        right: 30px;
        top: 0;
        line-height: 60px;
        color: brown;
        font-size: 16px;
        font-weight: 400;
    }

    >main {
        overflow: auto;
        flex: 1 1 0;

        >.button {
            margin-bottom: 15px;
        }

        >.empty {
            text-align: center;
            margin: 20px 0 60px 0;
        }
    }
}
</style>