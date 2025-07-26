<script setup lang="ts">
const props = defineProps<{
    userProfile?: IUserProfile
}>();

const account = ref<any>(props.userProfile ?? JSON.parse(localStorage.getItem("account") ?? "{}"));
</script>

<template>
    <div class="card userProfileCard">
        <img class="avatar" :src="'/api/avatar?id=' + account.avatar_id">
        <main>
            <div class="nickname">{{ account.nickname }}</div>
            <span class="sex">
                <span class="key">性别</span>
                <span class="val">{{ account.sex }}</span>
            </span>
            <span class="mbti">
                <span class="key">MBTI</span>
                <span class="val">{{ account.mbti }}</span>
            </span>
            <span class="birthYear">
                <span class="key">年龄</span>
                <span class="val">{{ new Date().getFullYear() - account.birthyear }}</span>
            </span>
        </main>
        <!-- <div class="settings">&#xEC86;</div> -->
    </div>
</template>

<style scoped>
.userProfileCard {
    display: flex;
    align-items: center;
    padding: 20px 24px;
    margin: 10px;
    border-radius: 12px;
    background-color: rgb(255 255 255 / .4);

    >.avatar {
        width: 48px;
        height: 48px;
        border-radius: 114514px;
    }

    >main {
        flex: 1 1 0;
        margin-left: 12px;

        >.nickname {
            font-size: 24px;
            font-weight: bolder;
        }

        .key {
            font-size: 14px;
            opacity: .8;
        }

        .val {
            font-weight: 400;
            font-size: 17px;
            margin: 0 20px 0 4px;
        }
    }

    >.settings {
        font-size: 24px;
        font-family: "remixicon";
        margin-right: 6px;
    }
}
</style>