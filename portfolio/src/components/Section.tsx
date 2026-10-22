import type { ReactNode } from 'react';

interface SectionProps {
  id?: string;
  title: string;
  intro?: string;
  children: ReactNode;
  tone?: 'default' | 'alt';
}

/** A scrollable page section with a labelled heading. */
export default function Section({ id, title, intro, children, tone = 'default' }: SectionProps) {
  const headingId = `${id ?? slugify(title)}-heading`;
  return (
    <section id={id} className={`section section-${tone}`} aria-labelledby={headingId}>
      <div className="container">
        <header className="section-head" data-reveal>
          <h2 id={headingId}>{title}</h2>
          {intro && <p className="muted">{intro}</p>}
        </header>
        {children}
      </div>
    </section>
  );
}

const slugify = (value: string) => value.toLowerCase().replace(/[^a-z0-9]+/g, '-');
