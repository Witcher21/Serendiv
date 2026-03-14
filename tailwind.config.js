/** @type {import('tailwindcss').Config} */
import typography from '@tailwindcss/typography'

export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  darkMode: 'class', // High-fidelity dark mode
  theme: {
    extend: {
      colors: {
        'ceylon-dark': '#0b0f19',
        'ceylon-navy': '#111827',
        'ceylon-gold': '#d4a373',
        'ceylon-teal': '#2a9d8f',
        'ceylon-sand': '#fefae0',
        'premium-glass': 'rgba(255, 255, 255, 0.05)',
        'premium-border': 'rgba(255, 255, 255, 0.1)',
      },
      fontFamily: {
        display: ['"Playfair Display"', 'serif'],
        sans: ['"Inter"', 'sans-serif'],
        accent: ['"Space Grotesk"', 'sans-serif'],
      },
      backgroundImage: {
        'glass-gradient': 'linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.01) 100%)',
        'dark-radial': 'radial-gradient(circle at 50% 50%, #111827 0%, #0b0f19 100%)',
      },
      backdropBlur: {
        'premium': '20px',
      },
      animation: {
        'spin-slow': 'spin 12s linear infinite',
      }
    },
  },
  plugins: [
    typography,
    function({ addUtilities }) {
      addUtilities({
        '.glassmorphism': {
          'background': 'linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.01) 100%)',
          'backdrop-filter': 'blur(20px)',
          '-webkit-backdrop-filter': 'blur(20px)',
          'border': '1px solid rgba(255, 255, 255, 0.1)',
          'box-shadow': '0 8px 32px 0 rgba(0, 0, 0, 0.3)',
        },
        '.text-gradient': {
          'background': 'linear-gradient(to right, #d4a373, #2a9d8f)',
          '-webkit-background-clip': 'text',
          '-webkit-text-fill-color': 'transparent',
          'background-clip': 'text',
        }
      })
    }
  ],
}
