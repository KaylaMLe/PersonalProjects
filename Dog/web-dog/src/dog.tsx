import React from 'react';

export function Dog() {
  return (
    <div className="Dog" >
      <Head />
      <Leg />
      <Body />
    </div>
  );
}

function Head() {
  return <img className="Head" src={'./assets/head.png'} alt="the dog's head" />;
}

function Leg() {
  return <img className="Leg" src={'./assets/leg.png'} alt="one of the dog's legs" />;
}

function Tail() {
  return <img className="Tail" src={'./assets/tail.png'} alt="a waggly tail" />;
}

function Body() {
  return <img className="Body" src={'./assets/body.png'} alt="the dog's fluffy body" />;
}
