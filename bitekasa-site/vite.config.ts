import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    host: '0.0.0.0',
    allowedHosts: ['.e2b.app'],
  },
  preview: {
    host: '0.0.0.0',
    allowedHosts: ['.e2b.app'],
  },
  test: {
    environment: 'jsdom',
    setupFiles: './src/test/setup.ts',
    restoreMocks: true,
    clearMocks: true,
    coverage: {
      provider: 'v8',
      include: ['src/App.tsx', 'src/AnalyticsConsent.tsx'],
      reporter: ['text', 'json-summary', 'html'],
      thresholds: { statements: 80, branches: 50, functions: 75, lines: 85 },
    },
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
