import numpy as np
from typing import Tuple

INITIAL_STATE = (1, 0)
STATE = INITIAL_STATE
Q_TABLE = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

def env(state, action: str) -> Tuple[tuple, float, bool]:

    grid = [[-1, -1],
            [-1, 10]]
    done = False

    new_pos = (0, 0)

    row, col = state
    if action == "top":
        new_pos = (row-1, col)
        if new_pos[0] < 0:
            new_pos = state
    elif action == "down":
        new_pos = (row+1, col)
        if new_pos[0] > 1:
            new_pos = state
    elif action == "left":
        new_pos = (row, col-1)
        if new_pos[1] < 0:
            new_pos = state
    elif action == "right":
        # hard
        if state == (1, 0):
            new_pos = state
        else:
            new_pos = (row, col+1)
            if new_pos[1] > 1:
                new_pos = state

    new_state = new_pos
    reward = grid[new_state[0]][new_state[1]]

    if reward == 10:
        done = True

    return new_state, reward, done

if __name__ == "__main__":
    ep = 4
    actions = ["top", "down", "left", "right"]
    rewards = []
    for i in range(0, ep):
        while True:
            action = np.random.choice(actions)
            new_state, reward, done = env(STATE, action)
            STATE = new_state
            print(f"Ep {i}: state: {new_state}; reward: {reward}; action: {action}")
            rewards.append(reward)
            if done == True:
                STATE = INITIAL_STATE
                sum_reward = sum(rewards)
                print(f"Ep {i}: sum rewards: {sum_reward}")
                rewards.clear()
                print("-------")
                break
