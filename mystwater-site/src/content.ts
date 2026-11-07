/**
 * MYST WATER — single source of truth for copy and structured data.
 * Every fact is either traced to a public source (see README) or marked
 * "on enquiry". Nothing in this file is invented.
 */

export const SITE = {
  name: 'MYST WATER COMPANY',
  shortName: 'Myst Water',
  tagline: 'The Feel Good Water',
  // Phones as published: Google Maps listing and Facebook page bio. Label them honestly.
  phoneMapsDisplay: '020 410 2171',
  phoneMapsIntl: '+233204102171',
  phoneFbDisplay: '+233 59 699 5220',
  phoneFbIntl: '+233596995220',
  email: 'info@drinkmyst.com',
  addressDisplay: 'Accra – Tema Beach Road, Accra',
  plusCode: 'JW3C+MH',
  mapsUrl: 'https://www.google.com/maps/search/?api=1&query=MYST+WATER+COMPANY',
  mapsEmbed: 'https://www.google.com/maps?q=MYST%20WATER%20COMPANY&output=embed',
  hoursNote: 'Opening hours on enquiry — the Google listing shows Saturday 9:00 am opening.',
  socials: {
    instagram: 'https://www.instagram.com/mystwater/',
    facebook: 'https://www.facebook.com/mystnaturalwater/',
    x: 'https://x.com/Myst_water',
    linkedin: 'https://gh.linkedin.com/company/pnf-industries-limited',
  },
} as const;

export const NAV_ITEMS = [
  { label: 'The range', href: '#range' },
  { label: 'Stockists', href: '#wholesale' },
  { label: 'Delivery', href: '#delivery' },
  { label: 'FAQ', href: '#faq' },
  { label: 'Contact', href: '#contact' },
] as const;

export const SIZES = [
  { value: '500', unit: 'ml', note: 'everyday bottle' },
  { value: '750', unit: 'ml', note: 'on-the-go' },
  { value: '1', unit: 'Litre', note: 'family & sharing' },
] as const;

export const DESIGNS = [
  {
    name: 'Blue',
    image: 'myst-dark-ice.jpg',
    alt: 'Myst Water blue-tinted 500 ml bottle on crushed ice with mint, dark backdrop, MYST WATER logo',
    note: 'Our signature. The one in the reviews, on your doorstep.',
    tag: 'Most popular',
    tagTone: 'cyan' as const,
  },
  {
    name: 'Clear',
    image: 'myst-clear-navycap.jpg',
    alt: 'Myst Water clear natural mineral water bottle with navy cap on a pale aqua backdrop',
    note: 'The pure classic. Crisp, clean, unmistakably Myst.',
    tag: 'The original',
    tagTone: 'cyan' as const,
  },
  {
    name: 'Green',
    image: 'myst-green.jpg',
    alt: 'Myst Water clear bottle with green cap against a light backdrop with green and blue water droplets',
    note: 'The fresh one. Same water, extra feel-good.',
    tag: 'The fresh one',
    tagTone: 'leaf' as const,
  },
] as const;

/** Real reviews reproduced from the business's Google Maps listing (accessed 2026-11-06). */
export const REVIEWS = [
  {
    name: 'Yung Salary',
    initials: 'YS',
    time: '2 months ago',
    text: 'I really appreciate your job Mr. Homor. I got the delivery to my doorstep after the payment was made via momo… Fast with delivery.',
  },
  {
    name: 'Olivia Griffin',
    initials: 'OG',
    time: 'A month ago',
    text: 'Myst water is the best.',
  },
  {
    name: 'God Fada',
    initials: 'GF',
    time: '4 months ago',
    text: 'Thank you Mr Amable. For your great work.',
  },
  {
    name: 'Edward Wagner',
    initials: 'EW',
    time: '4 months ago',
    text: 'Thanks your delivery mr Addison. I will need more packs on Monday.',
  },
  {
    name: 'Rubby Smith',
    initials: 'RS',
    time: '5 months ago',
    text: '#MYSTWATER — Always buy from myst water 💧.',
  },
  {
    name: 'Cassandra Griffin',
    initials: 'CG',
    time: '9 hours ago',
    text: 'God bless you for the delivery sir.',
  },
] as const;

export const FAQS = [
  {
    q: 'What sizes does Myst Water come in?',
    a: '500 ml, 750 ml and 1 Litre — in blue, clear (natural mineral water) and green designs. Exact availability per size and design is confirmed on enquiry.',
  },
  {
    q: 'Where does the water come from?',
    a: 'Myst Water is natural mineral water sourced from an aquifer in Dodowa, Eastern Region, and filtered and packaged at the origin. It is the flagship brand of PNF Industries Limited, proudly Ghanaian-owned, produced and packaged.',
  },
  {
    q: 'Do you deliver to my door?',
    a: 'Yes — doorstep delivery is how most of our customers buy. Order by phone or WhatsApp, and your water comes to you after payment via Mobile Money. Delivery areas and fees: on enquiry.',
  },
  {
    q: 'How do I pay?',
    a: 'Mobile Money (MoMo) is the usual way — exactly how our Google reviewers do it. Bank transfer and other arrangements: on enquiry.',
  },
  {
    q: 'How do I order for home or work?',
    a: 'Call or WhatsApp either number on this page, or send us a message on Instagram @mystwater. Tell us your address and how many packs you need — we confirm price, delivery and payment before dispatch.',
  },
  {
    q: 'How do I become a stockist or distributor?',
    a: 'Use the stockist form on this page — it reaches our sales line with your business name, area and how many packs you expect to move. Minimum order quantity, trade pricing and delivery terms: on enquiry.',
  },
  {
    q: 'Where can I find Myst Water in shops?',
    a: 'Myst is stocked by wholesale partners across Accra and beyond. Contact us and we will point you to the nearest stockist, or set up a standing supply for your shop, canteen or office.',
  },
  {
    q: 'Is the facility accessible?',
    a: 'Yes. Our Google listing shows wheelchair-accessible parking, entrance, seating and toilets, an assistive hearing loop, a nursing room, a changing table, gender-neutral toilets, and free on-site parking.',
  },
] as const;

export const WHOLESALE_VOLUMES = [
  'Under 500 packs / month',
  '500 – 2,000 packs / month',
  '2,000 – 10,000 packs / month',
  '10,000+ packs / month',
  'Just exploring — tell me more',
] as const;
