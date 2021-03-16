# Environment Values #

FRAME_RATE = 8

MAP_SIZE = 200
BOARD_TABLE = 10 # TABLE SIZE NxN
DOT_SIZE = MAP_SIZE // BOARD_TABLE

ACTION_SPACE_SIZE = 4

# Q-Learning Values  #

MOVE_PENALTY = 1
INVALID_MOVE_PENALTY = 100
FOOD_REWARD = 500

OBSERVATION_SPACE_VALUES = (BOARD_TABLE, BOARD_TABLE, 3)

EPISODES = 5_000
REPLAY_MEMORY_SIZE = 50_000
MIN_REPLAY_MEMORY_SIZE = 1_000
MINIBATCH_SIZE = 64

DISCOUNT = 0.998
LEARNING_RATE = 0.001
UPDATE_TARGET_EVERY = 5
MODEL_NAME = 'SnakeV1'
MIN_REWARD = -200
MEMORY_FRACTION = 0.20

epsilon = 1
EPSILON_DECAY = 0.99975
MIN_EPSILON = 0.001

AGGREGATE_STATS_EVERY = 200
SHOW_PREVIEW = False
SHOW_PREVIEW_EVERY = 1000