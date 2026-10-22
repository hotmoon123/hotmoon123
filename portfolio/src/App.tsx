import { Suspense, lazy } from 'react';
import { Route, Routes } from 'react-router-dom';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import PageTransition from './components/PageTransition';
import ScrollToTop from './components/ScrollToTop';
import About from './pages/About';
import Articles from './pages/Articles';
import CaseStudies from './pages/CaseStudies';
import Contact from './pages/Contact';
import Education from './pages/Education';
import Experience from './pages/Experience';
import NotFound from './pages/NotFound';
import ProjectDetails from './pages/ProjectDetails';
import Projects from './pages/Projects';
import Resume from './pages/Resume';
import Services from './pages/Services';
import Skills from './pages/Skills';

// The home page loads the Three.js scene lazily, so other pages do not download it.
const Home = lazy(() => import('./pages/Home'));

export default function App() {
  return (
    <>
      <a className="skip-link" href="#main">
        Skip to content
      </a>
      <ScrollToTop />
      <Navbar />
      <main id="main" tabIndex={-1}>
        <PageTransition>
          <Suspense fallback={<div className="route-loading" role="status">Loading…</div>}>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/skills" element={<Skills />} />
              <Route path="/projects" element={<Projects />} />
              <Route path="/projects/:slug" element={<ProjectDetails />} />
              <Route path="/experience" element={<Experience />} />
              <Route path="/education" element={<Education />} />
              <Route path="/resume" element={<Resume />} />
              <Route path="/case-studies" element={<CaseStudies />} />
              <Route path="/articles" element={<Articles />} />
              <Route path="/services" element={<Services />} />
              <Route path="/contact" element={<Contact />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </Suspense>
        </PageTransition>
      </main>
      <Footer />
    </>
  );
}
