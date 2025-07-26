import * as Vue from "vue";

import Alert from "~/components/UIAlert.vue";
import Waiting from "~/components/UIWaiting.vue";

function createElement(id: string) {
    const elem = document.createElement("div");
    elem.id = id;
    document.body.appendChild(elem);
    return elem;
}

export default () => ({
    alert(text: string, title: string = "提示") {
        const id = "ui-alert";
        Vue.createApp(Alert, {
            id, text, title
        }).mount(createElement(id));
    },
    waiting() {
        const id = "ui-waiting";
        return Vue.createApp(Waiting, {
            id
        }).mount(createElement(id));
    }
})