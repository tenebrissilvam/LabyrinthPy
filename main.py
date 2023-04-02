def remove_wall:

def get_neighbours:
def generate(height = 25, width = 25):
    maze = [[0] * width] * height
    for i in range(height):
        for j in range(width):
            if (not(i%2 == 0) and not(j%2 == 0)) and (i < height - 1 and j < width - 1):
                maze[i][j] = cell;
            else:
                maze[i][j] = wall;
def solve():


