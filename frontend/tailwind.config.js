/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          bg: "#fdfaf6",      // off-white background
          brown: "#3e2723",   // primary text / headings
          green: "#4a6741",   // accent (links, buttons)
          terra: "#b85c38",   // secondary accent
          card: "#ffffff",    // card bg
        },
      },
      fontFamily: {
        heading: ["Georgia", "Times New Roman", "serif"], // titles
        body: [
          "system-ui",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "sans-serif",
        ], // body
      },
      boxShadow: {
        soft: "0 6px 24px rgba(0,0,0,0.08)",
      },
      borderRadius: {
        card: "1rem",
      },
    },
  },
  plugins: [],
};
