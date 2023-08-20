import body from "./assets/body.png";
import tail from "./assets/tail.png";

export function Dog() {
  return (
    <div className="Dog">
      <Body />
      <Tail />
    </div>
  );
}

function Body() {
  return <img className="Body" src={body} alt="the dog's fluffy body" />;
}

function Tail() {
  return <img className="Tail" src={tail} alt="a waggly tail" />;
}
