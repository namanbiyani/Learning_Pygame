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
COL = 10
FPS = 4
#COLOR  ( R ,  G ,  B )
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
def draw_board(board, snake):
    """
        Draws the board
    """
    for i in range(0, ROW):
        for j in range(0, COL):
            if [i, j] == snake[0]:
                pygame.draw.circle(WINDOW, GREEN, (j * 50 + 25, i * 50 + 25), 20)
            elif [i, j] in snake:
                pygame.draw.circle(WINDOW, WHITE, (j * 50 + 25, i * 50 + 25), 20)
            elif board[i][j] == 1:
                pygame.draw.rect(WINDOW, BLUE, (j * 50 + 10, i * 50 + 10, 30, 30))
            else:
                pygame.draw.rect(WINDOW, BLACK, (j * 50, i * 50, 50, 50))

def handle_events(board, snake):
    """
        Handles Key Events
    """
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
        if new_head[0] < 0 or new_head[0] > COL or new_head[1] < 0 or new_head[1] > ROW :
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
            x = random.randint(0, ROW - 1)
            y = random.randint(0, COL - 1)
            while [x, y] in snake:
                x = random.randint(0, ROW - 1)
                y = random.randint(0, COL - 1)
            board[x][y] = 1
        draw_board(board, snake)



def main():
    """
        Main Function for all the code
    """
    board = []
    for i in range(0, int(ROW)):
        board.append([])
        for j in range(0, int(COL)):
            board[i].append(0)

    board[4][4] = 1
    snake = [[0, 2]]
    pygame.init()
    global WINDOW
    WINDOW = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Snake Game')
    WINDOW.fill(BLACK)
    fps_clock = pygame.time.Clock()
    draw_board(board, snake)

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
                    if event.key == K_UP:
                        new_head[0] -= 1
                    elif event.key == K_DOWN:
                        new_head[0] += 1
                    elif event.key == K_RIGHT:
                        new_head[1] += 1
                    elif event.key == K_LEFT:
                        new_head[1] -= 1
                    if new_head[0] < 0 or new_head[0] > COL or new_head[1] < 0 or new_head[1] > ROW :
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
                        x = random.randint(0, ROW - 1)
                        y = random.randint(0, COL - 1)
                        while [x, y] in snake:
                            x = random.randint(0, ROW - 1)
                            y = random.randint(0, COL - 1)
                        board[x][y] = 1
                    draw_board(board, snake)
                    handled = True
        if not handled:
            handle_events(board, snake)
        pygame.display.update()
        fps_clock.tick(FPS)


if __name__ == '__main__':
    main()
