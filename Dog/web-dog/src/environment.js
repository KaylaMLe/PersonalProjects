import './style.css';
import { Dog } from './dog'
import floor from './assets/floor.png';

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
    <img src={floor} className="Floor" alt="floor" />
  );
}
