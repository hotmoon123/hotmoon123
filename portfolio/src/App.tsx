import { useEffect } from 'react';
import BackToTop from './components/BackToTop';
import Footer from './components/Footer';
import Header from './components/Header';
import { observeReveals } from './animations/motion';
import AboutSection from './sections/AboutSection';
import ApproachSection from './sections/ApproachSection';
import ContactSection from './sections/ContactSection';
import ExperienceSection from './sections/ExperienceSection';
import HeroSection from './sections/HeroSection';
import ProjectsSection from './sections/ProjectsSection';
import SkillsSection from './sections/SkillsSection';

/** One scrolling page. Sections are anchored by id, and the header links to them. */
export default function App() {
  useEffect(() => {
    const root = document.getElementById('root');
    return root ? observeReveals(root) : undefined;
  }, []);

  return (
    <>
      <a className="skip-link" href="#main">
        Skip to content
      </a>
      <Header />
      <main id="main" tabIndex={-1}>
        <HeroSection />
        <AboutSection />
        <SkillsSection />
        <ProjectsSection />
        <ApproachSection />
        <ExperienceSection />
        <ContactSection />
      </main>
      <Footer />
      <BackToTop />
    </>
  );
}
