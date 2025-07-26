<script setup lang="ts">
const mode = ref("login");

const rAvatarId = ref("");
const rAvatarFileInput = ref<HTMLInputElement | null>(null);
function uploadAvatar() {
    rAvatarFileInput.value?.click();
}
function handleFileChange(evt: any) {
    const file = evt.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append("file", file);
        new API("/api/avatar").upload(formData).then((data: any) => {
            rAvatarId.value = data.avatar_id;
        });
    }
}
const rEmail = ref("");
const rPassword = ref("");
const rNickname = ref("");
const rMBTI = ref("INTJ");
const rBirthYear = ref("");
const rSex = ref("男");
function register() {
    const waiting: any = useUI().waiting();
    new API("/api/account").post({
        avatar_id: rAvatarId.value,
        email: rEmail.value,
        password: rPassword.value,
        nickname: rNickname.value,
        mbti: rMBTI.value,
        birthyear: rBirthYear.value,
        sex: rSex.value
    }).then((data: any) => {
        localStorage.setItem("account", JSON.stringify(data));
        useRouter().replace("/activities");
    }).catch(() => {
        useUI().alert("注册失败！");
    }).finally(() => {
        waiting.close();
    });
}

const lEmail = ref("");
const lPassword = ref("");
function login() {
    const waiting: any = useUI().waiting();
    new API("/api/account").get({
        email: lEmail.value,
        password: lPassword.value
    }).then((data: any) => {
        localStorage.setItem("account", JSON.stringify(data));
        useRouter().replace("/activities");
    }).catch(() => {
        useUI().alert("登录失败！");
    }).finally(() => {
        waiting.close();
    });
}
</script>

<template>
    <div class="login">
        <header>
            <img src="~/assets/img/PalUp.png">
            <div class="text">PalUp</div>
        </header>
        <div class="navBar">
            <div class="nav" :class="{ actived: mode == 'login' }" @click="mode = 'login'">登录</div>
            <div class="nav" :class="{ actived: mode == 'register' }" @click="mode = 'register'">注册</div>
        </div>
        <div v-if="mode == 'login'" class="module">
            <input v-model="lEmail" class="text-input" type="text" placeholder="邮箱">
            <input v-model="lPassword" class="text-input" type="text" placeholder="密码">
            <div class="button" @click="login">登录</div>
        </div>
        <div v-if="mode == 'register'" class="module">
            <div class="avatar" @click="uploadAvatar">
                <div v-if="!rAvatarId" class="text">上传头像</div>
                <img v-else :src="'/api/avatar?id=' + rAvatarId">
                <input ref="rAvatarFileInput" type="file" style="display: none;" @change="handleFileChange">
            </div>
            <input v-model="rEmail" class="text-input" type="text" placeholder="邮箱">
            <input v-model="rPassword" class="text-input" type="text" placeholder="密码">
            <input v-model="rNickname" class="text-input" type="text" placeholder="昵称">
            <div style="display: flex; width: 350px; margin: 0 auto; gap: 10px">
                <select v-model="rMBTI" class="text-input" style="flex: 1 1 0">
                    <option value="ESTJ">ESTJ</option>
                    <option value="ESFJ">ESFJ</option>
                    <option value="ESTP">ESTP</option>
                    <option value="ESFP">ESFP</option>
                    <option value="ISTJ">ISTJ</option>
                    <option value="ISFJ">ISFJ</option>
                    <option value="ISTP">ISTP</option>
                    <option value="ISFP">ISFP</option>
                    <option value="ENTJ">ENTJ</option>
                    <option value="ENFJ">ENFJ</option>
                    <option value="ENTP">ENTP</option>
                    <option value="ENFP">ENFP</option>
                    <option value="INTJ">INTJ</option>
                    <option value="INFJ">INFJ</option>
                    <option value="INTP">INTP</option>
                    <option value="INFP">INFP</option>
                </select>
                <select v-model="rSex" class="text-input" style="flex: 1 1 0">
                    <option value="男">男</option>
                    <option value="女">女</option>
                </select>
            </div>
            <input v-model="rBirthYear" class="text-input" style="flex: 1 1 0" type="number" placeholder="出生年份">
            <div class="button" @click="register">注册</div>
        </div>
    </div>
</template>

<style scoped>
.login {
    padding: 100px 0;

    >header {
        display: flex;
        align-items: center;
        justify-content: center;
        padding-bottom: 30px;

        >img {
            width: 60px;
            height: 60px;
        }

        >.text {
            font-weight: 600;
            font-size: 32px;
            margin-left: 15px;
        }
    }

    .navBar {
        width: fit-content;
        margin: 0 auto 20px auto;
        background-color: rgb(0 0 0 / .08);
        padding: 4px;
        border-radius: 8px;

        >.nav {
            display: inline-block;
            vertical-align: middle;
            font-size: 15px;
            padding: 5px 20px;
            border-radius: 6px;
            transition: background-color .2s;

            &:first-child {
                margin-right: 4px;
            }

            &:hover {
                background-color: rgb(0 0 0 / .06);
            }

            &.actived {
                background-color: #fff !important;
            }
        }
    }

    >.module {

        >.avatar {
            position: relative;
            width: 100px;
            height: 100px;
            margin: 0 auto;
            border-radius: 114514px;
            background-color: rgb(0 0 0 / .08);
            overflow: hidden;

            >.text {
                line-height: 100px;
                color: rgb(0 0 0 / .5);
                text-align: center;
            }

            >img {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
            }
        }

        >.text-input,
        >.button {
            margin: 12px auto;
            width: calc(100% - 40px);
            max-width: 320px;
        }
    }
}
</style>