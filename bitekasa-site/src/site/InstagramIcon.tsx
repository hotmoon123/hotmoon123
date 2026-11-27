/**
 * The Instagram glyph, drawn here instead of imported.
 *
 * `react-icons` ships a barrel of thousands of icons; one glyph from it is not
 * worth a dependency the whole page pays for. This is four shapes and it
 * inherits `currentColor` like every other icon on the site.
 */
type Props = { size?: number; className?: string };

export default function InstagramIcon({ size = 16, className }: Props) {
  return (
    <svg
      aria-hidden="true"
      focusable="false"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={1.9}
      strokeLinecap="round"
      strokeLinejoin="round"
      className={className}
    >
      <rect x="3" y="3" width="18" height="18" rx="5" />
      <circle cx="12" cy="12" r="4" />
      <circle cx="17.2" cy="6.8" r="0.9" fill="currentColor" stroke="none" />
    </svg>
  );
}
