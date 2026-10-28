from collections import deque
import heapq
import itertools

def neighbors(node, rows, cols):
    r, c = node
    for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
        if 0 <= nr < rows and 0 <= nc < cols:
            yield (nr, nc)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct(parent, goal):
    if goal not in parent:
        return []
    path = [goal]
    while path[-1] in parent and parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    counter = itertools.count()
    frontier = [(manhattan(start, goal), next(counter), start)]
    parent = {start: None}
    g_score = {start: 0}
    explored = []
    closed = set()
    while frontier:
        _, _, current = heapq.heappop(frontier)
        if current in closed:
            continue
        closed.add(current)
        explored.append(current)
        if current == goal:
            return reconstruct(parent, goal), explored
        for nxt in neighbors(current, rows, cols):
            if grid[nxt[0]][nxt[1]] == 1 or nxt in closed:
                continue
            tentative = g_score[current] + 1
            if tentative < g_score.get(nxt, float("inf")):
                parent[nxt] = current
                g_score[nxt] = tentative
                f = tentative + manhattan(nxt, goal)
                heapq.heappush(frontier, (f, next(counter), nxt))
    return [], explored

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    parent = {start: None}
    explored = []
    while queue:
        current = queue.popleft()
        explored.append(current)
        if current == goal:
            return reconstruct(parent, goal), explored
        for nxt in neighbors(current, rows, cols):
            if grid[nxt[0]][nxt[1]] == 1 or nxt in parent:
                continue
            parent[nxt] = current
            queue.append(nxt)
    return [], explored

def greedy_best_first(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    counter = itertools.count()
    frontier = [(manhattan(start, goal), next(counter), start)]
    parent = {start: None}
    visited = set()
    explored = []
    while frontier:
        _, _, current = heapq.heappop(frontier)
        if current in visited:
            continue
        visited.add(current)
        explored.append(current)
        if current == goal:
            return reconstruct(parent, goal), explored
        for nxt in neighbors(current, rows, cols):
            if grid[nxt[0]][nxt[1]] == 1 or nxt in visited or nxt in parent:
                continue
            parent[nxt] = current
            heapq.heappush(frontier, (manhattan(nxt, goal), next(counter), nxt))
    return [], explored
