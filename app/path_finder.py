import heapq

def heuristic(a, b):
    """Эвристика Манхэттенского расстояния."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(grid, node):
    """Возвращает соседей узла, которые проходимы."""
    x, y = node
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # Соседи по 4 направлениям
    valid = []
    for nx, ny in candidates:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):  # Проверка на выход за пределы
            if grid[nx][ny] == 0:  # 0 — проходимая клетка
                valid.append((nx, ny))
    return valid

def find_path(grid, start, goal):
    """Алгоритм A* для поиска пути."""
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))

    g_costs = {start: 0}
    
    visited = set()

    while open_set:
        est_total_cost, cost_so_far, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor in neighbors(grid, current):
            new_cost = cost_so_far + 1
            if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                est = new_cost + heuristic(neighbor, goal)  # f = g + h
                heapq.heappush(open_set, (est, new_cost, neighbor, path + [neighbor]))

    return []