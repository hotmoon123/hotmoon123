import { ExternalLink } from 'lucide-react';
import { REVIEWS, SITE } from '../content';

export default function Reviews() {
  return (
    <section className="section reviews" id="reviews" aria-labelledby="reviews-title">
      <div className="wrap">
        <div className="reviews-top">
          <div className="section-head" style={{ marginBottom: 0 }}>
            <span className="kicker">Reviews</span>
            <h2 className="section-title" id="reviews-title">
              Don’t take <span className="accent">our</span> word for it.
            </h2>
          </div>
          <a className="big-score" href={SITE.mapsUrl} target="_blank" rel="noopener noreferrer" aria-label="See Myst Water on Google Maps — 5.0 stars from 6 reviews">
            <span className="num">5.0</span>
            <span>
              <span className="stars" aria-hidden="true">★★★★★</span>
              <small>
                6 Google reviews, all five stars
                <ExternalLink aria-hidden="true" size={12} style={{ display: 'inline', verticalAlign: '-1px' }} />
              </small>
            </span>
          </a>
        </div>

        <div className="reviews-grid">
          {REVIEWS.map((review) => (
            <figure key={review.name} className="review-card">
              <span className="review-stars" aria-hidden="true">★★★★★</span>
              <blockquote>“{review.text}”</blockquote>
              <figcaption className="review-meta">
                <span className="review-avatar" aria-hidden="true">{review.initials}</span>
                <span>
                  <span className="review-name">{review.name}</span>
                  <br />
                  <span className="review-time">{review.time} · Google</span>
                </span>
              </figcaption>
            </figure>
          ))}
        </div>
        <p className="reviews-note">
          Reviews reproduced verbatim from the MYST WATER COMPANY Google Maps listing (accessed 6 November 2026).
          The owner replied personally to customers there — "Are you welcome anytime sir bright."
        </p>
      </div>
    </section>
  );
}
