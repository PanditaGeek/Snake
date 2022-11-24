import pygame
import time

pygame.init()

W = 820
H = 620

def colores(color):
    if color == "verde":
        return (0,128,55)
    if color == "rojo":
        return (255,22,22)
    if color == "turquesa":
        return (64,224,208)
    if color == "negro":
        return (0,0,0)

window = pygame.display.set_mode((W, H))

#icon_game = pygame.image.load("Dragon.png")

pygame.display.set_caption("Snake")

#pygame.display.set_icon(icon_game)
#board_w = pygame.image.load("Fondo.png")
#board = pygame.transform.scale(board_w, (800,600))

snake_head = pygame.image.load("Head_Right.png")
direction = ""

change_x = 0
change_y = 0

H_snake = 350
W_snake = 110

Run = True

def movement_x(direction):
    if direction == "Left":
        change_x = -40
        return change_x
    elif direction == "Right":
        change_x = 40
        return change_x
    return 0

def movement_y(direction):
    if direction == "Down":
        change_y = 40
        return change_y
    elif direction == "Up":
        change_y = -40
        return change_y
    return 0
class fruits:
    def __init__(self, buff, fruit):
        self.buff = buff
        self.fruit = fruit

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                Run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "Right":
                snake_head = pygame.image.load("Head_Left.png")
                direction = "Left"
            if event.key == pygame.K_RIGHT and direction != "Left":
                snake_head = pygame.image.load("Head_Right.png")
                direction = "Right"
            if event.key == pygame.K_DOWN and direction != "Up":
                snake_head = pygame.image.load("Head_Down.png")
                direction = "Down"
            if event.key == pygame.K_UP  and direction != "Down":
                snake_head = pygame.image.load("Head_Up.png")
                direction = "Up"
    
    time.sleep(0.6)

    change_x = movement_x(direction)
    change_y = movement_y(direction)

    H_snake += change_y
    W_snake += change_x

    if H_snake <= 90:
        H_snake = 110
        Run = False
    elif H_snake >= H - 10:
        H_snake = H - 20 - 10
        Run = False
    if W_snake <= 10:
        W_snake = 30
        Run = False
    elif W_snake >= W - 10:
        W_snake = W - 20 - 10
        Run = False

    window.fill(colores("negro"))

    pygame.draw.rect(window, colores("verde"), [10, 90, 800, 520], 0)

    contador = 0

    for i in range(90, H-10, 40):
        contador += 1
        if contador % 2 == 0:
            for j in range(10, W-10, 80):
                pygame.draw.rect(window, colores("rojo"), [j, i, 40, 40], 0)
        else:
            for j in range(50, W-10, 80):
                pygame.draw.rect(window, colores("rojo"), [j, i, 40, 40], 0)

    #window.blit(board,(10,10))
    pygame.draw.circle(window, colores("turquesa"),[W_snake,H_snake],20)
    #window.blit(snake_head,(W_snake,H_snake))
    pygame.display.update()
    
