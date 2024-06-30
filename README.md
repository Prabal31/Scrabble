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
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
"W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3,
10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
```

## Extensions

Here are some ideas to extend the functionality of this project:

- Add validation to ensure words contain only valid Scrabble letters.
- Implement functionality to handle multiple games and keep track of scores across games.
- Create a user interface to interact with the game data.
- Add functionality to track the number of turns each player has taken.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or suggestions.


Happy Coding!
