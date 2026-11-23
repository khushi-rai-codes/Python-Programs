import random

ROWS = 4
COLS = 4

START = (0, 0)
GOAL = (3, 3)

OBSTACLES = {
    (1, 1),
    (2, 1)
}

ACTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

ALPHA = 0.1
GAMMA = 0.9
EPSILON = 0.2

EPISODES = 5000

random.seed(42)


class QLearningAgent:

    def __init__(self):
        self.q_table = {}

    def get_q(self, state, action):
        return self.q_table.get(
            (state, action), 0.0
        )

    def choose_action(self, state, epsilon):
        if random.random() < epsilon:
            return random.choice(list(ACTIONS))

        return max(
            ACTIONS,
            key=lambda action: self.get_q(state, action)
        )

    def update(self, state, action, reward, next_state):
        old_value = self.get_q(state, action)

        next_best = max(
            self.get_q(next_state, a)
            for a in ACTIONS
        )

        new_value = old_value + ALPHA * (
            reward + GAMMA * next_best - old_value
        )

        self.q_table[(state, action)] = new_value


def move(state, action):
    dr, dc = ACTIONS[action]

    new_state = (
        state[0] + dr,
        state[1] + dc
    )

    if not (
        0 <= new_state[0] < ROWS
        and 0 <= new_state[1] < COLS
    ):
        return state, -5, False

    if new_state in OBSTACLES:
        return state, -5, False

    if new_state == GOAL:
        return new_state, 100, True

    return new_state, -1, False


def train(agent):
    for episode in range(EPISODES):
        state = START

        for _ in range(100):
            action = agent.choose_action(
                state, EPSILON
            )

            next_state, reward, done = move(
                state, action
            )

            agent.update(
                state, action, reward, next_state
            )

            state = next_state

            if done:
                break


def display_path(agent):
    state = START
    visited = {state}

    print("Learned Path:")

    print(state, end="")

    for _ in range(30):
        action = max(
            ACTIONS,
            key=lambda a: agent.get_q(state, a)
        )

        next_state, reward, done = move(
            state, action
        )

        if next_state == state or next_state in visited:
            print("\nPath stopped to avoid a loop.")
            return

        print(" ->", next_state, end="")

        visited.add(next_state)
        state = next_state

        if done:
            print("\nGoal reached!")
            return

    print("\nMaximum path length reached.")


agent = QLearningAgent()

train(agent)

print("Q-Learning Training Completed!")
print("Episodes:", EPISODES)

display_path(agent)
