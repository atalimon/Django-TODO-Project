/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../posts/**/*.html',
    '../profiles/**/*.html',
    '../templates/posts/*.html',
    '../templates/profiles/*.html',
    "../templates/**/*html",
    '../**/forms.py'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  
}

