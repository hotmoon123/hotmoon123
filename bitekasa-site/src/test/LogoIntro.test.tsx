import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import LogoIntro from '../LogoIntro';

const STORAGE_KEY = 'bitekasa-intro-seen';

beforeEach(() => {
  window.sessionStorage.clear();
  window.history.replaceState({}, '', '/');
});

afterEach(() => {
  cleanup();
  window.sessionStorage.clear();
});

describe('LogoIntro', () => {
  it('opens as a labelled splash over the site', () => {
    render(<LogoIntro />);
    expect(screen.getByRole('dialog', { name: 'BiteKasa is opening' })).toBeInTheDocument();
  });

  it('offers a way out that is reachable by keyboard', () => {
    render(<LogoIntro />);
    expect(screen.getByRole('button', { name: 'Enter site' })).toBeInTheDocument();
  });

  it('remembers that the splash was dismissed for this session', () => {
    render(<LogoIntro />);
    fireEvent.click(screen.getByRole('button', { name: 'Enter site' }));
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
    expect(screen.getByRole('dialog', { name: 'BiteKasa is opening' })).toBeInTheDocument();
  });

  it('can be switched off entirely with ?intro=0', () => {
    window.history.replaceState({}, '', '/?intro=0');
    render(<LogoIntro />);
    expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
  });
});
