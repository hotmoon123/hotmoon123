import { act, fireEvent, render, screen } from '@testing-library/react';
import { axe } from 'jest-axe';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import SplashScreen from '../components/SplashScreen';

describe('SplashScreen — intro on app open', () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it('shows the MYST logo immediately (no button needed) and auto-finishes', () => {
    const onDone = vi.fn();
    render(<SplashScreen onDone={onDone} />);

    expect(screen.getByRole('button', { name: /continue to the myst water website/i })).toBeInTheDocument();
    expect(screen.getByAltText('MYST Water logo')).toBeInTheDocument();
    expect(onDone).not.toHaveBeenCalled();

    act(() => {
      vi.advanceTimersByTime(2700 + 280 + 60);
    });
    expect(onDone).toHaveBeenCalledTimes(1);
  });

  it('reveals the website when the user taps anywhere on the screen', () => {
    const onDone = vi.fn();
    render(<SplashScreen onDone={onDone} />);

    fireEvent.pointerDown(screen.getByRole('button', { name: /continue to the myst water website/i }));
    act(() => {
      vi.advanceTimersByTime(400);
    });
    expect(onDone).toHaveBeenCalledTimes(1);
  });

  it('reveals the website on Escape (keyboard parity)', () => {
    const onDone = vi.fn();
    render(<SplashScreen onDone={onDone} />);

    fireEvent.keyDown(window, { key: 'Escape' });
    act(() => {
      vi.advanceTimersByTime(400);
    });
    expect(onDone).toHaveBeenCalledTimes(1);
  });

  it('has no detectable accessibility violations', async () => {
    vi.useRealTimers();
    const { container } = render(<SplashScreen onDone={() => undefined} />);
    const results = await axe(container, { iframes: false });
    expect(results.violations).toEqual([]);
  });
});
