import { MessageCircle, PackageCheck, Wallet, Truck } from 'lucide-react';
import { waLink } from '../lib/whatsapp';
import { SITE } from '../content';

const ORDER_MESSAGE =
  'Hello Myst Water! I would like to order Myst Water for delivery. Please confirm availability, price and delivery to my address.';

export default function Delivery() {
  const steps = [
    {
      icon: MessageCircle,
      title: 'Message or call',
      copy: 'WhatsApp us on either number, or tap Order on WhatsApp. Tell us your address and pack count.',
    },
    {
      icon: Wallet,
      title: 'Pay with Mobile Money',
      copy: 'We confirm the total, you send MoMo, we confirm receipt. Simple, like our reviewers do it.',
    },
    {
      icon: Truck,
      title: 'We deliver to your door',
      copy: 'Your packs arrive at your doorstep — home, office, shop or event. Fast, every time.',
    },
    {
      icon: PackageCheck,
      title: 'Reorder in one line',
      copy: 'Running out? One “more packs on Monday” message — that is literally how our customers do it.',
    },
  ] as const;

  return (
    <section className="section" id="delivery" aria-labelledby="delivery-title" style={{ background: 'var(--ice)' }}>
      <div className="wrap delivery-grid">
        <div>
          <span className="kicker">Delivery</span>
          <h2 className="section-title" id="delivery-title" style={{ marginTop: '1rem' }}>
            From our line <span className="accent">to your doorstep.</span>
          </h2>
          <p className="section-copy" style={{ marginTop: '1rem' }}>
            No queue, no stress. Order on WhatsApp or call, pay with Mobile Money, and Myst Water
            comes to you — the exact journey our five-star reviewers describe.
          </p>

          <ol className="delivery-steps">
            {steps.map(({ icon: Icon, title, copy }) => (
              <li key={title} className="step">
                <span className="step-num" aria-hidden="true">
                  <Icon size={18} />
                </span>
                <span>
                  <span className="step-title" style={{ color: 'var(--navy)' }}>{title}</span>
                  <br />
                  <span className="step-copy" style={{ color: 'var(--ink-soft)' }}>{copy}</span>
                </span>
              </li>
            ))}
          </ol>
        </div>

        <aside className="momo-card" aria-label="How Mobile Money payment works">
          <h3 className="momo-title">Mobile Money, doorstep, done.</h3>
          <ul className="momo-list">
            <li><strong>Order:</strong> tell us the packs and your delivery address.</li>
            <li><strong>Pay:</strong> send MoMo to our line — we confirm instantly.</li>
            <li><strong>Receive:</strong> delivery rides out — you get a call on approach.</li>
          </ul>
          <blockquote className="momo-quote">
            “I got the delivery to my doorstep after the payment was made via momo… <strong>Fast with delivery.</strong>”<br />
            <span style={{ color: 'var(--ink-muted)', fontSize: '0.8rem' }}>— Yung Salary, Google review</span>
          </blockquote>
          <a
            className="btn btn--navy"
            style={{ marginTop: '1.25rem', width: '100%' }}
            href={waLink(SITE.phoneMapsIntl, ORDER_MESSAGE)}
            target="_blank"
            rel="noopener noreferrer"
          >
            <MessageCircle aria-hidden="true" size={18} />
            Order on WhatsApp now
          </a>
          <p className="form-note" style={{ marginTop: '0.75rem' }}>
            Delivery areas, fees and timing: on enquiry. Payment before dispatch, as agreed on the call.
          </p>
        </aside>
      </div>
    </section>
  );
}
