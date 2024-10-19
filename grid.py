import pygame

WIDTH, HEIGHT = 800, 800

ROWS = 50

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Grid:

def __init__(self, rows, width):

self.rows = rows

self.width = width

self.grid = [[0 for _ in range(rows)] for _ in range(rows)]

def draw_grid(self, win):

gap = self.width // self.rows

for i in range(self.rows):

pygame.draw.line(win, (128, 128, 128), (0, i * gap), (self.width, i * gap))

pygame.draw.line(win, (128, 128, 128), (i * gap, 0), (i * gap, self.width))

def draw(self, win):

for row in self.grid:

for cell in row:

pygame.draw.rect(win, (255, 255, 255), (cell.x, cell.y, cell.width, cell.width))

self.draw_grid(win)
