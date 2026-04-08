import numpy as np
import random

def train_q_learning(env, episodes=200):
    Q = {}
    actions = env.get_actions()

    def get_q(state, action):
        return Q.get((state, action), 0)

    for _ in range(episodes):
        state = env.start
        steps = 0

        while state != env.goal and steps < 100:  # safety limit
            if random.random() < 0.2:
                action = random.choice(actions)
            else:
                action = max(actions, key=lambda a: get_q(state, a))

            next_state = (state[0]+action[0], state[1]+action[1])

            if not env.is_valid(next_state):
                reward = -10
                next_state = state
            elif next_state == env.goal:
                reward = 100
            else:
                reward = -1

            best_next = max([get_q(next_state, a) for a in actions])
            Q[(state, action)] = get_q(state, action) + 0.1 * (
                reward + 0.9 * best_next - get_q(state, action)
            )

            state = next_state
            steps += 1

    return Q


def get_path_from_q(env, Q):
    state = env.start
    path = [state]
    actions = env.get_actions()

    steps = 0
    while state != env.goal and steps < 50:
        action = max(actions, key=lambda a: Q.get((state, a), 0))
        next_state = (state[0]+action[0], state[1]+action[1])

        # safety check
        if not env.is_valid(next_state):
            break

        state = next_state
        path.append(state)
        steps += 1

    return path