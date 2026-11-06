import AnalyticsConsent from './AnalyticsConsent';
import LogoIntro from './LogoIntro';
import { PREPARATIONS, type PreparationSlug } from './data/catalogue';
import ContactCta from './site/ContactCta';
import Faq from './site/Faq';
import Footer from './site/Footer';
import Header from './site/Header';
import Hero from './site/Hero';
import HowItWorks from './site/HowItWorks';
import OrderBuilder from './site/OrderBuilder';
import Packs from './site/Packs';
import PreparationOptions from './site/PreparationOptions';
import ServicePage from './site/ServicePage';
import StickyCta from './site/StickyCta';

const SLUGS = PREPARATIONS.map((preparation) => preparation.slug);

function HomePage() {
  return (
    <>
      <a className="skip-link" href="#main">
        Skip to content
      </a>
      <Header />
      <main id="main">
        <Hero />
        <Packs />
        <OrderBuilder />
        <HowItWorks />
        <PreparationOptions />
        <Faq />
        <ContactCta />
      </main>
      <Footer />
      <StickyCta />
    </>
  );
}

export default function App() {
  const match = window.location.pathname.match(/\/services\/([a-z]+)\/?$/);
  const slug = match?.[1] as PreparationSlug | undefined;

  if (slug && SLUGS.includes(slug)) {
    return (
      <>
        <AnalyticsConsent />
        <ServicePage slug={slug} />
      </>
    );
  }

  return (
    <>
      <LogoIntro />
      <AnalyticsConsent />
      <HomePage />
    </>
  );
}
