import { useState } from 'react';
import Contact from './components/Contact';
import Delivery from './components/Delivery';
import Faq from './components/Faq';
import Footer from './components/Footer';
import Header from './components/Header';
import Hero from './components/Hero';
import Products from './components/Products';
import Reviews from './components/Reviews';
import Source from './components/Source';
import SplashScreen from './components/SplashScreen';
import StickyCta from './components/StickyCta';
import TrustStrip from './components/TrustStrip';
import Wholesale from './components/Wholesale';

export default function App() {
  // Intro overlay on app open. Tapping anywhere (or Escape/Enter/Space, or
  // letting the animation finish) reveals the site; it renders beneath it.
  const [introDone, setIntroDone] = useState(false);

  return (
    <>
      {!introDone && <SplashScreen onDone={() => setIntroDone(true)} />}
      <a className="skip-link" href="#main">
        Skip to content
      </a>
      <Header />
      <main id="main">
        <Hero />
        <TrustStrip />
        <Products />
        <Wholesale />
        <Delivery />
        <Source />
        <Reviews />
        <Faq />
        <Contact />
      </main>
      <Footer />
      <StickyCta />
    </>
  );
}
