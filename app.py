import time
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from algorithms import astar, bfs, greedy_best_first

st.set_page_config(page_title="AISC Smart Path Finder", page_icon="🧭", layout="wide")
st.title("🧭 AI Smart Path Finder")
st.caption("Artificial Intelligence and Soft Computing (CSE3121) — Heuristic Search Demonstration")
st.markdown("""
This interactive demo compares **A\***, **Breadth-First Search (BFS)**, and **Greedy Best-First Search** on a grid.
A* evaluates each cell using **f(n) = g(n) + h(n)**, where `g(n)` is the cost so far and `h(n)` is Manhattan distance to the goal.
""")

with st.sidebar:
    st.header("Grid settings")
    rows = st.slider("Rows", 8, 25, 15)
    cols = st.slider("Columns", 8, 25, 15)
    density = st.slider("Random obstacle density (%)", 0, 40, 22, 1)
    seed = st.number_input("Random seed", min_value=0, max_value=99999, value=7)
    algorithm_name = st.selectbox("Algorithm", ["A*", "BFS", "Greedy Best-First"])
    st.markdown("**Legend**: 🟩 Start · 🟥 Goal · ⬛ Wall · 🟦 Path · 🟨 Explored")

import random
random.seed(int(seed))
start = (0, 0)
goal = (rows - 1, cols - 1)
grid = [[0 for _ in range(cols)] for _ in range(rows)]
for r in range(rows):
    for c in range(cols):
        if (r, c) not in (start, goal) and random.random() < density / 100:
            grid[r][c] = 1

c1, c2 = st.columns([1, 1])
with c1:
    st.subheader("Generated grid")
    st.write("Change the seed or obstacle density in the sidebar to generate another maze.")
    fig, ax = plt.subplots(figsize=(7, 6))
    # 0 empty, 1 wall
    img = [[1 if grid[r][c] else 0 for c in range(cols)] for r in range(rows)]
    cmap = ListedColormap(["white", "#252a34"])
    ax.imshow(img, cmap=cmap, vmin=0, vmax=1)
    ax.scatter(start[1], start[0], c="#2ca25f", s=150, marker="s", label="Start")
    ax.scatter(goal[1], goal[0], c="#de2d26", s=150, marker="s", label="Goal")
    ax.set_xticks(range(cols)); ax.set_yticks(range(rows))
    ax.set_xticklabels([]); ax.set_yticklabels([])
    ax.grid(which="major", color="#aab2bd", linewidth=.5)
    ax.set_xlim(-.5, cols-.5); ax.set_ylim(rows-.5, -.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=2)
    st.pyplot(fig)
    plt.close(fig)

algo_map = {"A*": astar, "BFS": bfs, "Greedy Best-First": greedy_best_first}
if st.button("🚀 Find path", type="primary", use_container_width=True):
    t0 = time.perf_counter()
    path, explored = algo_map[algorithm_name](grid, start, goal)
    elapsed_ms = (time.perf_counter() - t0) * 1000
    with c2:
        st.subheader("Search result")
        if path:
            st.success(f"Path found using {algorithm_name}!")
            st.metric("Path length (moves)", len(path) - 1)
        else:
            st.error("No path found. Try reducing obstacle density or changing the seed.")
        m1, m2 = st.columns(2)
        m1.metric("Explored cells", len(explored))
        m2.metric("Execution time", f"{elapsed_ms:.3f} ms")
        # 0 free, 1 wall, 2 explored, 3 path
        view = [[1 if grid[r][c] else 0 for c in range(cols)] for r in range(rows)]
        for r, c in explored:
            if (r, c) not in (start, goal) and not grid[r][c]:
                view[r][c] = 2
        for r, c in path:
            if (r, c) not in (start, goal):
                view[r][c] = 3
        cmap2 = ListedColormap(["white", "#252a34", "#ffe082", "#42a5f5"])
        fig2, ax2 = plt.subplots(figsize=(7, 6))
        ax2.imshow(view, cmap=cmap2, vmin=0, vmax=3)
        ax2.scatter(start[1], start[0], c="#2ca25f", s=150, marker="s", label="Start")
        ax2.scatter(goal[1], goal[0], c="#de2d26", s=150, marker="s", label="Goal")
        ax2.set_xticks(range(cols)); ax2.set_yticks(range(rows))
        ax2.set_xticklabels([]); ax2.set_yticklabels([])
        ax2.grid(which="major", color="#aab2bd", linewidth=.5)
        ax2.set_xlim(-.5, cols-.5); ax2.set_ylim(rows-.5, -.5)
        ax2.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=2)
        st.pyplot(fig2)
        plt.close(fig2)
        st.caption("Yellow cells were explored; blue cells form the returned path.")
else:
    with c2:
        st.subheader("How to use")
        st.markdown("""
        1. Choose grid size and obstacle density in the sidebar.
        2. Select A*, BFS, or Greedy Best-First.
        3. Click **Find path**.
        4. Compare explored cells and path length across algorithms.

        The start is fixed at the top-left and the goal at the bottom-right.
        """)

with st.expander("Algorithm notes and limitations"):
    st.markdown("""
    - **A\***: prioritizes `f(n) = g(n) + h(n)`. With unit-cost four-direction movement and Manhattan distance, it finds an optimal path.
    - **BFS**: explores by distance from the start and finds a shortest path when every move has equal cost.
    - **Greedy Best-First**: prioritizes only `h(n)`; it can be faster in some cases but does not guarantee the shortest path.
    - This is a grid simulation, not a physical navigation system. Runtime measurements are machine- and run-dependent.
    """)
st.divider()
st.caption("CWS project prototype • AISC CSE3121 • Built with Python and Streamlit")
