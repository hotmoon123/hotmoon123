import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
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
      include: ['src/App.tsx', 'src/lib/**', 'src/content.ts'],
      reporter: ['text', 'json-summary', 'html'],
      thresholds: { statements: 70, branches: 50, functions: 70, lines: 75 },
    },
  },
});
