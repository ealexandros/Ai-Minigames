function dotTrainingPhase() {
    for(let i=0;i<EPOCHS;i++) {
        obs = calculateNextMove();
        collision = snakeGameBoardLogic();
        
        reward = calculateNextMoveReward();
        calculateTheQTableError(snake_coordinates, reward, obs);
        if (collision) restartGame();
    }
}

function calculateNextMove() {
    obs = [snake_coordinates[0]-food_coordinates[0], snake_coordinates[1]-food_coordinates[1]];
    if(Math.random() > epsilon) {
        move = findMaxArgMax(q_table[obs])[0];
    } else {
        move = Math.floor(Math.random()*10)%4
    }
    return obs;
}

function calculateNextMoveReward() {
    let reward = -MOVE_PENALTY;
    if ((snake_coordinates[0] == food_coordinates[0]) && (snake_coordinates[1] == food_coordinates[1])) {
        reward = FOOD_REWARD;
    } else if (collision) {
        reward = -COLLISION_PENALTY;
    }
    return reward;
}

function calculateTheQTableError(oldPosition, reward, obs) {
    new_obs = [[oldPosition[0]-food_coordinates[0], oldPosition[1]-food_coordinates[1]]]

    max_future_q = findMaxArgMax(q_table[new_obs])[1];
    current_q = q_table[obs][move];

    let new_q = 0;
    if (reward == FOOD_REWARD) {
        new_q = FOOD_REWARD
    } else {
        new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount * max_future_q);
    }
    q_table[obs][move] = new_q;
}

function createQTable() {
    for(let x1=-TABLE_SIZE+1;x1<TABLE_SIZE; x1++)
        for(let y1=-TABLE_SIZE+1;y1<TABLE_SIZE; y1++)
            q_table[[x1, y1]] = [Math.random()*5%5, Math.random()*5%5, Math.random()*5%5, Math.random()*5%5];
}