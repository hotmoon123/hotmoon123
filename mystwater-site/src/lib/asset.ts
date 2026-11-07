/** Prefix a bundled public asset with the configured base path (GitHub Pages subpath). */
export function asset(path: string): string {
  const base = import.meta.env.BASE_URL || '/';
  return `${base.replace(/\/?$/, '/')}${path.replace(/^\/+/, '')}`;
}
