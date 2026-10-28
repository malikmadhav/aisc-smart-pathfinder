# AI Smart Path Finder — AISC CSE3121 CWS

An interactive demonstration of heuristic and uninformed search algorithms.

## Algorithms
- A* Search: `f(n) = g(n) + h(n)` with Manhattan distance.
- Breadth-First Search (BFS): shortest path for equal-cost moves.
- Greedy Best-First Search: prioritizes the heuristic and is not guaranteed optimal.

## Run locally
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy with Streamlit Community Cloud
1. Upload these project files to a GitHub repository.
2. Go to https://share.streamlit.io/ and sign in with GitHub.
3. Create an app from your repository, select `app.py`, and deploy.
4. Open the generated public URL and test the app.

## Project overview
The app generates a grid with random obstacles, fixes the start at the top-left and goal at the bottom-right, and visualizes the selected algorithm's explored cells and path. It reports path length, explored cells, and execution time.

## Testing checklist
- Run with 0% obstacle density.
- Test several random seeds.
- Increase obstacle density and check no-path handling.
- Compare A* and BFS path lengths on the same grid.
- Confirm Greedy Best-First may return a non-optimal path.

## Limitations
This is an educational grid simulation. The start and goal are fixed corners, obstacles are randomly generated, and performance timings vary by machine and run.
