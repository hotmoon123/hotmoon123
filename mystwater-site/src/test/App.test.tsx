import { fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { axe } from 'jest-axe';
import { describe, expect, it } from 'vitest';
import App from '../App';

describe('Myst Water concept site', () => {
  it('renders the hero headline and primary conversion paths', () => {
    render(<App />);
    expect(screen.getByRole('heading', { level: 1, name: /the feel good water/i })).toBeInTheDocument();
    // Wholesale-first CTA in header, hero and sticky bar.
    expect(screen.getAllByRole('link', { name: /become a stockist/i }).length).toBeGreaterThanOrEqual(2);
    // Retail path present too.
    expect(screen.getAllByRole('link', { name: /order on whatsapp/i }).length).toBeGreaterThanOrEqual(1);
  });

  it('shows both published phone numbers, labelled by source', () => {
    render(<App />);
    // The two public numbers appear in the contact section with their source labels.
    expect(screen.getAllByText('020 410 2171').length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText('+233 59 699 5220').length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/as listed on google maps/i).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/as listed on facebook/i).length).toBeGreaterThanOrEqual(1);
  });

  it('renders the real Google reviews verbatim', () => {
    render(<App />);
    expect(screen.getAllByText(/i got the delivery to my doorstep/i).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/myst water is the best/i).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/5\.0/).length).toBeGreaterThanOrEqual(1);
  });

  it('marks the concept honestly and links the privacy notice', () => {
    render(<App />);
    expect(screen.getAllByText(/website concept for myst water company/i).length).toBeGreaterThanOrEqual(1);
    expect(screen.getByRole('link', { name: /privacy/i })).toHaveAttribute('href', './privacy.html');
  });

  it('exposes the three bottle designs and the stockist form', () => {
    render(<App />);
    expect(screen.getAllByRole('heading', { name: /blue design/i }).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByRole('heading', { name: /clear design/i }).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByRole('heading', { name: /green design/i }).length).toBeGreaterThanOrEqual(1);
    const form = screen.getByRole('form', { name: /stockist enquiry form/i });
    expect(within(form).getByLabelText(/business name/i)).toBeRequired();
    expect(within(form).getByLabelText(/area/i)).toBeRequired();
    expect(within(form).getByLabelText(/whatsapp \/ phone/i)).toBeRequired();
  });

  it('reveals the website after the intro overlay is tapped', async () => {
    render(<App />);
    // Intro overlay is up on open; taps anywhere dismiss it.
    fireEvent.pointerDown(screen.getByRole('button', { name: /continue to the myst water website/i }));
    await waitFor(
      () => {
        expect(screen.queryByRole('button', { name: /continue to the myst water website/i })).not.toBeInTheDocument();
      },
      { timeout: 2500 },
    );
    expect(screen.getByRole('main')).toBeInTheDocument();
  });

  it('has no detectable accessibility violations', async () => {
    const { container } = render(<App />);
    // jsdom cannot host the Google Maps iframe — exclude frame analysis.
    const results = await axe(container, { iframes: false });
    expect(results.violations).toEqual([]);
  });
});
