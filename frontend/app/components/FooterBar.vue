<script setup lang="ts">
const route = useRoute();
const footerLinks = ref([
    {
        to: '/activities',
        icon: '\uED3B',
        filledIcon: '\uED3A',
        text: '活动',
    }, {
        to: '/my',
        icon: '\uF256',
        filledIcon: '\uF255',
        text: '我的',
    }
]);
</script>

<template>
    <footer>
        <div v-for="link of footerLinks" :key="link.to" class="link">
            <NuxtLink :to="link.to" :class="{ actived: link.to == route.path }">
                <div class="icon">{{ route.path == link.to ? link.filledIcon : link.icon }}</div>
                <div class="text">{{ link.text }}</div>
            </NuxtLink>
        </div>
        <div class="add">
            <NuxtLink to="/postTrip">&#xEA13;</NuxtLink>
        </div>
    </footer>
</template>

<style scoped>
footer {
    /* position: absolute; */
    width: 100%;
    height: 70px;
    left: 0;
    bottom: 0;
    background-color: white;
    border-top: 1px solid rgb(0 0 0 / .1);
    display: flex;
    align-items: center;

    >.link {
        flex: 1 1 0;
        height: 100%;
        text-align: center;

        &:first-child {
            order: 1;
        }

        &:not(:first-child) {
            order: 3;
        }

        >a {
            color: black;
            text-decoration: none;

            &.actived {
                color: var(--theme-color);
            }

            >.icon {
                font-family: 'remixicon';
                font-size: 26px;
                padding-top: 10px;
            }

            >.text {
                font-size: 13px;
                padding-top: 2px;
            }
        }
    }

    >.add {
        width: 36px;
        height: 36px;
        line-height: 36px;
        border-radius: 114514px;
        background-color: var(--theme-color);
        font-family: "remixicon";
        font-size: 26px;
        text-align: center;
        order: 2;

        >a {
            color: white;
            text-decoration: none;
        }
    }
}
</style>