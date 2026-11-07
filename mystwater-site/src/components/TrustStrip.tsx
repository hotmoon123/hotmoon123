import { Droplets, HandHeart, MapPin, Star } from 'lucide-react';

const CELLS = [
  { icon: Star, value: '5.0 / 5', label: 'Google Maps rating · 6 reviews, all five stars' },
  { icon: Droplets, value: 'Dodowa aquifer', label: 'Natural mineral water, bottled at the origin' },
  { icon: HandHeart, value: 'Proudly Ghanaian', label: 'Owned, produced and packaged in Ghana — a PNF Industries Limited brand' },
  { icon: MapPin, value: 'Accra & delivery', label: 'On-site purchase plus doorstep delivery — hours on enquiry' },
] as const;

export default function TrustStrip() {
  return (
    <section className="trust" aria-label="Myst Water at a glance">
      <div className="trust-grid">
        {CELLS.map(({ icon: Icon, value, label }) => (
          <div key={value} className="trust-cell">
            <Icon aria-hidden="true" size={20} className="text-[var(--cyan-deep)]" />
            <span className="trust-value">{value}</span>
            <span className="trust-label">{label}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
