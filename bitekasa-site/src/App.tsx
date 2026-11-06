import { useEffect, useState, type ReactNode } from 'react';
import { ArrowRight, Menu, MessageCircle, Phone, X } from 'lucide-react';
import { SiInstagram } from 'react-icons/si';
import { AnimatePresence, motion, useReducedMotion } from 'motion/react';
import AnalyticsConsent from './AnalyticsConsent';
import LogoReveal from './LogoReveal';
import logo from '../assets/bitekasa-logo.jpg';
import friedFood from '../assets/food-fried.jpg';
import unfriedFood from '../assets/food-unfried.jpg';
import frozenFood from '../assets/food-frozen.jpg';
import './styles.css';

const INSTAGRAM_URL = 'https://www.instagram.com/bitekasa/';
const SITE_BASE = import.meta.env.BASE_URL;
const WHATSAPP_NUMBER = '233595638696';

type ServiceSlug = 'fried' | 'unfried' | 'frozen';

const SERVICE_PAGES: Record<ServiceSlug, { label: string; title: string; description: string; image: string; alt: string }> = {
  fried: {
    label: 'Fried',
    title: 'Fried samosas & spring rolls',
    description: 'Ask BiteKasa about fried samosas and spring rolls, current availability, pack options and the product mix before ordering.',
    image: 'fried',
    alt: 'Illustrative image of fried samosas and spring rolls.',
  },
  unfried: {
    label: 'Unfried',
    title: 'Unfried samosas & spring rolls',
    description: 'Ask BiteKasa about prepared, unfried samosas and spring rolls. Confirm current availability, pack options and product mix before ordering.',
    image: 'unfried',
    alt: 'Illustrative image of unfried samosas and spring rolls.',
  },
  frozen: {
    label: 'Frozen',
    title: 'Frozen samosas & spring rolls',
    description: 'Ask BiteKasa about rolled and frozen samosas and spring rolls. Confirm current availability, pack options and product mix before ordering.',
    image: 'frozen',
    alt: 'Illustrative image of frozen, unfried samosas and spring rolls.',
  },
};

const SERVICE_IMAGES = { fried: friedFood, unfried: unfriedFood, frozen: frozenFood };
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
  { name: 'GOLDEN', price: 'GH₵200', description: '55 pieces + 500 ml Coca-Cola', className: 'pack-golden' },
  { name: 'PREMIUM', price: 'GH₵250', description: '70 pieces + 1 litre Coca-Cola', className: 'pack-premium' },
];

const whatsappLink = (message: string) =>
  `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;

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
    { label: 'Home', href: `${SITE_BASE}#home` },
    { label: 'Packs', href: `${SITE_BASE}#packs` },
    { label: 'Contact', href: `${SITE_BASE}#contact` },
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
        <a href={`${SITE_BASE}#home`} onClick={closeMenu} aria-label="BiteKasa home" className="flex items-center">
          <img src={logo} alt="BiteKasa BITES logo" className="h-[56px] w-[56px] object-contain" />
        </a>
        <nav className="hidden items-center gap-8 md:flex" aria-label="Main navigation">
          {navItems.map((item) => <a key={item.href} href={item.href} className="nav-link">{item.label}</a>)}
          <a href={whatsappLink('Hello BiteKasa! I would like to ask about your packs and current availability.')} target="_blank" rel="noopener noreferrer" className="header-cta"><MessageCircle aria-hidden="true" size={16} />Order on WhatsApp</a>
        </nav>
        <button
          type="button"
          className="menu-toggle md:hidden"
          aria-label={open ? 'Close navigation' : 'Open navigation'}
          aria-expanded={open}
          aria-controls="mobile-menu"
          onClick={() => setOpen((current) => !current)}
        >
          {open ? <X aria-hidden="true" size={20} strokeWidth={1.8} /> : <Menu aria-hidden="true" size={20} strokeWidth={1.8} />}
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
            <div className="flex flex-col gap-1 py-2">
              {navItems.map((item) => (
                <a key={item.href} href={item.href} onClick={closeMenu} className="mobile-nav-link">{item.label}</a>
              ))}
              <a href={whatsappLink('Hello BiteKasa! I would like to ask about your packs and current availability.')} target="_blank" rel="noopener noreferrer" onClick={closeMenu} className="mobile-menu-cta"><MessageCircle aria-hidden="true" size={16} />Order on WhatsApp</a>
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
        </motion.figure>

        <div className="order-2 md:order-2">
          <Reveal>
            <p className="eyebrow">BITEKASA · SAMOSAS &amp; SPRING ROLLS</p>
            <h1 className="hero-title">Samosas &amp;<br /><em>spring rolls.</em></h1>
            <p className="hero-tagline">hot • crispy • fresh</p>
            <p className="hero-description">Ask about fried, unfried and frozen options.</p>
            <div className="hero-actions">
              <a className="whatsapp-button" href={whatsappLink('Hello BiteKasa! I would like to ask about your packs and current availability.')} target="_blank" rel="noopener noreferrer">
                <MessageCircle aria-hidden="true" size={17} />Order on WhatsApp <ArrowRight aria-hidden="true" size={17} />
              </a>
              <a className="call-button" href={PHONE_NUMBERS[0].href}><Phone aria-hidden="true" size={16} />Call Us</a>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}

