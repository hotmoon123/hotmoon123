import { useMemo, useState } from 'react';
import { ArrowRight, MessageCircle, Minus, Plus, RotateCcw } from 'lucide-react';
import { PACKS, cedi, packContents, type PackId } from '../data/catalogue';
import {
  MAX_PER_PACK,
  buildOrderMessage,
  normaliseQuantity,
  summariseOrder,
  whatsappHref,
  type OrderSelection,
} from '../lib/order';
import Reveal from './Reveal';

const EMPTY: OrderSelection = {};

export default function OrderBuilder() {
  const [selection, setSelection] = useState<OrderSelection>(EMPTY);
  const summary = useMemo(() => summariseOrder(selection), [selection]);
  const message = useMemo(() => buildOrderMessage(selection), [selection]);

  const change = (id: PackId, delta: number) => {
    setSelection((current) => {
      const next = normaliseQuantity((current[id] ?? 0) + delta);
      const updated: OrderSelection = { ...current, [id]: next };
      if (next === 0) delete updated[id];
      return updated;
    });
  };

  return (
    <section id="order" className="order-section px-4 py-14 sm:px-7 sm:py-20 lg:px-12 lg:py-24">
      <div className="mx-auto max-w-3xl">
        <Reveal>
          <p className="eyebrow">BUILD AN ORDER</p>
          <h2 className="section-title">Pick your packs.</h2>
          <p className="section-intro">
            Choose what you want and we prepare the WhatsApp message for you. Nothing is charged here — BiteKasa
            confirms availability first.
          </p>
        </Reveal>

        <Reveal delay={0.05}>
          <fieldset className="builder">
            <legend className="builder-legend">Pack selection</legend>

            {PACKS.map((pack) => {
              const quantity = selection[pack.id] ?? 0;
              return (
                <div key={pack.id} className="builder-row">
                  <div className="builder-copy">
                    <p className="builder-name">{pack.name}</p>
                    <p className="builder-detail">
                      {cedi(pack.price)} · {packContents(pack)}
                    </p>
                  </div>

                  <div className="stepper">
                    <button
                      type="button"
                      className="stepper-button"
                      onClick={() => change(pack.id, -1)}
                      disabled={quantity === 0}
                      aria-label={`Remove one ${pack.name} pack`}
                    >
                      <Minus aria-hidden="true" size={16} />
                    </button>
                    <output className="stepper-value" aria-label={`${pack.name} packs selected`}>
                      {quantity}
                    </output>
                    <button
                      type="button"
                      className="stepper-button"
                      onClick={() => change(pack.id, 1)}
                      disabled={quantity >= MAX_PER_PACK}
                      aria-label={`Add one ${pack.name} pack`}
                    >
                      <Plus aria-hidden="true" size={16} />
                    </button>
                  </div>

                  <p className="builder-line-total" aria-hidden={quantity === 0}>
                    {quantity > 0 ? cedi(pack.price * quantity) : ''}
                  </p>
                </div>
              );
            })}
          </fieldset>
        </Reveal>

        <div className="builder-footer">
          <div className="builder-summary" aria-live="polite">
            {summary.isEmpty ? (
              <p className="builder-empty">Add a pack above to see your total.</p>
            ) : (
              <>
                <p className="builder-total">
                  {/* Re-keyed on the value: the tick fires on a real change, never on a re-render. */}
                  <span key={summary.total} className="builder-total-value">
                    {cedi(summary.total)}
                  </span>
                  <span className="builder-total-meta">
                    {summary.packCount} {summary.packCount === 1 ? 'pack' : 'packs'} · {summary.pieceCount} pieces
                  </span>
                </p>
                <p className="builder-note">Prices are confirmed on WhatsApp before you pay.</p>
              </>
            )}
        </div>

          <div className="builder-actions">
            {summary.isEmpty ? (
              <button type="button" className="builder-cta" disabled>
                <MessageCircle aria-hidden="true" size={17} />
                Send order on WhatsApp
              </button>
            ) : (
              <a
                className="builder-cta"
                href={whatsappHref(message)}
                target="_blank"
                rel="noopener noreferrer"
              >
                <MessageCircle aria-hidden="true" size={17} />
                Send order on WhatsApp <ArrowRight aria-hidden="true" size={17} />
              </a>
            )}

            <button
              type="button"
              className="builder-reset"
              onClick={() => setSelection(EMPTY)}
              disabled={summary.isEmpty}
            >
              <RotateCcw aria-hidden="true" size={15} />
              Clear
            </button>
        </div>

        </div>
        {!summary.isEmpty && (
          <details className="builder-preview">
            <summary>Preview the message</summary>
            <pre>{message}</pre>
          </details>
        )}
      </div>
    </section>
  );
}
