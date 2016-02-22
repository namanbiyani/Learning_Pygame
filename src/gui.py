"""
  GUI for snake
  Author: Yash Srivastav
  Date  : 23/02/2016
"""
import pygame, sys
import random
from pygame.locals import *

WINDOW = None
ROW = 10
COL = 20
FPS = 4
#COLOR  ( R ,  G ,  B )
BLACK = (33, 33, 33)
WHITE = (207, 216, 220)
GREEN = (27, 94, 32)
BLUE = (255, 193, 7)
DIR = 'R'
DIRTY = []
def draw_board(board, snake):
    """
        Draws the board
    """
    for i in range(0, ROW):
        for j in range(0, COL):
            if [i, j] == snake[0]:
                pygame.draw.rect(WINDOW, BLACK, (j * 50, i * 50, 50, 50))
                pygame.draw.circle(WINDOW, GREEN, (j * 50 + 25, i * 50 + 25), 20)
                if DIR == 'R':
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 35, i * 50 + 15), 3)
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 35, i * 50 + 35), 3)
                elif DIR == 'L':
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 15, i * 50 + 15), 3)
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 15, i * 50 + 35), 3)
                elif DIR == 'D':
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 15, i * 50 + 35), 3)
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 35, i * 50 + 35), 3)
                elif DIR == 'U':
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 15, i * 50 + 15), 3)
                    pygame.draw.circle(WINDOW, BLACK, (j * 50 + 35, i * 50 + 15), 3)
            elif [i, j] in snake:
                pygame.draw.circle(WINDOW, WHITE, (j * 50 + 25, i * 50 + 25), 20)
            elif board[i][j] == 1:
                pygame.draw.rect(WINDOW, BLUE, (j * 50 + 10, i * 50 + 10, 30, 30))
            else:
                pygame.draw.rect(WINDOW, BLACK, (j * 50, i * 50, 50, 50))

def generate_food(board, snake):
    """
        Generates food in a random location
    """
    x = random.randint(0, ROW - 1)
    y = random.randint(0, COL - 1)
    while [x, y] in snake:
        x = random.randint(0, ROW - 1)
        y = random.randint(0, COL - 1)
    board[x][y] = 1
    DIRTY.append(Rect(y * 50, x * 50, 50, 50))

def move_snake(board, snake, direction):
    """
        Moves Snake
    """
    new_head = [snake[0][0], snake[0][1]]
    if direction == 'U':
        new_head[0] -= 1
    elif direction == 'D':
        new_head[0] += 1
    elif direction == 'R':
        new_head[1] += 1
    elif direction == 'L':
        new_head[1] -= 1
    if new_head[0] < 0 or new_head[0] >= ROW or new_head[1] < 0 or new_head[1] >= COL :
        # print('Mar Gaya')
        # pygame.quit()
        # sys.exit()
        new_head[0] = new_head[0] % ROW
        new_head[1] = new_head[1] % COL
    if new_head in snake:
        print('Mar Gaya!!',' Score = ',len(snake) * (1 + (len(snake)//5)))
        pygame.quit();
        sys.exit()
    snake.insert(0, new_head)
    DIRTY.append(Rect(new_head[1] * 50, new_head[0] * 50, 50, 50))
    if board[new_head[0]][new_head[1]] != 1:
        k = snake.pop()
        DIRTY.append(Rect(k[1] * 50, k[0] * 50, 50, 50))
    if board[new_head[0]][new_head[1]] == 1:
        board[new_head[0]][new_head[1]] = 0
        generate_food(board, snake)
    draw_board(board, snake)


def handle_events(board, snake):
    """
        Handles Key Events
    """
    keys = pygame.key.get_pressed()
    if keys[K_UP] or keys[K_DOWN] or keys[K_LEFT] or keys[K_RIGHT]:
        if keys[K_UP]:
            move_snake(board, snake, 'U')
        elif keys[K_DOWN]:
            move_snake(board, snake, 'D')
        elif keys[K_RIGHT]:
            move_snake(board, snake, 'R')
        elif keys[K_LEFT]:
            move_snake(board, snake, 'L')


def main():
    """
        Main Function for all the code
    """
    board = []
    for i in range(0, int(ROW)):
        board.append([])
        for j in range(0, int(COL)):
            board[i].append(0)

    snake = [[random.randint(0, ROW - 1), random.randint(0, COL -1)]]
    pygame.init()
    global WINDOW
    global DIR
    global FPS
    DIR = random.choice(['U', 'D', 'R', 'L'])
    WINDOW = pygame.display.set_mode((COL * 50, ROW * 50))
    pygame.display.set_caption('Snake Game')
    WINDOW.fill(BLACK)
    fps_clock = pygame.time.Clock()
    generate_food(board, snake)
    draw_board(board, snake)
    pygame.display.update()

    while True:
        handled = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_DOWN, K_LEFT, K_RIGHT):
                    current = snake[0]
                    new_head = [current[0], current[1]]
                    if event.key == K_UP and not DIR == 'D':
                        DIR = 'U'
                        move_snake(board, snake, 'U')
                    elif event.key == K_DOWN and not DIR == 'U':
                        DIR = 'D'
                        move_snake(board, snake, 'D')
                    elif event.key == K_RIGHT and not DIR == 'L':
                        DIR = 'R'
                        move_snake(board, snake, 'R')
                    elif event.key == K_LEFT and not DIR == 'R':
                        DIR = 'L'
                        move_snake(board, snake, 'L')
                    handled = True
                    pygame.display.update(DIRTY)
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()
        if not handled:
            move_snake(board, snake, DIR)
        pygame.display.update(DIRTY)
        fps_clock.tick(FPS)
        FPS = 4 + len(snake)//5

if __name__ == '__main__':
    main()
