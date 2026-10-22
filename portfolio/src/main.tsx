import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { prefersReducedMotion } from './animations/motion';
import './styles/tokens.css';
import './styles/global.css';
import './styles/responsive.css';

// Scroll-reveal styles only hide content when JavaScript runs and motion is allowed.
if (!prefersReducedMotion()) {
  document.documentElement.classList.add('js-motion');
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
