import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import ErrorBoundary from '../components/ErrorBoundary';

function Thrower(): never {
  throw new Error('boom');
}

describe('ErrorBoundary', () => {
  it('renders children when nothing throws', () => {
    render(
      <ErrorBoundary>
        <p>safe content</p>
      </ErrorBoundary>,
    );
    expect(screen.getByText('safe content')).toBeInTheDocument();
  });

  it('shows a plain, blame-free fallback with a call link and a reload button', () => {
    vi.spyOn(console, 'error').mockImplementation(() => {});
    render(
      <ErrorBoundary>
        <Thrower />
      </ErrorBoundary>,
    );
    expect(screen.getByRole('alert')).toBeInTheDocument();
    expect(screen.getByText(/something went wrong on our side/i)).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /call myst/i })).toHaveAttribute('href', 'tel:+233204102171');
    expect(screen.getByRole('button', { name: /reload page/i })).toBeInTheDocument();
  });
});
