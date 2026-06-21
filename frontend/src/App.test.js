import { render, screen } from '@testing-library/react';
import App from './App';

test('renders room table header', () => {
  render(<App />);
  const titleElement = screen.getByText(/Room Number/i);
  expect(titleElement).toBeInTheDocument();
});
