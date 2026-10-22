import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Static build only: no server code, no API routes.
// If you host under a sub-path (for example GitHub Pages project sites),
// change `base` to '/your-repo-name/'.
export default defineConfig({
  plugins: [react()],
  base: '/',
  build: {
    target: 'es2020',
    sourcemap: false,
    chunkSizeWarningLimit: 900,
  },
  server: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: true,
  },
  preview: {
    host: '0.0.0.0',
    port: 4173,
    allowedHosts: true,
  },
});
