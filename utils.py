def print_grid(grid, path):
    grid_copy = grid.copy()

    for (x, y) in path:
        grid_copy[x][y] = 9  # mark path

    print("\nGrid (9 = path):")
    for row in grid_copy:
        print(row)