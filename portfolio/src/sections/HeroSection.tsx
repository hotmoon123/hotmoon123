import { lazy, Suspense, useEffect, useRef } from 'react';
import { wordsIn } from '../animations/motion';
import { profile } from '../data/profile';

// The Three.js scene loads in its own chunk, so the text and links do not wait for WebGL.
const HeroScene = lazy(() => import('../three/HeroScene'));

export default function HeroSection() {
  const titleRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    if (titleRef.current) wordsIn(titleRef.current.querySelectorAll('[data-word]'));
  }, []);

  const words = profile.headline.split(' ');

  return (
    <section id="home" className="hero theme-dark" aria-labelledby="hero-title">
      <div className="container hero-grid">
        <div className="hero-copy">
          <p className="eyebrow">{profile.role}</p>
          <h1 id="hero-title" className="hero-title" ref={titleRef} aria-label={profile.headline}>
            {words.map((word, index) => (
              <span key={`${word}-${index}`}>
                {index > 0 && ' '}
                <span className="word" aria-hidden="true">
                  <span className="word-inner" data-word>
                    {word}
                  </span>
                </span>
              </span>
            ))}
          </h1>
          <p className="hero-lead">{profile.lead}</p>
          <div className="actions">
            <a className="btn btn-primary" href="#projects">
              View my work
            </a>
            <a className="btn btn-secondary" href="#contact">
              Contact me
            </a>
          </div>
          <p className="hero-languages small">{profile.languages.join(' · ')}</p>
        </div>

        <div className="hero-visual">
          <Suspense fallback={null}>
            <HeroScene />
          </Suspense>
        </div>
      </div>

      <a className="scroll-cue" href="#about">
        <span className="visually-hidden">Scroll to about me</span>
        <span aria-hidden="true">Scroll ↓</span>
      </a>
    </section>
  );
}
