# Traffic Signal LEDs on a Raspberry Pi

> Using WiringPi and some simple circuitry, I was able to create traffic lights that turn on, blink, and turn off in a sequence.

* Language: ARM assembly
* Status: Finished *

![A labelled image of a circuit on a breadboard.](https://i.imgur.com/D2NcmQL.png "Labelled circuit")

I would have loved to do more with ARM assembly and WiringPi, but there were some difficulties in implementing a for loop after using "delay." I am
interested in investigating how WiringPi implements this function.

## Installation
With GCC on Windows, Mac OS X, and Unix systems:

```sh
g++ traffic_signal.s -lwiringPi -g -o traffic_signal
```