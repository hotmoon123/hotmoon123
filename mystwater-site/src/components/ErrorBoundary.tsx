import { Component, type ReactNode } from 'react';
import { Phone, RotateCcw } from 'lucide-react';
import { SITE } from '../content';
import { telLink } from '../lib/whatsapp';

interface Props {
  children: ReactNode;
}

interface State {
  failed: boolean;
}

/**
 * Root error boundary. If a section throws during render we keep the shell
 * (header/footer) alive and give the visitor a plain, blame-free way out:
 * reload, or call MYST directly. No error text, no stack, no exclamation.
 */
export default class ErrorBoundary extends Component<Props, State> {
  state: State = { failed: false };

  static getDerivedStateFromError(): State {
    return { failed: true };
  }

  componentDidCatch(error: unknown): void {
    // Report nowhere (no trackers); log locally so preview sessions can see it.
    console.error('[myst] render failed:', error);
  }

  render() {
    if (!this.state.failed) return this.props.children;

    return (
      <div className="wrap error-boundary" role="alert">
        <h2 className="error-boundary-title">Something went wrong on our side.</h2>
        <p className="error-boundary-copy">
          The page hit an unexpected error. Reloading usually fixes it — or reach the
          team directly, we answer the phone.
        </p>
        <div className="error-boundary-actions">
          <a className="btn btn--navy btn--sm" href={telLink(SITE.phoneMapsDisplay)}>
            <Phone size={16} aria-hidden="true" /> Call MYST · {SITE.phoneMapsDisplay}
          </a>
          <button type="button" className="btn btn--outline btn--sm" onClick={() => window.location.reload()}>
            <RotateCcw size={16} aria-hidden="true" /> Reload page
          </button>
        </div>
      </div>
    );
  }
}
