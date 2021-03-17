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
| Keras             | v2.4.3                    |
| Pygame            | v2.1.0                    |
| Pillow            | v8.1.2                    |
| Tqdm              | NaN                       |

*The `NaN` means that every version can be installed.* 

If you want to train the model from scratch I would suggest you to download the tensorflow-gpu more information about that you can find here: [tensorflow-gpu](https://www.tensorflow.org/install/gpu)

## Visualization and Modification

If you want to visualize the progress of your training real time make sure that you have tensorboard install. If you have installed tensorboard just type this command on you terminal:

```bash
..\Q-learning Snake>tensorboard --logdir='logs\'
```

Now if you want to add a existing model you can type the next command:


```bash
..\Q-learning Snake>python __init__.py -p path_of_model
```

Where the path_of_model is the relative path to the model you want to use.

## Train

If you want to train a new rl model I recommend you to download the tensorflow-gpu because it takes a lot of time. For more information about tesnorflow gpu you can find [here](https://www.tensorflow.org/install/gpu).

In order to make your own model you can change the params in the `env.py` file. More specifically:
```
EPISODES             = ...
MINIBATCH_SIZE       = ...
DISCOUNT             = ...

LEARNING_RATE        = ...
MOVE_PENALTY         = ...
INVALID_MOVE_PENALTY = ...
FOOD_REWARD          = ...

epsilon              = ...
EPSILON_DECAY        = ...
MIN_EPSILON          = ...
```

After you change the params you want to change just run the __init__.py file and the training will start.

Last but not least you can change the model in the `MachineAgent.py` file.

## Conclusion ✨

This is by far my best project with reinforcement learning.