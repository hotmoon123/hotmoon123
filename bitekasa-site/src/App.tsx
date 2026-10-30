import { useEffect, useState, type ReactNode } from 'react';
import { AnimatePresence, motion, useReducedMotion } from 'motion/react';
import logo from '../assets/bitekasa-logo.jpg';
import friedFood from '../assets/food-fried.jpg';
import unfriedFood from '../assets/food-unfried.jpg';
import frozenFood from '../assets/food-frozen.jpg';
import LazySnackCanvas from './LazySnackCanvas';
import './styles.css';

const INSTAGRAM_URL = 'https://www.instagram.com/bitekasa/';
const WHATSAPP_NUMBER = '233595638696';
const PHONE_NUMBERS = [
  { label: '0595 638 696', href: 'tel:+233595638696' },
  { label: '0552 727 051', href: 'tel:+233552727051' },
];

type Pack = {
  name: 'SILVER' | 'GOLDEN' | 'PREMIUM';
  price: string;
  description: string;
  className: string;
};

const PACKS: Pack[] = [
  { name: 'SILVER', price: 'GH₵100', description: '30 pieces', className: 'pack-silver' },
  { name: 'GOLDEN', price: 'GH₵200', description: '50 pieces + 500 ml Coca-Cola', className: 'pack-golden' },
  { name: 'PREMIUM', price: 'GH₵250', description: '70 pieces + 1 litre Coca-Cola', className: 'pack-premium' },
];

