import { describe, expect, it } from 'vitest';
import { fireEvent, render, screen } from '@testing-library/react';
import OrderBuilder from '../site/OrderBuilder';

const addGolden = () => fireEvent.click(screen.getByRole('button', { name: /add one golden pack/i }));
const addSilver = () => fireEvent.click(screen.getByRole('button', { name: /add one silver pack/i }));

describe('OrderBuilder', () => {
  it('cannot send an empty order', () => {
    render(<OrderBuilder />);
    expect(screen.getByRole('button', { name: /send order on whatsapp/i })).toBeDisabled();
    expect(screen.getByText(/add a pack above/i)).toBeInTheDocument();
  });

  it('totals the packs, pieces and cedi amount as they are added', () => {
    render(<OrderBuilder />);

    addGolden();
    addGolden();
    addSilver();

    expect(screen.getByText('GH₵500')).toBeInTheDocument();
    expect(screen.getByText('3 packs · 140 pieces')).toBeInTheDocument();
  });

  it('sends a WhatsApp link carrying the chosen packs', () => {
    render(<OrderBuilder />);
    addGolden();

    const send = screen.getByRole('link', { name: /send order on whatsapp/i });
    const href = send.getAttribute('href') ?? '';
    expect(href.startsWith('https://wa.me/233595638696?text=')).toBe(true);
    expect(decodeURIComponent(href)).toContain('1 × GOLDEN');
  });

  it('removes a pack again and can clear the whole order', () => {
    render(<OrderBuilder />);
    addGolden();
    fireEvent.click(screen.getByRole('button', { name: /remove one golden pack/i }));

    expect(screen.getByText(/add a pack above/i)).toBeInTheDocument();

    addGolden();
    fireEvent.click(screen.getByRole('button', { name: /^clear$/i }));
    expect(screen.getByText(/add a pack above/i)).toBeInTheDocument();
  });

  it('previews the exact message before it is sent', () => {
    render(<OrderBuilder />);
    addSilver();

    fireEvent.click(screen.getByText(/preview the message/i));
    expect(screen.getByText(/would like to order/i)).toBeInTheDocument();
  });
});
