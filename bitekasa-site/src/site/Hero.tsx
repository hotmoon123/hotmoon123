import { motion, useReducedMotion } from 'motion/react';
import { ArrowRight, MessageCircle, Phone } from 'lucide-react';
import friedFood from '../../assets/food-fried.jpg';
import { PACKS, PHONES, SITE_BASE, cedi } from '../data/catalogue';
import { whatsappHref } from '../lib/order';
import Reveal from './Reveal';

const cheapest = Math.min(...PACKS.map((pack) => pack.price));

export default function Hero() {
  const reduceMotion = useReducedMotion();

  return (
    <section id="home" className="bg-cream">
      <div className="mx-auto grid max-w-7xl items-center gap-8 px-4 pb-14 pt-8 sm:px-7 sm:pb-20 sm:pt-10 md:grid-cols-2 md:gap-14 md:px-12 md:py-24">
        <motion.figure
          className="hero-photo relative order-2 md:order-1"
          initial={reduceMotion ? false : { opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: reduceMotion ? 0 : 0.4 }}
        >
          <img
            src={friedFood}
            alt="Illustrative image of golden-brown samosas and spring rolls on a plate."
            className="hero-image"
            fetchPriority="high"
          />
          <figcaption className="image-disclosure">Illustrative product image</figcaption>
        </motion.figure>

        <div className="order-1 md:order-2">
          <Reveal>
            <p className="eyebrow">BITEKASA · SAMOSAS &amp; SPRING ROLLS</p>
            <h1 className="hero-title">
              Samosas &amp;
              <br />
              <em>spring rolls.</em>
            </h1>
            <p className="hero-tagline">hot • crispy • fresh</p>
            <p className="hero-description">
              Three packs, from {cedi(cheapest)}. Build your order here and send it to WhatsApp in one tap — or ask
              about fried, unfried and frozen options.
            </p>
            <div className="hero-actions">
              <a className="whatsapp-button" href={`${SITE_BASE}#order`}>
                Build your order <ArrowRight aria-hidden="true" size={17} />
              </a>
              <a
                className="call-button"
                href={whatsappHref('Hello BiteKasa! I would like to ask about your packs and current availability.')}
                target="_blank"
                rel="noopener noreferrer"
              >
                <MessageCircle aria-hidden="true" size={16} />
                Order on WhatsApp
              </a>
            </div>
            <a className="hero-phone" href={PHONES[0].href}>
              <Phone aria-hidden="true" size={14} />
              Or call {PHONES[0].label}
            </a>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
