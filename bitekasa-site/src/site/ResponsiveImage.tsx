/**
 * One image component for the whole site.
 *
 * Every photograph ships as AVIF, WebP and JPEG at two widths, and the browser
 * picks. The original 1024px JPEGs (136–171 kB) are no longer served to anyone:
 * a phone downloads roughly a fifth of that, and the smallest honest file wins.
 *
 * Files are discovered by glob rather than imported one by one, so adding a
 * third width is a build step — not twenty hand-written imports. The naming
 * contract is `<name>-<width>.<format>` inside `assets/responsive/`.
 */
import { SITE_BASE } from '../data/catalogue';

export type ImageName = 'food-fried' | 'food-unfried' | 'food-frozen' | 'bitekasa-logo';

type Format = 'avif' | 'webp' | 'jpg';
type Variant = { url: string; width: number };

const files = import.meta.glob('../../assets/responsive/*.{avif,webp,jpg}', {
  eager: true,
  query: '?url',
  import: 'default',
}) as unknown as Record<string, string>;

const registry: Record<string, Partial<Record<Format, Variant[]>>> = {};

for (const [path, url] of Object.entries(files)) {
  const file = path.split('/').pop() ?? '';
  const match = /^(.+)-(\d+)\.(avif|webp|jpg)$/.exec(file);
  if (!match) continue;

  const [, name, rawWidth, rawFormat] = match;
  const format = rawFormat as Format;
  const width = Number(rawWidth);
  const bucket = (registry[name] ??= {});

  (bucket[format] ??= []).push({ url: url.startsWith('/') ? `${SITE_BASE.replace(/\/$/, '')}${url}` : url, width });
}

for (const formats of Object.values(registry)) {
  for (const variants of Object.values(formats)) {
    variants?.sort((a, b) => a.width - b.width);
  }
}

const srcSet = (variants: Variant[]) => variants.map((variant) => `${variant.url} ${variant.width}w`).join(', ');

type ResponsiveImageProps = {
  name: ImageName;
  alt: string;
  /** How wide the image actually renders, e.g. `(min-width: 1024px) 560px, 92vw`. */
  sizes: string;
  /** Intrinsic size of the largest source, so the browser reserves the box. */
  width: number;
  height: number;
  className?: string;
  /** Above the fold: load eagerly at high priority. Everything else lazy-loads. */
  priority?: boolean;
};

export default function ResponsiveImage({
  name,
  alt,
  sizes,
  width,
  height,
  className,
  priority = false,
}: ResponsiveImageProps) {
  const formats = registry[name] ?? {};
  const fallback = formats.jpg ?? formats.webp ?? formats.avif ?? [];

  if (fallback.length === 0) {
    // A missing asset should be visible in development, not silently blank.
    console.warn(`[ResponsiveImage] no sources found for "${name}"`);
    return null;
  }

  return (
    <picture className="photo-picture">
      {formats.avif && <source type="image/avif" srcSet={srcSet(formats.avif)} sizes={sizes} />}
      {formats.webp && <source type="image/webp" srcSet={srcSet(formats.webp)} sizes={sizes} />}
      <img
        src={fallback[fallback.length - 1].url}
        srcSet={srcSet(fallback)}
        sizes={sizes}
        width={width}
        height={height}
        alt={alt}
        className={className}
        loading={priority ? 'eager' : 'lazy'}
        // `sync` only for the one image a visitor is already looking at; every
        // other image decodes off the main thread.
        decoding={priority ? 'sync' : 'async'}
        fetchPriority={priority ? 'high' : 'auto'}
      />
    </picture>
  );
}
