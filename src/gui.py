import pygame, sys
import random
from pygame.locals import *
board = []
row = 10
col = 10
for i in range(0, int(row)):
    board.append([])
    for j in range(0, int(col)):
        board[i].append(0)

board[4][4] = 1
snake = [[0, 2]]
pygame.init()
WINDOW = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake Game')
RED = (0, 0, 0)#black
BLACK = (255, 255, 255)#white
WINDOW.fill(RED)
FPS = 4
fpsClock = pygame.time.Clock()

def draw_board():
    """
      Draws the board
    """
    for i in range(0, row):
        for j in range(0, col):
            if [i, j] == snake[0]:
                pygame.draw.circle(WINDOW, (0, 255, 0), (j*50 + 25, i * 50 + 25), 20)
            elif [i, j] in snake:
                pygame.draw.circle(WINDOW, BLACK, (j*50 + 25, i*50 + 25), 20)
            elif board[i][j] == 1:
                pygame.draw.rect(WINDOW, (255, 255, 255), (j*50 + 10, i*50 + 10, 30, 30))
            else:
                pygame.draw.rect(WINDOW, RED, (j*50, i*50, 50, 50))

def handleEvents():
    keys = pygame.key.get_pressed()
    if keys[K_UP] or keys[K_DOWN] or keys[K_LEFT] or keys[K_RIGHT]:
        current = snake[0]
        new_head = [current[0], current[1]]
        if keys[K_UP]:
            new_head[0] -= 1
        elif keys[K_DOWN]:
            new_head[0] += 1
        elif keys[K_RIGHT]:
            new_head[1] += 1
        elif keys[K_LEFT]:
            new_head[1] -= 1
        if new_head[0] < 0 or new_head[0] > col or new_head[1] < 0 or new_head[1] > row :
            print('Mar Gaya')
            pygame.quit()
            sys.exit()
        if new_head in snake:
            print('Mar Gaya')
            pygame.quit();
            sys.exit()
        snake.insert(0, new_head)
        if board[new_head[0]][new_head[1]] != 1:
            snake.pop()
        if board[new_head[0]][new_head[1]] == 1:
            board[new_head[0]][new_head[1]] = 0
            x = random.randint(0, row - 1)
            y = random.randint(0, col - 1)
            while [x, y] in snake:
                x = random.randint(0, row - 1)
                y = random.randint(0, col - 1)
            board[x][y] = 1
        draw_board()


draw_board()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    handleEvents()
    pygame.display.update()
    fpsClock.tick(FPS)

