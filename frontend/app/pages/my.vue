<script setup lang="ts">
import "~/assets/css/home.css";

const myTrips = ref<Array<any>>([]);
function fetchMyTrips() {
    new API("/api/user/trips").get().then((data: any) => {
        myTrips.value = data;
    })
}
onMounted(fetchMyTrips);

function toSuggestions(tripId: number) {
    useRouter().push({
        path: "/suggestions",
        query: { tripId }
    });
}
</script>

<template>
    <div class="homeRoot">
        <UserProfileCard />
        <div style="flex: 1 1 0; overflow: auto;">
            <TripCard v-for="trip of myTrips" :key="trip.id" :trip="trip" @click="toSuggestions(trip.id)" />
        </div>
        <FooterBar />
    </div>
</template>

<style scoped></style>