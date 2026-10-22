import type { ProjectStatus } from '../data/types';

/** Shows the honest state of a project. Colour is not the only signal: the text is always shown. */
export default function StatusBadge({ status }: { status: ProjectStatus }) {
  return <span className={`badge badge-${status.toLowerCase().replace(' ', '-')}`}>{status}</span>;
}
