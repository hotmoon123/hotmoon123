import { describe, expect, it } from 'vitest';
import { mystVCard, mystVCardDataUri } from '../lib/vcard';

describe('MYST vCard (save-to-contacts)', () => {
  it('is a well-formed vCard 3.0 payload', () => {
    const vcf = mystVCard();
    expect(vcf.startsWith('BEGIN:VCARD\r\nVERSION:3.0\r\n')).toBe(true);
    expect(vcf.endsWith('END:VCARD\r\n')).toBe(true);
    expect(vcf).toContain('ORG:PNF Industries Limited');
  });

  it('carries both published phones, the email, and the plus code — nothing invented', () => {
    const vcf = mystVCard();
    expect(vcf).toContain('+233204102171'); // Google Maps listing number
    expect(vcf).toContain('+233596995220'); // Facebook page number
    expect(vcf).toContain('info@drinkmyst.com');
    expect(vcf).toContain('JW3C+MH');
    // The only URL may be the Google Maps listing; no drinkmyst.com claim while it is down.
    const urls = vcf.split('\r\n').filter((line) => line.startsWith('URL:'));
    expect(urls).toEqual(['URL:https://www.google.com/maps/search/?api=1&query=MYST+WATER+COMPANY']);
  });

  it('encodes as a vcard data URI for <a download>', () => {
    const uri = mystVCardDataUri();
    expect(uri.startsWith('data:text/vcard;charset=utf-8,')).toBe(true);
    expect(decodeURIComponent(uri)).toContain('FN:MYST WATER COMPANY');
  });
});
