import { beforeEach, describe, expect, it, vi } from 'vitest';
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import App from '../App';

const scrollTo = vi.fn();

beforeEach(() => {
  scrollTo.mockReset();
  window.sessionStorage.setItem('bitekasa-intro-seen', '1');
  window.history.replaceState({}, '', '/');
  Object.defineProperty(window, 'scrollTo', { configurable: true, writable: true, value: scrollTo });
  Object.defineProperty(window, 'scrollY', { configurable: true, writable: true, value: 0 });
});

const clickNav = (name: RegExp) => fireEvent.click(screen.getByRole('link', { name }));

describe('in-page navigation', () => {
  it('scrolls to the packs section instead of reloading the page', async () => {
    render(<App />);

    clickNav(/^packs$/i);

    await waitFor(() => expect(scrollTo).toHaveBeenCalled());
    expect(window.location.hash).toBe('#packs');
  });

  it('reaches every section named in the navigation', async () => {
    render(<App />);

    for (const [label, hash] of [
      [/build an order/i, '#order'],
      [/questions/i, '#questions'],
      [/^contact$/i, '#contact'],
    ] as const) {
      clickNav(label);
      await waitFor(() => expect(window.location.hash).toBe(hash));
    }
  });

  it('takes the hero call to action to the order builder', async () => {
    render(<App />);

    fireEvent.click(screen.getAllByRole('link', { name: /build your order/i })[0]);

    await waitFor(() => expect(window.location.hash).toBe('#order'));
  });

  it('resolves a deep link that arrives with a hash', async () => {
    window.history.replaceState({}, '', '/#questions');
    render(<App />);

    await waitFor(() => expect(scrollTo).toHaveBeenCalled());
  });

  it('leaves external and WhatsApp links alone', () => {
    render(<App />);

    const whatsapp = screen.getAllByRole('link', { name: /whatsapp/i })[0];
    fireEvent.click(whatsapp);

    expect(scrollTo).not.toHaveBeenCalled();
  });
});
