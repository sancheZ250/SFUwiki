import { defineConfig } from 'vite';
import Vue from '@vitejs/plugin-vue';
// import { createProxyMiddleware } from 'http-proxy-middleware';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [Vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', //адрес бэкенда
        changeOrigin: true,
        // rewrite: path => path.replace(/^\/api/, ''),
      },
      '/auth':{
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    },
  },
});