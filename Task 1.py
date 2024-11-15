import numpy as np
import random
from PIL import Image

# Load and process the maze image
def load_maze_image(image_path, scale_factor=0.50):
    image = Image.open(image_path).convert('L')  
    # Scale down the image
    scaled_size = (int(image.width * scale_factor), int(image.height * scale_factor))
    image = image.resize(scaled_size, Image.LANCZOS)
    maze_array = np.array(image)
    # Threshold the grayscale image to binary
    binary_maze = np.where(maze_array > 128, 0, 1)  # 0 = path, 1 = wall
    return binary_maze

# Automatically detect the start and end points
def detect_start_end(maze):
    # Start point (first path cell at the top row)
    start_x = np.where(maze[0] == 0)[0][0]
    start = (0, start_x)

    # End point (first path cell at the bottom row)
    end_x = np.where(maze[-1] == 0)[0][0]
    end = (maze.shape[0] - 1, end_x)
    return start, end

# Visualizer to show the maze as 0s and 1s
def display_maze(maze, path=None):
    display_maze = maze.copy()
    if path:
        for (x, y) in path:
            display_maze[x, y] = 2  
    for row in display_maze:
        print("".join(["0" if cell == 0 else "1" if cell == 1 else "*" for cell in row]))

# Backtracking algorithm (DFS)
def solve_maze_backtracking(maze, start, end):
    path = []
    visited = set()

    def dfs(position):
        if position == end:
            path.append(position)
            return True
        if position in visited:
            return False
        visited.add(position)
        x, y = position
        path.append(position)

        # Move orthogonally
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx, ny] == 0:
                if dfs((nx, ny)):
                    return True

        path.pop()  # Backtrack
        return False

    dfs(start)
    return path

# Las Vegas algorithm (Random Walk with step limit)
def solve_maze_las_vegas(maze, start, end, step_limit=400):
    position = start
    path = [position]
    visited = set()
    steps = 0

    while position != end and steps < step_limit:
        visited.add(position)
        x, y = position
        options = []

        # Orthogonal moves
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx, ny] == 0 and (nx, ny) not in visited:
                options.append((nx, ny))

        if options:
            position = random.choice(options)
            path.append(position)
        else:
            # Dead end, randomly go back in path
            position = random.choice(path)
        
        steps += 1

    return path if position == end else None

# Main code
image_path = 'maze-2.png'
maze = load_maze_image(image_path, scale_factor=0.25)
start, end = detect_start_end(maze)

# Display the maze with start and end points
print("Maze (0 = path, 1 = wall):")
display_maze(maze)
print(f"Start: {start}, End: {end}")

# Choose algorithm
algorithm = input("Choose algorithm (backtracking/las_vegas): ").strip().lower()
if algorithm == "backtracking":
    path = solve_maze_backtracking(maze, start, end)
elif algorithm == "las_vegas":
    path = solve_maze_las_vegas(maze, start, end)
else:
    print("Invalid algorithm choice.")
    path = None

# Display result
if path:
    print("Path found:")
    display_maze(maze, path)
else:
    print("No path found within step limit.")
