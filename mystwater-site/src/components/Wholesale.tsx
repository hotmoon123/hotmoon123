import { FormEvent, useMemo, useState } from 'react';
import { MessageCircle } from 'lucide-react';
import { mailtoLink, waLink } from '../lib/whatsapp';
import { SITE, WHOLESALE_VOLUMES } from '../content';

const SALES_MESSAGE_INTRO = 'Hello Myst Water! I would like to become a stockist.';

export default function Wholesale() {
  const [business, setBusiness] = useState('');
  const [area, setArea] = useState('');
  const [volume, setVolume] = useState<string>(WHOLESALE_VOLUMES[0]);
  const [contact, setContact] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [honeypot, setHoneypot] = useState('');

  const composedMessage = useMemo(() => {
    const lines = [
      SALES_MESSAGE_INTRO,
      `Business: ${business || '—'}`,
      `Area: ${area || '—'}`,
      `Expected volume: ${volume}`,
      `WhatsApp/phone: ${contact || '—'}`,
      email ? `Email: ${email}` : null,
      message ? `Notes: ${message}` : null,
    ].filter(Boolean) as string[];
    return lines.join('\n');
  }, [business, area, volume, contact, email, message]);

  const composedMail = useMemo(
    () => ({
      subject: 'Stockist enquiry — Myst Water',
      body: composedMessage,
    }),
    [composedMessage],
  );

  /** Bots fill hidden fields; humans get the real links. */
  const isBot = honeypot.trim().length > 0;

  const send = (channel: 'whatsapp' | 'email') => {
    if (isBot) return;
    if (channel === 'whatsapp') {
      window.open(waLink(SITE.phoneMapsIntl, composedMessage), '_blank', 'noopener,noreferrer');
    } else {
      // mailto: keeps everything client-side; no data leaves the device otherwise.
      window.location.href = mailtoLink(SITE.email, composedMail.subject, composedMail.body);
    }
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    send('whatsapp');
  };

  return (
    <section className="section wholesale" id="wholesale" aria-labelledby="wholesale-title">
      <div className="wrap wholesale-grid">
        <div>
          <span className="kicker kicker--on-dark">Wholesale &amp; stockists</span>
          <h2 className="wholesale-title" id="wholesale-title" style={{ marginTop: '1rem' }}>
            Put the <span className="accent">feel good water</span> on your shelf.
          </h2>
          <p className="wholesale-copy">
            Shops, depots, canteens, offices, events and churches — if your customers ask for water,
            they should be asking for Myst. Tell us your area and expected volume and we will send
            trade terms within one working day.
          </p>

          <ol className="steps">
            {[
              ['Tell us about your business', 'Name, location and monthly volume — the form takes under a minute.'],
              ['Get your trade terms', 'Minimum order, mixed-design packing, delivery schedule and Mobile Money / invoice payment terms.'],
              ['First delivery, then a rhythm', 'We schedule your first drop and set a standing order that fits your shelf.'],
            ].map(([title, copy], index) => (
              <li key={title} className="step">
                <span className="step-num" aria-hidden="true">{index + 1}</span>
                <span>
                  <span className="step-title">{title}</span>
                  <br />
                  <span className="step-copy">{copy}</span>
                </span>
              </li>
            ))}
          </ol>

          <div className="wholesale-proof" aria-label="Why stockists stay">
            <span className="proof-chip">5.0 ★ Google Maps rating</span>
            <span className="proof-chip">Doorstep delivery proven daily</span>
            <span className="proof-chip">MoMo-friendly terms</span>
            <span className="proof-chip">Ghanaian-made, Ghanaian-owned</span>
          </div>
        </div>

        <form
          className="form-card"
          name="stockist-enquiry"
          method="POST"
          data-netlify="true"
          netlify-honeypot="bot-field"
          onSubmit={handleSubmit}
          aria-label="Stockist enquiry form"
        >
          <input type="hidden" name="form-name" value="stockist-enquiry" />
          {/* Netlify Forms picks this up on deployment; on other hosts the
              WhatsApp / email buttons below are the submission channel. */}
          <p className="honeypot" aria-hidden="true">
            <label>
              Don’t fill this out if you’re human: <input name="bot-field" value={honeypot} onChange={(event) => setHoneypot(event.target.value)} tabIndex={-1} autoComplete="off" />
            </label>
          </p>

          <h3 className="form-title">Become a stockist</h3>
          <p className="form-sub">We reply within one working day — fast, like the reviews.</p>

          <div className="form-grid">
            <div className="field">
              <label htmlFor="ws-business">Business name *</label>
              <input id="ws-business" name="business" required value={business} onChange={(event) => setBusiness(event.target.value)} placeholder="e.g. Sunrise Mini Mart" autoComplete="organization" />
            </div>
            <div className="field">
              <label htmlFor="ws-area">Area / town *</label>
              <input id="ws-area" name="area" required value={area} onChange={(event) => setArea(event.target.value)} placeholder="e.g. East Legon, Tema" />
            </div>
            <div className="field field--full">
              <label htmlFor="ws-volume">Expected volume</label>
              <select id="ws-volume" name="volume" value={volume} onChange={(event) => setVolume(event.target.value)}>
                {WHOLESALE_VOLUMES.map((option) => (
                  <option key={option} value={option}>{option}</option>
                ))}
              </select>
            </div>
            <div className="field">
              <label htmlFor="ws-contact">WhatsApp / phone *</label>
              <input id="ws-contact" name="contact" required inputMode="tel" value={contact} onChange={(event) => setContact(event.target.value)} placeholder="024 000 0000" autoComplete="tel" />
            </div>
            <div className="field">
              <label htmlFor="ws-email">Email <span style={{ fontWeight: 400 }}>(optional)</span></label>
              <input id="ws-email" name="email" type="email" value={email} onChange={(event) => setEmail(event.target.value)} placeholder="you@example.com" autoComplete="email" />
            </div>
            <div className="field field--full">
              <label htmlFor="ws-message">Anything else? <span style={{ fontWeight: 400 }}>(optional)</span></label>
              <textarea id="ws-message" name="message" value={message} onChange={(event) => setMessage(event.target.value)} placeholder="e.g. We need mixed blue and clear designs, delivered every Tuesday…" />
            </div>
          </div>

          <div className="form-actions">
            <button type="submit" className="btn btn--whatsapp">
              <MessageCircle aria-hidden="true" size={18} />
              Send on WhatsApp
            </button>
            <button type="button" className="btn btn--outline" onClick={() => send('email')}>
              Send by email
            </button>
          </div>
          <p className="form-note">
            Sending opens WhatsApp (or your mail app) with everything pre-filled — you press send, nothing is stored on this page.
            Minimum order quantity, trade price list and delivery schedule are shared on enquiry.
          </p>
        </form>
      </div>
    </section>
  );
}
