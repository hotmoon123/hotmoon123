import { useState } from 'react';

type CopyState = 'idle' | 'copied' | 'failed';

/** Copies the address with the Clipboard API, falling back to a selection-based copy. */
async function copyText(text: string): Promise<boolean> {
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      // Fall through to the legacy method below.
    }
  }
  const field = document.createElement('textarea');
  field.value = text;
  field.setAttribute('readonly', '');
  field.style.position = 'fixed';
  field.style.opacity = '0';
  document.body.appendChild(field);
  field.select();
  let copied = false;
  try {
    copied = document.execCommand('copy');
  } catch {
    copied = false;
  }
  field.remove();
  return copied;
}

export default function CopyEmail({ email }: { email: string }) {
  const [state, setState] = useState<CopyState>('idle');

  const handleCopy = async () => {
    const ok = await copyText(email);
    setState(ok ? 'copied' : 'failed');
    window.setTimeout(() => setState('idle'), 2500);
  };

  return (
    <div className="copy-email">
      <button type="button" className="btn btn-secondary" onClick={handleCopy}>
        Copy email address
      </button>
      <p className="small status" role="status" aria-live="polite">
        {state === 'copied' && 'Email address copied.'}
        {state === 'failed' && 'Copy failed. Select the address and copy it manually.'}
      </p>
    </div>
  );
}
