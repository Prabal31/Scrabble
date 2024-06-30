# Scrabble Game Data Processor

## Overview

This project processes data from a group of friends playing Scrabble. The primary objective is to use dictionaries to organize players, their words, and the corresponding points. This README file will guide you through the setup and functionality of the project.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Data Structure](#data-structure)
5. [Extensions](#extensions)
6. [Contributing](#contributing)

## Introduction

The Scrabble Game Data Processor is designed to track the words played by each player and compute their scores based on Scrabble letter values. This project can be extended in various ways to add more functionality and improve data handling.

## Requirements

- Python 3

## Setup

1. **Clone the repository:**

    ```bash
    git clone (https://github.com/Prabal31/Scrabble.git)
    cd scrabble
    ```

3. **Run the script:**

    ```bash
    python scrabble.py
    ```

## Data Structure

The data is organized using dictionaries to keep track of players, words, and points.

Example:

```python
players = {
    'Alice': ['HELLO', 'WORLD'],
    'Bob': ['PYTHON', 'SCRABBLE']
}

points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
    'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
    'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

## Extensions

Here are some ideas to extend the functionality of this project:

- Add validation to ensure words contain only valid Scrabble letters.
- Implement functionality to handle multiple games and keep track of scores across games.
- Create a user interface to interact with the game data.
- Add functionality to track the number of turns each player has taken.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or suggestions.


Happy Coding!
