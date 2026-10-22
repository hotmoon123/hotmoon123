import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import { prefersReducedMotion } from './animations/motion';
import './styles/global.css';
import './styles/layout.css';
import './styles/animations.css';

// Scroll-reveal CSS only hides content when JavaScript is running and motion is allowed.
if (!prefersReducedMotion()) {
  document.documentElement.classList.add('js-motion');
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
