import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { act, cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react';
import LogoIntro from '../LogoIntro';

const STORAGE_KEY = 'bitekasa-intro-seen';

beforeEach(() => {
  window.sessionStorage.clear();
  window.history.replaceState({}, '', '/');
});

afterEach(() => {
  cleanup();
  vi.useRealTimers();
  window.sessionStorage.clear();
});

describe('LogoIntro', () => {
  it('opens as a labelled splash over the site', () => {
    render(<LogoIntro />);
    expect(screen.getByRole('dialog')).toBeInTheDocument();
  });

  it('carries no button of its own — it plays and leaves', () => {
    render(<LogoIntro />);
    expect(screen.queryByRole('button')).not.toBeInTheDocument();
  });

  it('leaves on its own after the reveal and remembers that for the session', () => {
    vi.useFakeTimers();
    render(<LogoIntro />);

    act(() => {
      vi.advanceTimersByTime(4000);
    });

    expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
    expect(window.sessionStorage.getItem(STORAGE_KEY)).toBe('1');
  });

  it('does not replay the splash on a later page view', () => {
    window.sessionStorage.setItem(STORAGE_KEY, '1');
    render(<LogoIntro />);
    expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
  });

  it('replays on demand with ?intro=1', () => {
    window.sessionStorage.setItem(STORAGE_KEY, '1');
    window.history.replaceState({}, '', '/?intro=1');
    render(<LogoIntro />);
    expect(screen.getByRole('dialog')).toBeInTheDocument();
  });

  it('can be switched off entirely with ?intro=0', () => {
    window.history.replaceState({}, '', '/?intro=0');
    render(<LogoIntro />);
    expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
  });
});

describe('LogoIntro dismissal paths', () => {
  beforeEach(() => {
    window.sessionStorage.clear();
    window.history.replaceState({}, '', '/');
  });

  it('opens the site as soon as the visitor taps the splash', async () => {
    render(<LogoIntro />);
    const splash = screen.getByRole('dialog');

    fireEvent.pointerDown(splash);

    expect(splash).toHaveClass('is-leaving');
    await waitFor(() => expect(screen.queryByRole('dialog')).not.toBeInTheDocument());
  });

  it('opens the site on a click too, for mouse and trackpad users', async () => {
    render(<LogoIntro />);
    const splash = screen.getByRole('dialog');

    fireEvent.click(splash);

    expect(splash).toHaveClass('is-leaving');
    await waitFor(() => expect(screen.queryByRole('dialog')).not.toBeInTheDocument());
  });

  it('opens the site on Enter for keyboard users', async () => {
    render(<LogoIntro />);
    fireEvent.keyDown(window, { key: 'Enter' });
    await waitFor(() => expect(screen.queryByRole('dialog')).not.toBeInTheDocument());
  });

  it('ignores scrolling, so the page underneath is not disturbed', () => {
    render(<LogoIntro />);
    const splash = screen.getByRole('dialog');

    fireEvent.wheel(splash);
    fireEvent.touchStart(splash);

    expect(splash).not.toHaveClass('is-leaving');
  });

  it('still closes on Escape for keyboard users', async () => {
    render(<LogoIntro />);
    fireEvent.keyDown(window, { key: 'Escape' });
    await waitFor(() => expect(screen.queryByRole('dialog')).not.toBeInTheDocument());
  });
});
