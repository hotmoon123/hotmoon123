import friedFood from '../../assets/food-fried.jpg';
import unfriedFood from '../../assets/food-unfried.jpg';
import frozenFood from '../../assets/food-frozen.jpg';

/** Single source of truth for every commercial fact on the site. */
export const SITE_BASE = import.meta.env.BASE_URL;
export const WHATSAPP_NUMBER = '233595638696';
export const INSTAGRAM_URL = 'https://www.instagram.com/bitekasa/';
export const INSTAGRAM_HANDLE = '@bitekasa';

export const PHONES = [
  { label: '0595 638 696', href: 'tel:+233595638696' },
  { label: '0552 727 051', href: 'tel:+233552727051' },
] as const;

export type PackId = 'silver' | 'golden' | 'premium';

export type Pack = {
  id: PackId;
  name: string;
  price: number;
  pieces: number;
  drink: string | null;
  className: string;
};

/** Prices confirmed by the owner. Golden is 55 pieces — final. */
export const PACKS: Pack[] = [
  { id: 'silver', name: 'SILVER', price: 100, pieces: 30, drink: null, className: 'pack-silver' },
  {
    id: 'golden',
    name: 'GOLDEN',
    price: 200,
    pieces: 55,
    drink: '500 ml Coca-Cola',
    className: 'pack-golden',
  },
  {
    id: 'premium',
    name: 'PREMIUM',
    price: 250,
    pieces: 70,
    drink: '1 litre Coca-Cola',
    className: 'pack-premium',
  },
];

export const cedi = (amount: number) => `GH₵${amount.toLocaleString('en-GH')}`;

export const packContents = (pack: Pack) =>
  pack.drink ? `${pack.pieces} pieces + ${pack.drink}` : `${pack.pieces} pieces`;

export const packUnitPrice = (pack: Pack) => pack.price / pack.pieces;

export type PreparationSlug = 'fried' | 'unfried' | 'frozen';

export type Preparation = {
  slug: PreparationSlug;
  label: string;
  title: string;
  state: string;
  description: string;
  image: string;
  alt: string;
};

export const PREPARATIONS: Preparation[] = [
  {
    slug: 'fried',
    label: 'FRIED',
    title: 'Fried samosas & spring rolls',
    state: 'Ready to eat',
    description:
      'Ask BiteKasa about fried samosas and spring rolls, current availability, pack options and the product mix before ordering.',
    image: friedFood,
    alt: 'Illustrative image of fried samosas and spring rolls.',
  },
  {
    slug: 'unfried',
    label: 'UNFRIED',
    title: 'Unfried samosas & spring rolls',
    state: 'Prepared, not yet fried',
    description:
      'Ask BiteKasa about prepared, unfried samosas and spring rolls. Confirm current availability, pack options and product mix before ordering.',
    image: unfriedFood,
    alt: 'Illustrative image of unfried samosas and spring rolls.',
  },
  {
    slug: 'frozen',
    label: 'FROZEN',
    title: 'Frozen samosas & spring rolls',
    state: 'Rolled and frozen before frying',
    description:
      'Ask BiteKasa about rolled and frozen samosas and spring rolls. Confirm current availability, pack options and product mix before ordering.',
    image: frozenFood,
    alt: 'Illustrative image of frozen, unfried samosas and spring rolls.',
  },
];

export const FAQS = [
  {
    question: 'How much are the BiteKasa packs?',
    answer:
      'Silver is GH₵100 for 30 pieces. Golden is GH₵200 for 55 pieces with a 500 ml Coca-Cola. Premium is GH₵250 for 70 pieces with a 1 litre Coca-Cola.',
  },
  {
    question: 'How do I place an order?',
    answer:
      'Build your pack selection on this page and tap “Send order on WhatsApp”. The message arrives ready-written with your packs, quantities and total. BiteKasa confirms availability before anything is paid.',
  },
  {
    question: 'What is the difference between fried, unfried and frozen?',
    answer:
      'Fried is ready to eat. Unfried is prepared but not yet fried — for frying yourself. Frozen is rolled and frozen before frying. Ask which option is available today before ordering.',
  },
  {
    question: 'Do you deliver, or do I collect?',
    answer:
      'Delivery and collection are agreed on WhatsApp when you order, together with timing and payment. This page does not promise a delivery area.',
  },
  {
    question: 'Are the photographs on this page real BiteKasa products?',
    answer:
      'No. The food photographs are illustrative images, labelled as such. They show the style of the product, not a verified photograph of a BiteKasa pack.',
  },
];
