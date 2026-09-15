export default [
  {
    files: ["**/*.mjs"],
    languageOptions: {
      ecmaVersion: 2024,
      sourceType: "module",
      globals: { console: "readonly", process: "readonly", URL: "readonly", URLSearchParams: "readonly", fetch: "readonly", setTimeout: "readonly", clearTimeout: "readonly", setInterval: "readonly", clearInterval: "readonly", Buffer: "readonly", structuredClone: "readonly", AbortController: "readonly", TextEncoder: "readonly", TextDecoder: "readonly", document: "readonly", window: "readonly", getComputedStyle: "readonly", NodeFilter: "readonly", Range: "readonly", Image: "readonly", performance: "readonly", crypto: "readonly", __dirname: "readonly", require: "readonly", module: "readonly" },
    },
    rules: { "no-undef": "error" },
  },
];
