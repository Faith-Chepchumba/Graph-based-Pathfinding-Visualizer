import pygame

from grid import Grid

from dijkstra import dijkstra

from astar import astar

def main(win, width):

grid = Grid(ROWS, width)

run = True

while run:

grid.draw(win)

pygame.display.update()

for event in pygame.event.get():

if event.type == pygame.QUIT:

run = False

*# User interaction for choosing start, goal, walls, etc.*

pygame.quit()

if __name__ == "__main__":

main(WIN, WIDTH)
