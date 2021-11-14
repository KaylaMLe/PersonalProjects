# HighLow
> Calculates the choice most likely to be successful in a game of High or Low

* Language: Python

## Installation

In a terminal with Python 3.9 installed on any operating system:

```sh
python3 HighLow.py
```

or

```sh
python HighLow.py
```

## Usage example

![A test run of entering cards seen into the program](https://i.imgur.com/vFWUDuN.png)

A game of High or Low starts with a full deck shuffled and placed face down. The top card is then flipped over. The player has to predict if the next card to be flipped will have a higher or lower value. (In this version of the game, if the next card has the same value as the current card, a prediction of either higher or lower passes.)
In the command line, enter the current card's suit followed by its value. The most likely choice will then be displayed.

## Release History
*Status: Finished*
* 1.0 (November 4, 2021)
    * Successfully calculates chances of the next card's value and recognizes cards as seen and not yet seen
* 1.1 (November 10, 2021)
	* Condensed lists of cards seen into one 2D list
* 1.2 (November 13, 2021)
	* Restarting a game is now possible with restarting the program