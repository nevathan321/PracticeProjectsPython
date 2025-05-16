import curses
from curses import wrapper
import queue
import time

# Define the maze as a 2D list
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# Function to print the maze and optionally a path
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)  # Maze color
    RED = curses.color_pair(2)   # Path color

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:  # If this cell is part of the path
                stdscr.addstr(i, j * 2, "X", RED)  # Print 'X' for path
            else:
                stdscr.addstr(i, j * 2, value, BLUE)  # Print maze wall/space

# Function to find the start position in the maze
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j  # Return coordinates of start symbol

# Function to get valid neighbors of a position
def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))  # Right

    return neighbors

# Breadth-first search to find the shortest path
def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)  # Locate start position

    q = queue.Queue()  # Initialize queue for BFS
    q.put((start_pos, [start_pos]))  # Enqueue the start node with path

    visited = set()
    visited.add(start_pos)  # Mark start as visited

    while not q.empty():
        current_pos, path = q.get()  # Get next position and path
        row, col = current_pos

        stdscr.clear()  # Clear screen
        print_maze(maze, stdscr, path)  # Draw maze with current path
        stdscr.refresh()  # Update the screen
        time.sleep(0.1)  # Delay for visualization

        if maze[row][col] == end:  # Check if we reached the goal
            return path

        for neighbor in find_neighbors(maze, row, col):  # Explore neighbors
            if neighbor in visited:
                continue  # Skip visited nodes

            r, c = neighbor
            if maze[r][c] == "#":
                continue  # Skip walls

            new_path = path + [neighbor]  # Append neighbor to path
            q.put((neighbor, new_path))  # Enqueue new path
            visited.add(neighbor)  # Mark as visited

# Main function required by curses
def main(stdscr):
    curses.start_color()  # Initialize color support

    # Define color pairs
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Maze
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Path

    find_path(maze, stdscr)  # Run BFS and draw the result

    stdscr.getch()  # Wait for user input before exiting

# Run the curses app
wrapper(main)