function ProductPack({ pack }: { pack: Pack }) {
  return (
    <Reveal className={`product-pack ${pack.className}`}>
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
        Ask about this pack <ArrowRight aria-hidden="true" size={16} />
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
          {PACKS.map((pack) => <ProductPack key={pack.name} pack={pack} />)}
        </div>
        <Reveal className="product-state-note">
          <p>Ask about fried, unfried and frozen options. Confirm which products are available and the pack mix when ordering.</p>
        </Reveal>
      </div>
    </section>
  );
}

function ProductOptions() {
  const options: { slug: ServiceSlug; name: string; image: string; alt: string; state: string }[] = [
    { slug: 'fried', name: 'FRIED', image: friedFood, alt: 'Illustrative image of fried samosas and spring rolls.', state: 'Fried' },
    { slug: 'unfried', name: 'UNFRIED', image: unfriedFood, alt: 'Illustrative image of unfried samosas and spring rolls.', state: 'Prepared, not yet fried' },
    { slug: 'frozen', name: 'FROZEN', image: frozenFood, alt: 'Illustrative image of frozen, unfried samosas and spring rolls.', state: 'Rolled and frozen before frying' },
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
                <a className="option-detail-link" href={`${SITE_BASE}services/${option.slug}/`}>
                  Learn more about {option.name.toLowerCase()} options <ArrowRight aria-hidden="true" size={15} />
                </a>
              </div>
            </Reveal>
          ))}
        </div>
        <p className="illustration-note">Generated examples, not verified photographs of BiteKasa products.</p>
      </div>
    </section>
  );
}

