import { PACKS, WHATSAPP_NUMBER, cedi, packContents, type PackId } from '../data/catalogue';

export type OrderSelection = Partial<Record<PackId, number>>;

export type OrderLine = { id: PackId; quantity: number; name: string; line: string; total: number };

export type OrderSummary = {
  lines: OrderLine[];
  packCount: number;
  pieceCount: number;
  total: number;
  isEmpty: boolean;
};

export const MAX_PER_PACK = 20;

/** Clamp whatever a visitor typed or tapped into a sane whole number. */
export const normaliseQuantity = (value: number) => {
  if (!Number.isFinite(value)) return 0;
  return Math.min(MAX_PER_PACK, Math.max(0, Math.trunc(value)));
};

export function summariseOrder(selection: OrderSelection): OrderSummary {
  const lines: OrderLine[] = PACKS.flatMap((pack) => {
    const quantity = normaliseQuantity(selection[pack.id] ?? 0);
    if (quantity === 0) return [];
    return [
      {
        id: pack.id,
        quantity,
        name: pack.name,
        line: packContents(pack),
        total: pack.price * quantity,
      },
    ];
  });

  const packCount = lines.reduce((sum, line) => sum + line.quantity, 0);
  const pieceCount = PACKS.reduce(
    (sum, pack) => sum + normaliseQuantity(selection[pack.id] ?? 0) * pack.pieces,
    0,
  );
  const total = lines.reduce((sum, line) => sum + line.total, 0);

  return { lines, packCount, pieceCount, total, isEmpty: lines.length === 0 };
}

/**
 * The message a visitor sends. It never claims stock, price changes or a
 * delivery promise — BiteKasa confirms those in the conversation.
 */
export function buildOrderMessage(selection: OrderSelection): string {
  const { lines, packCount, pieceCount, total, isEmpty } = summariseOrder(selection);
  if (isEmpty) {
    return 'Hello BiteKasa! I would like to ask about your packs and current availability.';
  }

  const items = lines.map((line) => `• ${line.quantity} × ${line.name} (${line.line}) — ${cedi(line.total)}`);
  return [
    'Hello BiteKasa! I would like to order:',
    ...items,
    '',
    `${packCount} ${packCount === 1 ? 'pack' : 'packs'} · ${pieceCount} pieces · ${cedi(total)}`,
    '',
    'Please confirm availability, and whether collection or delivery works.',
  ].join('\n');
}

export const whatsappHref = (message: string) =>
  `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
