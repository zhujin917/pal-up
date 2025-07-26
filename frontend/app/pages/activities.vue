<script setup lang="ts">
import "~/assets/css/home.css";

const searchKeyword = ref("");
const future14days = getNextDay(14);
const targetDayTs = ref(-1);

if (!localStorage.getItem("city")) localStorage.setItem("city", "杭州市");
const city = ref(localStorage.getItem("city"));
const citySelector = ref<any>(null);

const activities = ref<Array<IActivity>>([]);
function fetchActivities() {
    new API("/api/activity").get({ city: city.value }).then((data: any) => {
        activities.value = data;
    });
}
onMounted(fetchActivities);
watch(city, () => {
    localStorage.setItem("city", city.value ?? "");
    fetchActivities();
});

function toPostTrips(activityId: any) {
    useRouter().push({
        path: "/postTrip",
        query: { activityId }
    });
}
</script>

<template>
    <div class="homeRoot">
        <header>
            <div class="city" @click="citySelector.dialog.open = true">
                <div class="icon">&#xEF14;</div>
                <div class="text">{{ city }}</div>
                <div class="arrow">&#xEA4E;</div>
            </div>
            <div class="card search">
                <div class="icon">&#xF0D1;</div>
                <input v-model="searchKeyword" type="text" placeholder="搜索活动">
            </div>
        </header>
        <div class="days">
            <div class="card day" :class="{ actived: targetDayTs < 0 }" @click="targetDayTs = -1">
                <div class="text">全部</div>
            </div>
            <div v-for="day of future14days" :key="day.timestamp" class="card day"
                :class="{ actived: targetDayTs == day.timestamp }" @click="targetDayTs = day.timestamp">
                <div class="month">{{ day.month }}</div>
                <div class="date">{{ day.date }}</div>
                <div class="day">{{ day.day }}</div>
            </div>
        </div>
        <div class="activities">
            <ActivityCard v-for="activity of activities"
                v-show="(targetDayTs == -1 || (new Date(activity.begin_time).getTime() <= targetDayTs && (new Date(activity.end_time).getTime() + 86400000) >= targetDayTs)) && activity.title.includes(searchKeyword)"
                :key="activity.id" :activity="activity" @click="toPostTrips(activity.id)" />
        </div>
        <FooterBar />
        <CitySelector ref="citySelector" @selected="(c) => city = c" />
    </div>
</template>

<style scoped>
header {
    display: flex;
    align-items: center;
    padding: 12px 0 6px 0;

    >.city {
        display: flex;
        align-items: center;
        padding: 8px 10px;
        margin: 0 6px 0 10px;

        >.icon {
            font-family: "remixicon";
            font-size: 20px;
        }

        >.text {
            font-size: 16px;
            margin: 0 1px 0 2px;
        }

        >.arrow {
            font-family: "remixicon";
        }
    }

    >.search {
        height: 36px;
        padding: 0 12px;
        flex: 1 1 0;
        display: flex;
        gap: 4px;
        align-items: center;
        border-radius: 114514px;
        margin-right: 20px;

        >.icon {
            font-family: "remixicon";
            font-size: 18px;
        }

        >input[type=text] {
            background-color: transparent;
            border: none;
            outline: none;
            flex: 1 1 0;
            font-size: 14px;
        }
    }
}

.days {
    overflow-x: scroll;
    white-space: nowrap;
    padding: 6px 4px;

    >.day {
        display: inline-flex;
        flex-direction: column;
        justify-content: center;
        vertical-align: middle;
        width: 64px;
        height: 64px;
        text-align: center;
        margin-right: 6px;
        border-radius: 8px;

        &:first-child {
            margin-left: 6px;
        }

        &.actived {
            background-color: var(--theme-color);
            color: white;
        }

        >.month,
        >.day {
            font-size: 12px;
            opacity: .8;
        }

        >.date,
        >.text {
            font-weight: bolder;
        }

        >.date {
            font-size: 20px;
        }

        >.text {
            font-size: 17px;
        }
    }
}

.activities {
    flex: 1 1 0;
    padding: 6px 10px 0 10px;
    overflow-y: auto;
}
</style>