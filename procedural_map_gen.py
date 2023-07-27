import numpy as np
import pygame
import time

# Set colors 
WALL_COLOR = (50, 50, 50)
GRID_COLOR = (0, 0, 0)
FLOOR_COLOR = (255, 255, 255)
FLOOR_NEXT_COL = (0, 0, 255)

# Set size of screen
WIDTH = 800
HEIGHT = 600

def update(screen, cells, size, with_progress=False):
    # Create temporary matrix of zeros
    temp = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        walls = np.sum(cells[row - 1:row + 2, col-1:col+2]) -   cells[row, col]      
        color = FLOOR_COLOR if cells[row, col] == 0 else WALL_COLOR
        
        #Apply rules (if more than 4 walls create a wall, else a floor)
        if walls > 4:
            temp[row, col] = 1
            if with_progress:
                color = WALL_COLOR  
        else:
            if cells[row, col] == 1:
                if with_progress:
                    color = FLOOR_NEXT_COL
        
        # Draw rectangles, using as backgorund the screen value.
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))   
    
    # Set borders to walls    
    temp[0:int(HEIGHT/CELL_SIZE), 0] = 1
    temp[0, 0:int(WIDTH/CELL_SIZE)] = 1
    temp[0:int(HEIGHT/CELL_SIZE), int(WIDTH/CELL_SIZE) - 1] = 1
    temp[int(HEIGHT/CELL_SIZE) - 1, 0:int(WIDTH/CELL_SIZE)] = 1  
        
    return temp

# Cell visualization settings 
CELL_SIZE = 20

def main():    
    #Initialize pygame
    pygame.init()

    # Set dimension of cells and their initial configuration
    cells = np.random.choice(2, size=(int(HEIGHT/CELL_SIZE), int(WIDTH/CELL_SIZE)), p=[0.38, 0.62])
    cells[0:int(HEIGHT/CELL_SIZE), 0] = 1
    cells[0, 0:int(WIDTH/CELL_SIZE)] = 1
    cells[0:int(HEIGHT/CELL_SIZE), int(WIDTH/CELL_SIZE) - 1] = 1
    cells[int(HEIGHT/CELL_SIZE) - 1, 0:int(WIDTH/CELL_SIZE)] = 1
    
    #Init surface/screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
    # Fill the screen with the grid
    screen.fill(GRID_COLOR)
    
    update(screen, cells, CELL_SIZE)
    
    #Update the full screen
    pygame.display.flip()
    
    # Initialize running as false, so it won't immediately start the game
    running = False
    
    # Create infinite while loop to listen to keys 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # If space key is pressed, change running in true/flase
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running 
                    update(screen, cells, CELL_SIZE)
                    pygame.display.update()                    
    
        if running:
            cells = update(screen, cells, CELL_SIZE, with_progress=True)
            pygame.display.update()
        time.sleep(2)

if __name__ == '__main__':
    main()