import { act, fireEvent, render, screen } from '@testing-library/react';
import { axe } from 'jest-axe';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import SplashScreen from '../components/SplashScreen';

const chimeSources: string[] = [];
const playMock = vi.fn(() => Promise.resolve());

class AudioStub {
  volume = 1;
  currentTime = 0;
  pause = vi.fn();
  play = playMock;

  constructor(public src: string) {
    chimeSources.push(src);
  }
}

describe('SplashScreen — intro on app open', () => {
  beforeEach(() => {
    vi.useFakeTimers();
    vi.stubGlobal('Audio', AudioStub as unknown as typeof Audio);
    playMock.mockClear();
    playMock.mockImplementation(() => Promise.resolve());
    chimeSources.length = 0;
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllGlobals();
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

  it('plays the water chime with the animation', () => {
    render(<SplashScreen onDone={() => undefined} />);
    expect(playMock).toHaveBeenCalledTimes(1);
    expect(chimeSources[0]).toContain('assets/audio/myst-splash.wav');
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

  it('stays functional when the browser blocks autoplay audio', () => {
    playMock.mockImplementationOnce(() => Promise.reject(new DOMException('denied', 'NotAllowedError')));
    const onDone = vi.fn();
    render(<SplashScreen onDone={onDone} />);

    fireEvent.pointerDown(screen.getByRole('button', { name: /continue to the myst water website/i }));
    act(() => {
      vi.advanceTimersByTime(400);
    });
    expect(onDone).toHaveBeenCalledTimes(1);
  });

  it('mutes on the M key without dismissing the intro', () => {
    const onDone = vi.fn();
    render(<SplashScreen onDone={onDone} />);

    fireEvent.keyDown(window, { key: 'm' });
    act(() => {
      vi.advanceTimersByTime(1200);
    });
    expect(onDone).not.toHaveBeenCalled();
    expect(screen.getByRole('button', { name: /continue to the myst water website/i })).toBeInTheDocument();
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
