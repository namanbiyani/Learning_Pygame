import pygame, sys
from pygame.locals import *
board = []
row = 10
col = 10
for i in range(0,int(row)):
    board.append([])
    for j in range(0,int(col)):
        board[i].append(0)

board[4][4]=1
snake = [[0,2]]
pygame.init()
WINDOW = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake Game')
RED = (0,0,0)#black
BLACK = (255,255,255)#white
WINDOW.fill(RED)

def draw_board():
    for i in range(0,row):
        for j in range(0,col):
            if [i,j] == snake[0]:
                pygame.draw.circle(WINDOW,(0,255,0),(j*50 + 25,i*50 + 25),20)
            elif [i,j] in snake:
                pygame.draw.circle(WINDOW,BLACK,(j*50 + 25,i*50 + 25),20)
            elif board[i][j] == 1:
                pygame.draw.rect(WINDOW,(255,255,255),(j*50 + 10, i*50 + 10,30,30))
            else:
                pygame.draw.rect(WINDOW,RED,(j*50,i*50,50,50))
            for j in range(0,500):
                pygame.draw.line(WINDOW,BLACK,(0,5+i*10),(500,5+i*10))
                
draw_board()
while True:
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            #print(event.key,K_UP)
            if event.key in (K_UP,K_DOWN,K_RIGHT,K_LEFT):
                current = snake[0]
                new_head = [current[0],current[1]]
                if event.key == K_UP:
                    new_head[0] -= 1 
                elif event.key == K_DOWN:
                    new_head[0] += 1
                elif event.key == K_RIGHT:
                    new_head[1] += 1
                elif event.key == K_LEFT:
                    new_head[1] -= 1
                if(new_head[0] < 0 or new_head[0] > int(col) or new_head[1] < 0 or new_head[1] > int(row)):
                    print("chutiye bancho out kara diya")
                    exit(0)
                if new_head in snake:
                    print("tu ja re tujhe ni aata khelna")
                    exit(0) 
                snake.insert(0,new_head)
                if(board[new_head[0]][new_head[1]] != 1):
                    snake.pop()
                if(board[new_head[0]][new_head[1]] == 1):
                    board[new_head[0]][new_head[1]] = 0

                draw_board()                
    pygame.display.update()