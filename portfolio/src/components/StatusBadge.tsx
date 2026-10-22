import type { ProjectStatus } from '../data/types';

/** Shows a project's honest status. The class name is derived from the label, so styles stay in sync. */
export default function StatusBadge({ status }: { status: ProjectStatus }) {
  const slug = status.toLowerCase().replace(/\s+/g, '-');
  return <span className={`badge badge-${slug}`}>{status}</span>;
}
