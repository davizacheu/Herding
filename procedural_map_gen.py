import numpy as np
import pygame
import time
from landparcel import LandParcel

# Set colors 
WALL_COLOR = (50, 50, 50)
GRID_COLOR = (0, 0, 0)
FLOOR_COLOR = (255, 255, 255)
FLOOR_NEXT_COL = (0, 0, 255)

# Set size of screen
WIDTH = 1600
HEIGHT = 900


def procedural_update(screen, cells, size, with_progress=False):
    # Create temporary matrix of zeros
    temp = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        walls = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        color = FLOOR_COLOR if cells[row, col] == 0 else WALL_COLOR

        # Apply rules (if more than 4 walls create a wall, else a floor)
        if walls > 4:
            temp[row, col] = 1
            if with_progress:
                color = WALL_COLOR
        else:
            if cells[row, col] == 1:
                if with_progress:
                    color = FLOOR_NEXT_COL

        # Draw rectangles, using as background the screen value.
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return temp


# Cell visualization settings
CELL_SIZE = 4


def main():
    # Initialize pygame
    pygame.init()

    # Set dimension of cells and their initial configuration
    cells = np.random.choice(2, size=(int(HEIGHT / CELL_SIZE), int(WIDTH / CELL_SIZE)), p=[0.55, 0.45])

    # Init surface/screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Fill the screen with the grid
    screen.fill(GRID_COLOR)

    procedural_update(screen, cells, CELL_SIZE)

    # Update the full screen
    pygame.display.flip()

    # Initialize running_procedural and running_model as false, so it won't immediately start the game
    running_procedural = False
    running_model = False

    # Create infinite while loop to listen to keys 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # If space key is pressed, change running in true/false
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not running_model:
                    running_procedural = not running_procedural
                    procedural_update(screen, cells, CELL_SIZE)
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    running_model = True
                    initialize_world(screen, cells, CELL_SIZE)
                    pygame.display.update()
        if running_procedural and not running_model:
            cells = procedural_update(screen, cells, CELL_SIZE, with_progress=True)
            pygame.display.update()
        time.sleep(.5)


if __name__ == '__main__':
    main()
