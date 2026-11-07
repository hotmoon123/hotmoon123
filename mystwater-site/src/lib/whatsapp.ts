const DIGITS = /\D+/g;

/** Build a wa.me link from an international-format number. */
export function waLink(numberIntl: string, message: string): string {
  return `https://wa.me/${numberIntl.replace(DIGITS, '')}?text=${encodeURIComponent(message)}`;
}

/** Build a tel: link. Ghanaian local numbers (leading 0) are converted to +233. */
export function telLink(numberDisplay: string): string {
  const digits = numberDisplay.replace(DIGITS, '');
  const intl = digits.startsWith('0') ? `+233${digits.slice(1)}` : `+${digits}`;
  return `tel:${intl}`;
}

export function mailtoLink(email: string, subject: string, body: string): string {
  return `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}