const whatsappLink = (message: string) =>
  `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;

function Arrow({ className = 'h-4 w-4' }: { className?: string }) {
  return (
    <svg className={className} viewBox="0 0 20 20" fill="none" aria-hidden="true">
      <path d="M4.5 10h10m-4-4 4 4-4 4" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

function Reveal({ children, className = '', delay = 0 }: { children: ReactNode; className?: string; delay?: number }) {
  const reduceMotion = useReducedMotion();
  return (
    <motion.div
      className={className}
      initial={reduceMotion ? false : { opacity: 0, y: 10 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.18 }}
      transition={{ duration: reduceMotion ? 0 : 0.38, delay, ease: 'easeOut' }}
    >
      {children}
    </motion.div>
  );
}

function Header() {
  const [open, setOpen] = useState(false);
  const reduceMotion = useReducedMotion();
  const closeMenu = () => setOpen(false);
  const navItems = [
    { label: 'Home', href: '#home' },
    { label: 'Packs', href: '#packs' },
    { label: 'Contact', href: '#contact' },
  ];

  useEffect(() => {
    const handleKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') closeMenu();
    };
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, []);

  return (
    <header className="sticky top-0 z-50 border-b border-red/15 bg-cream">
      <div className="mx-auto flex h-[66px] max-w-7xl items-center justify-between px-4 sm:px-7 lg:px-12">
        <a href="#home" onClick={closeMenu} aria-label="BiteKasa home" className="flex items-center">
          <img src={logo} alt="BiteKasa BITES logo" className="h-[56px] w-[56px] object-contain" />
        </a>
        <nav className="hidden items-center gap-8 md:flex" aria-label="Main navigation">
          {navItems.map((item) => <a key={item.href} href={item.href} className="nav-link">{item.label}</a>)}
          <a href={whatsappLink('Hello BiteKasa! I would like to ask about your packs and current availability.')} target="_blank" rel="noopener noreferrer" className="header-cta">Order on WhatsApp</a>
        </nav>
        <button
          type="button"
          className="menu-toggle md:hidden"
          aria-label={open ? 'Close navigation' : 'Open navigation'}
          aria-expanded={open}
          aria-controls="mobile-menu"
          onClick={() => setOpen((current) => !current)}
        >
          <span className={open ? 'menu-line menu-line-open-top' : 'menu-line'} />
          <span className={open ? 'menu-line opacity-0' : 'menu-line'} />
          <span className={open ? 'menu-line menu-line-open-bottom' : 'menu-line'} />
        </button>
      </div>
      <AnimatePresence>
        {open && (
          <motion.nav
            id="mobile-menu"
            aria-label="Mobile navigation"
            initial={reduceMotion ? false : { height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: reduceMotion ? 0 : 0.18 }}
            className="overflow-hidden border-t border-red/15 bg-cream px-4 md:hidden"
          >
            <div className="flex flex-col py-2">
              {navItems.map((item) => (
                <a key={item.href} href={item.href} onClick={closeMenu} className="mobile-nav-link">{item.label}</a>
              ))}
              <a href={whatsappLink('Hello BiteKasa! I would like to ask about your packs and current availability.')} target="_blank" rel="noopener noreferrer" onClick={closeMenu} className="mobile-menu-cta">Order on WhatsApp</a>
            </div>
          </motion.nav>
        )}
      </AnimatePresence>
    </header>
  );
}

function Hero() {
  const reduceMotion = useReducedMotion();
  return (
    <section id="home" className="bg-cream">
      <div className="mx-auto grid max-w-7xl items-center gap-5 px-4 pb-9 pt-4 sm:px-7 sm:pb-14 sm:pt-7 md:grid-cols-2 md:gap-12 md:px-12 md:py-16">
        <motion.figure
          className="hero-photo relative order-1"
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
          <div className="three-accent" aria-hidden="true"><LazySnackCanvas /></div>
        </motion.figure>

        <div className="order-2 md:order-2">
          <Reveal>
            <p className="eyebrow">BITEKASA · SAMOSAS &amp; SPRING ROLLS</p>
            <h1 className="hero-title">Samosas &amp;<br /><em>spring rolls.</em></h1>
            <p className="hero-tagline">hot • crispy • fresh</p>
            <p className="hero-description">Ask about fried, unfried and frozen options.</p>
            <div className="hero-actions">
              <a className="whatsapp-button" href={whatsappLink('Hello BiteKasa! I would like to ask about your packs and current availability.')} target="_blank" rel="noopener noreferrer">
                Order on WhatsApp <Arrow />
              </a>
              <a className="call-button" href={PHONE_NUMBERS[0].href}>Call Us</a>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}

function ProductPack({ pack, index }: { pack: Pack; index: number }) {
  return (
    <Reveal delay={index * 0.06} className={`product-pack ${pack.className}`}>
      <span className="pack-index">0{index + 1}</span>
      <h3 className="pack-name">{pack.name}</h3>
      <p className="pack-price">{pack.price}</p>
      <p className="pack-description">{pack.description}</p>
      <a
        href={whatsappLink(`Hello BiteKasa! I am interested in the ${pack.name} pack: ${pack.price}, ${pack.description}. Please confirm current availability and product condition.`)}
        target="_blank"
        rel="noopener noreferrer"
        className="pack-link"
        aria-label={`Ask about the ${pack.name} pack on WhatsApp`}
      >
        Ask about this pack <Arrow className="h-4 w-4" />
      </a>
    </Reveal>
  );
}

function Packs() {
  return (
    <section id="packs" className="bg-paper px-4 py-11 sm:px-7 sm:py-16 lg:px-12">
      <div className="mx-auto max-w-7xl">
        <Reveal className="section-heading-row">
          <div>
            <p className="eyebrow">THE PACKS</p>
            <h2 className="section-title">Choose your pack.</h2>
          </div>
          <p className="section-intro">Pack details and product condition can be confirmed with your enquiry.</p>
        </Reveal>
        <div className="grid gap-3 sm:grid-cols-3 sm:gap-4">
          {PACKS.map((pack, index) => <ProductPack key={pack.name} pack={pack} index={index} />)}
        </div>
        <Reveal className="product-state-note">
          <p>Ask about fried, unfried and frozen options. Confirm which products are available and the pack mix when ordering.</p>
        </Reveal>
      </div>
    </section>
  );
}

function ProductOptions() {
  const options = [
    { name: 'FRIED', image: friedFood, alt: 'Illustrative image of fried samosas and spring rolls.', state: 'Fried' },
    { name: 'UNFRIED', image: unfriedFood, alt: 'Illustrative image of unfried samosas and spring rolls.', state: 'Prepared, not yet fried' },
    { name: 'FROZEN', image: frozenFood, alt: 'Illustrative image of frozen, unfried samosas and spring rolls.', state: 'Rolled and frozen before frying' },
  ];
  return (
    <section className="bg-cream px-4 py-11 sm:px-7 sm:py-16 lg:px-12">
      <div className="mx-auto max-w-7xl">
        <Reveal className="mb-6">
          <p className="eyebrow">PRODUCT OPTIONS</p>
          <h2 className="section-title">Choose a preparation.</h2>
        </Reveal>
        <div className="grid gap-4 sm:grid-cols-3">
          {options.map((option, index) => (
            <Reveal key={option.name} delay={index * 0.05} className="option-card">
              <img src={option.image} alt={option.alt} className="option-image" loading="lazy" />
              <div className="option-copy">
                <p className="image-disclosure">Illustrative image</p>
                <h3 className="option-name">{option.name}</h3>
                <p className="option-state">{option.state}</p>
              </div>
            </Reveal>
          ))}
        </div>
        <p className="illustration-note">Generated examples, not verified photographs of BiteKasa products.</p>
      </div>
    </section>
  );
}

function CTASection() {
  return (
    <section id="contact" className="cta-section px-4 py-10 sm:px-7 sm:py-14 lg:px-12">
      <div className="mx-auto grid max-w-7xl gap-6 md:grid-cols-[1fr_0.9fr] md:items-center">
        <Reveal>
          <p className="eyebrow eyebrow-light">CONTACT BITEKASA</p>
          <h2 className="cta-title">Let’s talk<br />snack time.</h2>
          <p className="cta-copy">Ask about the packs and current product options.</p>
        </Reveal>
        <Reveal delay={0.05} className="cta-actions">
          <a className="whatsapp-button cta-whatsapp" href={whatsappLink('Hello BiteKasa! I would like to ask about your packs and current availability.')} target="_blank" rel="noopener noreferrer">
            Order on WhatsApp <Arrow />
          </a>
          {PHONE_NUMBERS.map((phone) => (
            <a className="phone-link" key={phone.label} href={phone.href}>
              <span>Call Us</span><strong>{phone.label}</strong><Arrow />
            </a>
          ))}
          <a className="instagram-link" href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">Instagram · @bitekasa <Arrow /></a>
        </Reveal>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="site-footer px-4 py-5 sm:px-7 lg:px-12">
      <div className="mx-auto flex max-w-7xl flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <a href="#home" className="footer-brand">BiteKasa</a>
        <p className="footer-note">Pack details and product condition should be confirmed when ordering.</p>
        <small className="footer-copyright">© 2026 BiteKasa.</small>
      </div>
    </footer>
  );
}

export default function App() {
  return (
    <>
      <Header />
      <main>
        <Hero />
        <Packs />
        <ProductOptions />
        <CTASection />
      </main>
      <Footer />
    </>
  );
}
