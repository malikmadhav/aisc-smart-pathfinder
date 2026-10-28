# AI Smart Path Finder Using A* Search

## 1. Abstract
This project demonstrates AI search techniques by finding a route through a grid containing obstacles. It implements A* Search, Breadth-First Search (BFS), and Greedy Best-First Search and visualizes explored cells and the resulting path in a Streamlit web interface.

## 2. Problem Statement
Given a two-dimensional grid, a start cell, a goal cell, and blocked cells, find a valid route from start to goal while avoiding obstacles. For equal-cost four-directional moves, A* should find a shortest route when using Manhattan distance.

## 3. Objectives
- Implement heuristic search using A*.
- Compare A* with BFS and Greedy Best-First Search.
- Visualize explored cells and the returned path.
- Measure path length, explored cells, and execution time.

## 4. Methodology
Each cell is a state. Valid actions move up, down, left, or right, provided the next cell is within the grid and not blocked. The goal test checks whether the current cell equals the destination.

A* uses:
- g(n): cost from the start to n.
- h(n): Manhattan distance from n to the goal.
- f(n) = g(n) + h(n).

For a grid with four-directional unit-cost moves, Manhattan distance is an admissible heuristic. BFS is used as a shortest-path baseline. Greedy Best-First Search uses only the heuristic and does not guarantee optimality.

## 5. Tools and Technologies
- Python
- Streamlit for the interface
- Matplotlib for grid visualization
- Heap-based priority queues and a FIFO queue for search

## 6. System Design
The Streamlit UI generates the grid and collects parameters. The algorithms module searches the grid and returns the route and explored states. The UI visualizes the result and displays metrics.

## 7. Testing and Evaluation
Test on empty grids, grids with obstacles, and grids where no route exists. Compare the same generated grid across algorithms. Record path length, explored cells, and execution time. Do not claim experimental results until they have been obtained by running the application.

## 8. Results
Fill this section after running the app and recording your own measurements:
- Grid dimensions:
- Obstacle density:
- Algorithm:
- Path length:
- Explored cells:
- Execution time:
- Observations:

## 9. Limitations
The grid and endpoints are simplified; obstacles are randomly generated; performance measurements vary by machine; and the prototype is not a real-world navigation system.

## 10. Conclusion
The prototype illustrates how informed and uninformed search algorithms solve a pathfinding problem. A* combines the cost already incurred with an estimate of remaining cost, while BFS explores by depth and Greedy Best-First prioritizes the estimated distance to the goal.

## 11. Future Scope
Add manual obstacle placement, step-by-step animation, diagonal movement, weighted terrain, and exportable comparison charts.
