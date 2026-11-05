import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    host: '0.0.0.0',
    allowedHosts: true,
  },
  build: {
    rollupOptions: {
      input: {
        main: new URL('./index.html', import.meta.url).pathname,
        fried: new URL('./services/fried/index.html', import.meta.url).pathname,
        unfried: new URL('./services/unfried/index.html', import.meta.url).pathname,
        frozen: new URL('./services/frozen/index.html', import.meta.url).pathname,
      },
    },
  },
});
