import React from 'react';
import './style.css';
import { Dog } from './dog'

export function Room() {
  return (
    <div className="Room">
      <Dog />
      <Floor />
    </div>
  );
}

function Floor() {
  return (
    <img src={'./assets/floor.png'} className="Floor" alt="floor" />
  );
}
