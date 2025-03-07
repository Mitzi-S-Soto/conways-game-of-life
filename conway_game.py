"""
A version of Conway's Game of Life
originally based on the code from https://automatetheboringstuff.com/2e/chapter4/

Recreated using PyGame for better visual appeal
Added 'cell' class to keep track of individual cell live/dead state
to color according to alive/still alive/dead/still dead

Alive cells with 2 or 3 Alive neghbors stay Alive (symbol 'o')
Dead cells with 3 Alive neighbors become Alive
All other cells become Dead. (symbol '.')

Cells that are still Alive are Green 'o'
Newly Alive cells are Black 'o'
Newly Dead cells are Red '.'
Cells that are still Dead are '.' White (can't be seen against white background)

Press Spacebar to restart simulation with new pattern

by Kima Prince 2025
"""

import pygame
from pygame.locals import *
import random
import sys
import copy

pygame.init()

font = pygame.font.SysFont("Verdana", 24)

symALIVE = "o"
symDEAD = "."

cALIVE = (0, 0, 0)  # Black
cStillALIVE = (50, 200, 70)  # Green
cDEAD = (255, 0, 0)  # Red
cStillDEAD = (255, 255, 255)  # White

# grid size. Change these to change number of cells. Also changes display's size accordingly
gridHEIGHT = 50
gridWIDTH = 50


def main():
    FPS = 5  # change this number to affect simulation speed
    FramePerSec = pygame.time.Clock()
    nextCells = []
    currentCells = []

    new_cells(nextCells)

    #     GAME LOOP      #
    while True:
        # TEST FOR INPUTS
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_cells(nextCells)

        display.surface.fill((255, 255, 255))
        currentCells = copy.deepcopy(nextCells)
        draw_grid(currentCells)
        living_cells(currentCells, nextCells)

        pygame.display.update()
        FramePerSec.tick(FPS)


class display:
    HEIGHT = gridHEIGHT * 16.25
    WIDTH = gridWIDTH * 16.25
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")


class cell:
    def __init__(self, sym, age_color=cALIVE):
        self.sym = sym
        self.age_color = age_color


def draw_grid(currentCells):
    """Print currentCells on the screen"""
    for y in range(gridHEIGHT):
        for x in range(gridWIDTH):
            write_line = font.render(
                str(currentCells[x][y].sym), True, currentCells[x][y].age_color
            )
            display.surface.blit(write_line, (x * 16, y * 16))


def new_cells(nextCells):
    """Create the starting list of lists for the cells"""
    nextCells.clear()
    for x in range(gridWIDTH):
        column = []
        for y in range(gridHEIGHT):
            if random.randint(0, 5) == 0:
                column.append(cell(symALIVE, cALIVE))
            else:
                column.append(cell(symDEAD, cDEAD))
        nextCells.append(column)


def living_cells(currentCells, nextCells):
    """Calculate the next cells based on current cells
    Accorinding to the rules of Conway's Game of Life"""
    for x in range(gridWIDTH):
        for y in range(gridHEIGHT):
            # Get Neighboring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH-1
            leftCoord = (x - 1) % gridWIDTH
            rightCoord = (x + 1) % gridWIDTH
            aboveCoord = (y - 1) % gridHEIGHT
            belowCoord = (y + 1) % gridHEIGHT
            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord].sym == symALIVE:
                numNeighbors += 1  # Top-left neighbor is alive.
            if currentCells[x][aboveCoord].sym == symALIVE:
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord].sym == symALIVE:
                numNeighbors += 1  # Top-right neighbor is alive.
            if currentCells[leftCoord][y].sym == symALIVE:
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y].sym == symALIVE:
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord].sym == symALIVE:
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord].sym == symALIVE:
                numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord].sym == symALIVE:
                numNeighbors += 1  # Bottom-right neighbor is alive.
            # Set cells new state:
            if currentCells[x][y].sym == symALIVE and (
                numNeighbors == 2 or numNeighbors == 3
            ):
                nextCells[x][y].sym = symALIVE
                nextCells[x][y].age_color = cStillALIVE
            elif currentCells[x][y].sym == symDEAD and numNeighbors == 3:
                nextCells[x][y].sym = symALIVE
                nextCells[x][y].age_color = cALIVE
            elif currentCells[x][y].sym == symDEAD and numNeighbors != 3:
                nextCells[x][y].sym = symDEAD
                nextCells[x][y].age_color = cStillDEAD
            else:
                nextCells[x][y].sym = symDEAD
                nextCells[x][y].age_color = cDEAD


if __name__ == "__main__":
    main()
