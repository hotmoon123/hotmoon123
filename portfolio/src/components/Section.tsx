import type { ReactNode } from 'react';

interface SectionProps {
  id: string;
  number: string;
  label: string;
  title: string;
  intro?: string;
  tone: 'dark' | 'light';
  children: ReactNode;
}

/** A full-width page section with a numbered label, a single h2 and its content. */
export default function Section({ id, number, label, title, intro, tone, children }: SectionProps) {
  const headingId = `${id}-title`;
  return (
    <section id={id} className={`section theme-${tone}`} aria-labelledby={headingId}>
      <div className="container">
        <div className="section-head" data-reveal>
          <p className="eyebrow">
            {number} / {label}
          </p>
          <h2 id={headingId}>{title}</h2>
          {intro && <p className="section-intro">{intro}</p>}
        </div>
        {children}
      </div>
    </section>
  );
}
