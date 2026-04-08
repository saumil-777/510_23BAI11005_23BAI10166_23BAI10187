import heapq

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {start: 0}

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for d in directions:
            neighbor = (current[0]+d[0], current[1]+d[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    priority = new_cost + heuristic(goal, neighbor)
                    heapq.heappush(open_list, (priority, neighbor))
                    came_from[neighbor] = current

    return []