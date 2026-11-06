import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import LogoReveal from '../LogoReveal';

describe('LogoReveal', () => {
  it('names the brand reveal section for assistive tech', () => {
    render(<LogoReveal />);
    expect(screen.getByRole('region', { name: 'BiteKasa' })).toBeInTheDocument();
  });

  it('shows a still of the project logo before the glass animation mounts', () => {
    render(<LogoReveal />);
    const stills = screen.getAllByAltText('BiteKasa logo — samosas, spring rolls, hot, crispy, fresh');
    expect(stills.length).toBeGreaterThan(0);
    expect(stills[0]).toHaveAttribute('src');
  });
});
