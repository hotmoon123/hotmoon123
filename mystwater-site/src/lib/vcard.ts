import { SITE } from '../content';

/**
 * MYST WATER — vCard 3.0 for "save to contacts".
 * Every field is traced to content.ts (verified, labelled facts).
 * No invented URLs: the only URL is the Google Maps listing.
 */
export function mystVCard(): string {
  const lines = [
    'BEGIN:VCARD',
    'VERSION:3.0',
    'N:MYST;WATER COMPANY;;;',
    'FN:MYST WATER COMPANY - The Feel Good Water',
    'ORG:PNF Industries Limited',
    `TEL;TYPE=WORK,VOICE:${SITE.phoneMapsIntl}`,
    `TEL;TYPE=CELL,VOICE:${SITE.phoneFbIntl}`,
    `EMAIL;TYPE=WORK:${SITE.email}`,
    'ADR;TYPE=WORK:;;Accra - Tema Beach Road;Accra;;;Ghana',
    `NOTE:Plus code ${SITE.plusCode}. Natural mineral water from the Dodowa aquifer, packaged and proudly made in Ghana. Hours on enquiry; the Google listing shows Saturday 9:00 am opening.`,
    `URL:${SITE.mapsUrl}`,
    'REV:2026-11-12',
    'END:VCARD',
  ];
  return `${lines.join('\r\n')}\r\n`;
}

/** Encoded data URI suitable for <a download>. */
export function mystVCardDataUri(): string {
  return `data:text/vcard;charset=utf-8,${encodeURIComponent(mystVCard())}`;
}
