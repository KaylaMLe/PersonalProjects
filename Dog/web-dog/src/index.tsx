import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { Room } from './environment.js';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <Room />
  </React.StrictMode>
);
