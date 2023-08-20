import head from "./assets/head.png";
import leg from "./assets/leg.png";
import tail from "./assets/tail.png";
import body from "./assets/body.png";

export function Dog() {
  return (
    <div className="Dog">
      <Head />
      <Leg />
      <Body />
    </div>
  );
}

function Head() {
  return <img className="Head" src={head} alt="the dog's head" />;
}

function Leg() {
  return <img className="Leg" src={leg} alt="one of the dog's legs" />;
}

function Tail() {
  return <img className="Tail" src={tail} alt="a waggly tail" />;
}

function Body() {
  return <img className="Body" src={body} alt="the dog's fluffy body" />;
}
