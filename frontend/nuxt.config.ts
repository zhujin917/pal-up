// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  // devtools: { enabled: true },
  devtools: { enabled: false },
  modules: ['@nuxt/eslint'],
  app: {
    rootAttrs: {
      id: "app"
    },
    head: {
      title: "PalUp 搭伴"
    }
  },
  css: [
    '@/assets/css/global.css'
  ],
  ssr: false,
  devServer: {
    host: "0.0.0.0"
  },
  nitro: {
    devProxy: {
      "/api": {
        target: "http://re-computer:8000/api",
        changeOrigin: true
      }
    }
  }
})