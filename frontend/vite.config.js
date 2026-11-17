import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// The dev server forwards every /api request to the Flask backend,
// so the browser sees one origin and login cookies just work.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': { target: 'http://127.0.0.1:5000', changeOrigin: true },
    },
  },
});
