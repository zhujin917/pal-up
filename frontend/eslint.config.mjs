// @ts-check
import withNuxt from './.nuxt/eslint.config.mjs'

export default withNuxt(
  // Your custom configs here
  {
    rules: {
      "@typescript-eslint/no-explicit-any": "off",
      "vue/html-self-closing": "off",
      "vue/first-attribute-linebreak": "off"
    }
  }
)
