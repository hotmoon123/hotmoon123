import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import { axe } from 'jest-axe';
import App from '../App';
import AnalyticsConsent from '../AnalyticsConsent';

afterEach(() => {
  cleanup();
  document.head.querySelectorAll('script[src*="googletagmanager.com"]').forEach((script) => script.remove());
  localStorage.clear();
  delete window.gtag;
  delete window.dataLayer;
  window.history.replaceState({}, '', '/');
});

beforeEach(() => {
  localStorage.clear();
  delete window.gtag;
  delete window.dataLayer;
  window.history.replaceState({}, '', '/');
});

describe('BiteKasa home page', () => {
  it('renders the advertised packs and enquiry actions', () => {
    render(<App />);

    expect(screen.getByRole('heading', { level: 1, name: /samosas\s*&\s*spring rolls/i })).toBeInTheDocument();
    expect(screen.getByText('GH₵100')).toBeInTheDocument();
    expect(screen.getByText('GH₵200')).toBeInTheDocument();
    expect(screen.getByText('GH₵250')).toBeInTheDocument();
    const whatsappLinks = screen.getAllByRole('link', { name: /order on whatsapp/i });
    expect(whatsappLinks.some((link) => link.getAttribute('href')?.includes('wa.me/233595638696'))).toBe(true);
    expect(document.querySelector('.pack-index')).not.toBeInTheDocument();
    expect(document.querySelector('.three-accent')).not.toBeInTheDocument();
  });

  it('links each preparation option to its dedicated page', () => {
    render(<App />);

    expect(screen.getByRole('link', { name: /learn more about fried options/i })).toHaveAttribute('href', '/services/fried/');
    expect(screen.getByRole('link', { name: /learn more about unfried options/i })).toHaveAttribute('href', '/services/unfried/');
    expect(screen.getByRole('link', { name: /learn more about frozen options/i })).toHaveAttribute('href', '/services/frozen/');
  });

  it('opens the mobile navigation and closes it with Escape', () => {
    render(<App />);
    const menuButton = screen.getByRole('button', { name: 'Open navigation' });

    fireEvent.click(menuButton);
    expect(screen.getByRole('button', { name: 'Close navigation' })).toHaveAttribute('aria-expanded', 'true');
    expect(screen.getByRole('navigation', { name: 'Mobile navigation' })).toBeInTheDocument();

    fireEvent.keyDown(window, { key: 'Escape' });
    expect(screen.getByRole('button', { name: 'Open navigation' })).toHaveAttribute('aria-expanded', 'false');
  });

  it('has no axe accessibility violations in the semantic home-page markup', async () => {
    const { container } = render(<App />);
    const results = await axe(container, { rules: { 'color-contrast': { enabled: false } } });

    expect(results.violations).toEqual([]);
  });
});

describe('dedicated service pages', () => {
  it('shows the selected product option and links to related options', () => {
    window.history.pushState({}, '', '/services/frozen/');
    render(<App />);

    expect(screen.getByRole('heading', { level: 1, name: /frozen samosas & spring rolls/i })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /^fried options$/i })).toHaveAttribute('href', '/services/fried/');
    expect(screen.getByRole('link', { name: /^unfried options$/i })).toHaveAttribute('href', '/services/unfried/');
    expect(screen.getByRole('link', { name: /view bitekasa packs/i })).toHaveAttribute('href', '/#packs');
  });
});

describe('analytics consent', () => {
  it('keeps analytics disabled until a visitor chooses to allow it', () => {
    render(<AnalyticsConsent />);

    expect(screen.getByRole('button', { name: 'Reject' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Allow analytics' })).toBeInTheDocument();
    expect(document.head.querySelector('script[src*="googletagmanager.com"]')).not.toBeInTheDocument();
  });

  it('stores a rejection without adding the Google tag', () => {
    render(<AnalyticsConsent />);
    fireEvent.click(screen.getByRole('button', { name: 'Reject' }));

    expect(localStorage.getItem('bitekasa-analytics-consent-v1')).toBe('rejected');
    expect(document.head.querySelector('script[src*="googletagmanager.com"]')).not.toBeInTheDocument();
  });

  it('loads the configured Google tag only after consent', () => {
    render(<AnalyticsConsent />);
    fireEvent.click(screen.getByRole('button', { name: 'Allow analytics' }));

    const tag = document.head.querySelector<HTMLScriptElement>('script[src*="googletagmanager.com"]');
    expect(localStorage.getItem('bitekasa-analytics-consent-v1')).toBe('accepted');
    expect(tag?.src).toContain('id=G-TEST000000');
  });
});
