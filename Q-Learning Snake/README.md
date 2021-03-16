# Q-learning Snake 🐉

*This is one of the most fun and productive games I made thus far in this repo.*

## Table of Content (ToC)

- [Description](#description)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Train](#train)
- [Conclusion](#conclusion-✨)

## Description

As the title and the `Main Repository markdown` says in this folder we have a snake game played by a `deep q learning` model (**DQN**).

## Project Structure

#### Here is the structure

```bash
./Q-learning Snake
├── computer/
│   ├── __init__py
│   ├── MachineAgent.py
│   └── ModTensorBoard.py
├── game/
│   ├── __init__.py
│   ├── Board.py
│   ├── EventListener.py
│   ├── Food.py
│   ├── SnakeGameEnv.py
│   └── Snake
├── logs/
│   └── ...
├── models/
│   └── ...
├── __main__.py
└── env.py
```

#### Here is the descriptive structure

| Name                             | Description                                                       |
| -------------------------------- | ----------------------------------------------------------------- |
| **computer/**                    | Contains everything that has to do with the Q-learning model.     |
| **computer/**`__init__.py`       | Package.                                                          |
| **computer/**`MachineAgent.py`   | Here is the train model and the reinforcement model.              |
| **computer/**`ModTensorBoard.py` | This file helps us vizualize the progress of the model.           |
| **game/**                        | Contains everything that has to do with the Snake game.           |
| **game/**`__init__.py`           | Package.                                                          |
| **game/**`Board.py`              | Manages the board vizualization and the scoreboard.               |
| **game/**`EventListener.py`      | Helps with the keyboard inputs of the player.                     |
| **game/**`Food.py`               | Manages the snake's food.                                         |
| **game/**`SnakeGameEnv.py`       | Manages the game environment. For exmaple, render, step..         |
| **game/**`Snake.py`              | Manages the snake head and tail on the board.                     |
| **logs/**                        | Contains everything that has to do with the progress of the game. |
| **models/**                      | Contains everything that has to do with the Q-learning models.    |
| __ main__.py                     | This is the starting state.                                       |
| env.py                           | Containts all constant parameters.                                |

## Setup

## Train

## Conclusion ✨
