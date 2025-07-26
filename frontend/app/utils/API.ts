export default class API {
    private url;
    constructor(url: string) {
        this.url = url;
    }

    private fetch(url: string, opt: any) {
        return $fetch(url, Object.assign({
            onResponse({ response }: any) {
                if (response.status == 403) {
                    useRouter().replace("/login");
                    throw new Error("not login");
                }
            }
        }, opt));
    }

    async get(data: unknown = {}) {
        let params = '';
        for (const [key, value] of Object.entries(data as object)) {
            params += params ? '&' : '?';
            params += `${key}=${encodeURIComponent(value)}`;
        }
        return await this.fetch(this.url + params, {
            method: "GET"
        });
    }

    async post(data: unknown = {}) {
        // let body = '';
        // for (const [key, value] of Object.entries(data as object)) {
        //   if (body) body += '&';
        //   body += `${key}=${encodeURIComponent(value)}`;
        // }
        return await this.fetch(this.url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });
    }

    async upload(body: FormData) {
        return await this.fetch(this.url, {
            method: "POST",
            body
        });
    }

    async delete(data: unknown = {}) {
        let params = '';
        for (const [key, value] of Object.entries(data as object)) {
            params += params ? '&' : '?';
            params += `${key}=${encodeURIComponent(value)}`;
        }
        return await this.fetch(this.url + params, {
            method: "DELETE"
        });
    }
}