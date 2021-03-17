# Q-learning Snake 🐉

*This is one of the most fun and productive games I made thus far in this repo.*

## Table of Content (ToC)

- [Description](#description)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Visualization and Modification](#visualization-and-modification)
- [Train](#train)
- [Conclusion](#conclusion-✨)

## Description

As the title and the `Main Repository Markdown` says in this folder we have a snake game played by a `deep q learning` model (**DQN**).

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
| **computer/** __ init__.py       | Package.                                                          |
| **computer/** MachineAgent.py    | Here is the train model and the reinforcement model.              |
| **computer/** ModTensorBoard.py  | This file helps us visualize the progress of the model.           |
| **game/**                        | Contains everything that has to do with the snake game.           |
| **game/** __ init__.py           | Package.                                                          |
| **game/** Board.py               | Manages the board Visualization and the scoreboard.               |
| **game/** EventListener.py       | Helps with the keyboard inputs of the player.                     |
| **game/** Food.py                | Manages the snake's food.                                         |
| **game/** SnakeGameEnv.py        | Manages the game environment. For exmaple, render, step..         |
| **game/** Snake.py               | Manages the snake head and tail on the board.                     |
| **logs/**                        | Contains everything that has to do with the progress of the game. |
| **models/**                      | Contains everything that has to do with the Q-learning models.    |
| __ main__.py                     | As you can see, this is the file that we need to run first.       |
| env.py                           | Contains all constant parameters.                                 |

## Setup

For the setup you will need to have install the following `libs`:

| Name              | Version                   |
|-------------------|---------------------------|
| Python            | v3.8.8                    |
| Tensorflow        | v2.2.0                    |
| Tensorboard       | v2.4.1                    |
| Pygame            | v2.1.0                    |
| Pillow            | v8.1.2                    |
| Tqdm              | NaN                       |

*The `NaN` means that every version can be installed.* 

If you want to train the model from scratch I would suggest you to download the tensorflow-gpu more information about that you can find here: [tensorflow-gpu](https://www.tensorflow.org/install/gpu)

## Visualization and Modification

If you want to visualize the progress of your training real time make sure that you have tensorboard install. If you have installed tensorboard 
```bash
-> tensorboard --logdir='logs\'
```

## Train

## Conclusion ✨
