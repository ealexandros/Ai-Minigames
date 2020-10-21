const MAP = 400;
const DOT_SIZE = 20;
const FRAME = 6;

let board = new Array(MAP/20).fill(0).map(() => new Array(MAP/20).fill(0));
let snake_lenght = 3;
let move = -2;

function setup(){
    createCanvas(MAP, MAP);
    frameRate(FRAME);
    startBoard();
}

function draw(){
    background(20);
    const SNAKE_COLOR = color(255, 0, 0);
    const FOOD = color(0, 200, 0);
    
    changeSnakeBoard();

    for(i=0;i<board.length;i++){
        for(j=0;j<board.length;j++){
            if(board[i][j] == -1){
                fill(FOOD);
                rect(20*j, 20*i, DOT_SIZE, DOT_SIZE);
            }else if(board[i][j] > 0){
                fill(SNAKE_COLOR);
                rect(20*j, 20*i, DOT_SIZE, DOT_SIZE);
            }
        }
    }
}

function keyPressed() {
    if(keyCode === LEFT_ARROW) {
        move = 1;
    }else if(keyCode === RIGHT_ARROW) {
        move = 0;
    }else if(keyCode === UP_ARROW) {
        move = -1;
    }else if(keyCode === DOWN_ARROW) {
        move = -2;
    }
}

function changeSnakeBoard(){
    let resp = -1;
    for(i=0;i<board.length;i++){
        for(j=0;j<board.length;j++){
            if(board[i][j] == snake_lenght){
                if(move == 0){
                    resp = checkSnake(i, j+1);
                }else if(move == 1){
                    resp = checkSnake(i, j-1);
                }else if(move == -1){
                    resp = checkSnake(i-1, j);
                }else if(move == -2){
                    resp = checkSnake(i+1, j);
                }
                if(resp == 1) return;
                if(resp == 2) exit();
            }
        }
    }

    for(i=0;i<board.length;i++){
        for(j=0;j<board.length;j++){
            if(board[i][j] > 0){
                board[i][j] -= 1;
            }
        }
    }
}

function checkSnake(i, j){
    if(i > 19 || i < 0 || j > 19 || j < 0) return 2;
    if(board[i][j] > 0) return 2;

    if(board[i][j] == -1){
        snake_lenght = snake_lenght + 1;
        addRandomFoodPosition();
        board[i][j] = snake_lenght+1;
        editScore();
        return 1;
    }
    board[i][j] = snake_lenght+1;
    return 0;
}

function editScore(){
    document.getElementById("score").innerHTML = `Your score is: ${snake_lenght}`
}

function startBoard(){
    for(i=3;i<6;i++)
        board[i][3] = i-2;
    addRandomFoodPosition();
}

function addRandomFoodPosition(){
    let food = [Math.floor(Math.random() * 10)*2, Math.floor(Math.random() * 10)*2];
    while(board[food[0]][food[1]] > 0){
        food = [Math.floor(Math.random() * 10)*2, Math.floor(Math.random() * 10)*2];
    }
    board[food[0]][food[1]] = -1;
}
