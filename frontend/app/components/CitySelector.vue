<script setup lang="ts">
import cities from "~/assets/json/cities.json";

const emit = defineEmits<{
    (event: 'selected', value: string): void
}>();

const selectedProvince = ref("");

const dialog = ref<any>(null);
defineExpose({ dialog });
</script>

<template>
    <UIDialog ref="dialog" height="500px">
        <header>
            <div v-if="selectedProvince" class="province" @click="selectedProvince = ''">{{ selectedProvince }}</div>
            <div v-else class="province actived">请选择省份</div>
            <template v-if="selectedProvince">
                <div class="icon">&#xF496;</div>
                <div class="city actived">请选择城市</div>
            </template>
        </header>
        <main>
            <div v-if="!selectedProvince" class="provinces">
                <div v-for="province of Object.keys(cities)" :key="province" class="province"
                    @click="selectedProvince = province">
                    {{ province }}
                </div>
            </div>
            <div v-else class="cities">
                <div v-for="city of cities[selectedProvince as keyof typeof cities]" :key="city" class="city"
                    @click="emit('selected', city); dialog.open = false">
                    {{ city }}
                </div>
            </div>
        </main>
    </UIDialog>
</template>

<style scoped>
header {
    display: flex;
    align-items: center;
    margin-bottom: 10px;

    >.province,
    >.city {
        padding: 6px 12px;
        font-weight: bolder;
        border-radius: 114514px;
        background-color: rgb(0 0 0 / .05);

        &.actived {
            background-color: #E8F5FF;
            color: var(--theme-color);
        }
    }

    >.icon {
        font-family: "remixicon";
        font-size: 20px;
        margin: 0 6px;
    }
}

main {
    overflow: auto;

    .province,
    .city {
        padding: 6px 12px;
        margin: 3px 0;
    }
}
</style>