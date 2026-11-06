import { describe, expect, it } from 'vitest';
import { buildOrderMessage, normaliseQuantity, summariseOrder, whatsappHref, MAX_PER_PACK } from '../lib/order';

describe('order maths', () => {
  it('adds pack prices and piece counts', () => {
    const summary = summariseOrder({ golden: 2, silver: 1 });
    expect(summary.packCount).toBe(3);
    expect(summary.pieceCount).toBe(140);
    expect(summary.total).toBe(500);
    expect(summary.isEmpty).toBe(false);
  });

  it('is empty when nothing is chosen', () => {
    expect(summariseOrder({}).isEmpty).toBe(true);
    expect(summariseOrder({ golden: 0 }).isEmpty).toBe(true);
  });

  it('clamps quantities to whole numbers within the limit', () => {
    expect(normaliseQuantity(-3)).toBe(0);
    expect(normaliseQuantity(2.9)).toBe(2);
    expect(normaliseQuantity(MAX_PER_PACK + 5)).toBe(MAX_PER_PACK);
    expect(normaliseQuantity(Number.NaN)).toBe(0);
  });

  it('builds a WhatsApp message that states what the visitor chose', () => {
    const message = buildOrderMessage({ premium: 1, golden: 2 });

    expect(message).toContain('2 × GOLDEN');
    expect(message).toContain('1 × PREMIUM');
    expect(message).toContain('GH₵650');
    expect(message).toContain('3 packs');
    expect(message).toContain('180 pieces');
    expect(message).toContain('confirm availability');
  });

  it('falls back to a plain enquiry when the order is empty', () => {
    expect(buildOrderMessage({})).toContain('would like to ask about your packs');
  });

  it('encodes the message into a wa.me link', () => {
    const href = whatsappHref(buildOrderMessage({ silver: 1 }));
    expect(href.startsWith('https://wa.me/233595638696?text=')).toBe(true);
    expect(href).toContain(encodeURIComponent('1 × SILVER'));
  });
});
