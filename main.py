from environment import GridWorld
from astar import astar
from dqn import train_q_learning, get_path_from_q
from utils import print_grid
import time

env = GridWorld()

# --- A* ---
start_time = time.time()
astar_path = astar(env.grid, env.start, env.goal)
astar_time = time.time() - start_time

# --- Q-Learning ---
start_time = time.time()
Q = train_q_learning(env)
q_path = get_path_from_q(env, Q)
q_time = time.time() - start_time

# --- Results ---
print("A* Path:", astar_path)
print("A* Length:", len(astar_path))

print("\nQ-Learning Path:", q_path)
print("Q-Learning Length:", len(q_path))

# --- Comparison ---
print("\n--- COMPARISON ---")
print(f"A* Path Length: {len(astar_path)}")
print(f"Q-Learning Path Length: {len(q_path)}")

if len(astar_path) < len(q_path):
    print("A* is more optimal")
elif len(astar_path) > len(q_path):
    print("Q-Learning performed better")
else:
    print("Both performed equally")

# --- Time Comparison ---
print(f"\nA* Time: {astar_time:.5f}s")
print(f"Q-Learning Time: {q_time:.5f}s")

# --- Hybrid Decision ---
if len(astar_path) <= len(q_path):
    final_path = astar_path
    print("\nHybrid chose A* path")
else:
    final_path = q_path
    print("\nHybrid chose Q-Learning path")

# --- Visualization ---
print("\nA* Grid:")
print_grid(env.grid, astar_path)

print("\nQ-Learning Grid:")
print_grid(env.grid, q_path)