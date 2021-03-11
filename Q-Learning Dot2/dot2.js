/* GAME VARIABLES */
const MAP = 400;
const DOT_SIZE = 50;
const TABLE_SIZE = MAP/DOT_SIZE

const FRAME = 6;

let foodCoordinates = [-1, -1];
const SNAKE_LENGHT = 2;
let snakeCoordinates = [[3, 3], [4, 3]];

let board = new Array(TABLE_SIZE).fill(0).map(() => new Array(TABLE_SIZE).fill(0));
let move = 0;

let score = 0;
let bestScore = 0;

/* Q-VARIABLES */
/* HYPERPARAMS */
let q_table = {}

const EPOCHS = 2500000;

const learning_rate = 0.005;
const discount = 0.95;

const MOVE_PENALTY = 8
const COLLISION_PENALTY = 600
const SELF_COLLISION_PENALTY = 300
const FOOD_REWARD = 1000

let epsilon = 0.4;
const EPS_DECAY = 0.9998


function setup(){
    createCanvas(MAP, MAP);
    frameRate(FRAME);

    setDotGameBoard();
    createQTable();

    dotTrainingPhase();
    restartGame();
}

function draw(){
    obs = calculateNextMove();

    background(20);
    collision = drawGameFrame();
    
    reward = calculateNextMoveReward();
    calculateTheQTableError(snakeCoordinates, reward, obs);
    if (collision) restartGame();
}

function drawGameFrame() {
    const SNAKE_COLOR = color(255, 0, 0);
    const FOOD = color(0, 200, 0);

    collision = snakeGameBoardLogic();
    for(i=0;i<board.length;i++) {
        for(j=0;j<board.length;j++) {
            if(board[i][j] == -1) {
                fill(FOOD);
                rect(DOT_SIZE*j, DOT_SIZE*i, DOT_SIZE, DOT_SIZE);
            } else if(board[i][j] > 0) {
                fill(SNAKE_COLOR);
                rect(DOT_SIZE*j, DOT_SIZE*i, DOT_SIZE, DOT_SIZE);
            }
        }
    }
    return collision;
}
