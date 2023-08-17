import './style.css';
import dog from './assets/artists-rendition.png'
import floor from './assets/floor.png';

export function Room() {
  return (
    <div className="Room">
      <Dog />
      <Floor />
    </div>
  )
}

function Dog() {
  return (
    <img src={dog} className="Dog" alt="A friendly dog" />
  )
}

function Floor() {
  return (
    <img src={floor} className="Floor" alt="floor" />
  );
}
