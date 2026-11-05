import { useEffect, useState } from 'react';
const SITE_BASE = import.meta.env.BASE_URL;
const MEASUREMENT_ID = import.meta.env.VITE_GA_MEASUREMENT_ID?.trim();
const CONSENT_KEY = 'bitekasa-analytics-consent-v1';

declare global {
  interface Window {
    dataLayer?: unknown[];
    gtag?: (...args: unknown[]) => void;
  }
}

function loadAnalytics() {
  if (!MEASUREMENT_ID || window.gtag) return;

  window.dataLayer = window.dataLayer ?? [];
  window.gtag = (...args: unknown[]) => window.dataLayer?.push(args);
  window.gtag('js', new Date());
  window.gtag('config', MEASUREMENT_ID, { send_page_view: true });

  const script = document.createElement('script');
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(MEASUREMENT_ID)}`;
  document.head.appendChild(script);
}

export default function AnalyticsConsent() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (!MEASUREMENT_ID) return;
    try {
      const choice = window.localStorage.getItem(CONSENT_KEY);
      if (choice === 'accepted') loadAnalytics();
      else if (choice !== 'rejected') setVisible(true);
    } catch {
      // Keep analytics disabled if browser storage is unavailable.
    }
  }, []);

  const choose = (accepted: boolean) => {
    try {
      window.localStorage.setItem(CONSENT_KEY, accepted ? 'accepted' : 'rejected');
    } catch {
      // A storage failure never enables analytics by itself.
    }
    setVisible(false);
    if (accepted) {
      loadAnalytics();
    } else if (window.gtag) {
      window.gtag('consent', 'update', { analytics_storage: 'denied', ad_storage: 'denied' });
      // A reload discards the already-loaded tag; the saved rejection prevents it loading again.
      window.location.reload();
    }
  };

  if (!MEASUREMENT_ID) return null;

  return (
    <>
      {visible ? (
        <aside className="analytics-consent" aria-label="Analytics preference" aria-live="polite">
          <p>
            BiteKasa can use Google Analytics to understand site visits. Analytics stays off unless you allow it.{' '}
            <a href={`${SITE_BASE}privacy.html`}>Privacy notice</a>
          </p>
          <div className="analytics-consent-actions">
            <button type="button" className="analytics-reject" onClick={() => choose(false)}>Reject</button>
            <button type="button" className="analytics-accept" onClick={() => choose(true)}>Allow analytics</button>
          </div>
        </aside>
      ) : (
        <button type="button" className="analytics-settings" onClick={() => setVisible(true)}>Privacy settings</button>
      )}
    </>
  );
}
