import { render, screen } from '@testing-library/react';
import { Dog } from './App';

test('renders learn react link', () => {
  render(<Dog />);
  // const linkElement = screen.getByText(/learn react/i);
  // expect(linkElement).toBeInTheDocument();
});
