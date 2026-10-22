import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Static build only: no server-side code, no API proxy.
export default defineConfig({
  plugins: [react()],
  server: { host: '0.0.0.0', port: 5173, allowedHosts: true },
  build: { chunkSizeWarningLimit: 600 },
  preview: { host: '0.0.0.0', port: 4173, allowedHosts: true },
});