function ServicePage({ slug }: { slug: ServiceSlug }) {
  const page = SERVICE_PAGES[slug];
  const otherServices = (Object.keys(SERVICE_PAGES) as ServiceSlug[]).filter((item) => item !== slug);
  const message = `Hello BiteKasa! I would like to ask about ${page.label.toLowerCase()} samosas and spring rolls. Please confirm current availability, pack options and product mix.`;

  return (
    <>
      <AnalyticsConsent />
      <Header />
      <main>
        <section className="bg-cream px-4 py-10 sm:px-7 sm:py-16 lg:px-12">
          <div className="mx-auto grid max-w-7xl items-center gap-8 md:grid-cols-2 md:gap-12">
            <Reveal>
              <a href={`${SITE_BASE}#home`} className="service-back-link">BiteKasa home <ArrowRight aria-hidden="true" size={14} /></a>
              <p className="eyebrow mt-5">PRODUCT PREPARATION OPTION</p>
              <h1 className="section-title mt-2">{page.title}.</h1>
              <p className="hero-description mt-4">{page.description}</p>
              <p className="image-disclosure mt-4">Illustrative image; not a verified BiteKasa product photograph.</p>
              <div className="hero-actions">
                <a className="whatsapp-button" href={whatsappLink(message)} target="_blank" rel="noopener noreferrer">
                  <MessageCircle aria-hidden="true" size={17} />Ask about availability <ArrowRight aria-hidden="true" size={17} />
                </a>
                <a className="call-button" href={`${SITE_BASE}#packs`}>View packs</a>
              </div>
            </Reveal>
            <Reveal>
              <img src={SERVICE_IMAGES[slug]} alt={page.alt} className="hero-image" />
              <p className="image-disclosure">Illustrative example</p>
            </Reveal>
          </div>
        </section>
        <section className="bg-paper px-4 py-10 sm:px-7 sm:py-14 lg:px-12">
          <div className="mx-auto max-w-7xl">
            <Reveal>
              <p className="eyebrow">EXPLORE PREPARATION OPTIONS</p>
              <h2 className="section-title mt-2">Other options to ask about.</h2>
              <p className="section-intro mt-3">Current stock, quantities, pack mix and collection or delivery details are confirmed directly with BiteKasa.</p>
            </Reveal>
            <div className="service-cross-links mt-7">
              {otherServices.map((other) => (
                <a key={other} href={`${SITE_BASE}services/${other}/`}>
                  <span>{SERVICE_PAGES[other].label} options</span>
                  <ArrowRight aria-hidden="true" size={16} />
                </a>
              ))}
              <a href={`${SITE_BASE}#packs`}><span>View BiteKasa packs</span><ArrowRight aria-hidden="true" size={16} /></a>
            </div>
          </div>
        </section>
        <section className="cta-section px-4 py-10 sm:px-7 sm:py-14 lg:px-12">
          <div className="mx-auto max-w-7xl">
            <p className="eyebrow eyebrow-light">CONFIRM BEFORE ORDERING</p>
            <h2 className="cta-title">Ask BiteKasa<br />about this option.</h2>
            <div className="hero-actions">
              <a className="whatsapp-button" href={whatsappLink(message)} target="_blank" rel="noopener noreferrer">
                <MessageCircle aria-hidden="true" size={17} />WhatsApp BiteKasa <ArrowRight aria-hidden="true" size={17} />
              </a>
              <a className="instagram-link" href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer"><SiInstagram aria-hidden="true" size={16} />Instagram · @bitekasa</a>
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </>
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
            <MessageCircle aria-hidden="true" size={17} />Order on WhatsApp <ArrowRight aria-hidden="true" size={17} />
          </a>
          {PHONE_NUMBERS.map((phone) => (
            <a className="phone-link" key={phone.label} href={phone.href}>
              <Phone aria-hidden="true" size={16} /><strong>{phone.label}</strong><ArrowRight aria-hidden="true" size={16} />
            </a>
          ))}
          <a className="instagram-link" href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer"><SiInstagram aria-hidden="true" size={16} />Instagram · @bitekasa <ArrowRight aria-hidden="true" size={16} /></a>
        </Reveal>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="site-footer px-4 py-5 sm:px-7 lg:px-12">
      <div className="mx-auto flex max-w-7xl flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <a href={`${SITE_BASE}#home`} className="footer-brand">BiteKasa</a>
        <p className="footer-note">Pack details and product condition should be confirmed when ordering.</p>
        <small className="footer-copyright">© 2026 BiteKasa.</small>
      </div>
    </footer>
  );
}

export default function App() {
  const serviceMatch = window.location.pathname.match(/\/services\/(fried|unfried|frozen)\/?$/);
  if (serviceMatch) return <ServicePage slug={serviceMatch[1] as ServiceSlug} />;

  return (
    <>
      <AnalyticsConsent />
      <Header />
      <main>
        <Hero />
        <Packs />
        <ProductOptions />
        <LogoReveal />
        <CTASection />
      </main>
      <Footer />
    </>
  );
}
