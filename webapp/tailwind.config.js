/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#6C5CE7',
        secondary: '#A29BFE',
        dark: '#1A1A2E',
        darker: '#16213E',
        accent: '#E94560',
      },
    },
  },
  plugins: [],
}
