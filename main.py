import pygame
import time
import random

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
    if color == "azul":
        return (0,0,255)

def dibuja_cuadricula(color1 = colores("verde"), color2 = colores("rojo")):
    pygame.draw.rect(window, color1, [10, 90, 800, 520], 0)

    contador = 0

    for i in range(90, H-10, 40):
        contador += 1
        if contador % 2 == 0:
            for j in range(10, W-10, 80):
                pygame.draw.rect(window, color2, [j, i, 40, 40], 0)
        else:
            for j in range(50, W-10, 80):
                pygame.draw.rect(window, color2, [j, i, 40, 40], 0)

def dibuja_circulo(coordenadas, radio = 20):
    pygame.draw.circle(window, colores("turquesa"), coordenadas, radio)

class food:
    def __init__(self, window):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, 20, 20))

    def relocate(self):
        self.x = random.randrange(30) * 5
        self.y = random.randrange(30) * 5

#food
class food:
    def __init__(self, window):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, 20, 20))

    def relocate(self):
        self.x = random.randrange(30) * 5
        self.y = random.randrange(30) * 5

def redraw(window):
    comida.draw() 

#score

type_word = pygame.font.Font('freesansbold.ttf', 28)

def write(str,x,y):
        score_render = type_word.render(str,True, (255,255,255))
        window.blit(score_render,(x,y))

score = 0

max_score = 0

score_p_i_W = 10
score_p_i_H = 10

max_p_i_W = 40
max_p_i_H = 10

window = pygame.display.set_mode((W, H))

global comida

comida = food(window)

#icon_game = pygame.image.load("Dragon.png")

pygame.display.set_caption("Snake")

#pygame.display.set_icon(icon_game)

snake_head = pygame.image.load("Head_Right.png")
direction = ""

s_scores = []

change_x = 0
change_y = 0

H_snake = 350
W_snake = 110

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

Run = True

Ini_win = True

Lose_win = True

click = ""

mouse_pos = (-50,-50)

while Ini_win:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Ini_win = False
            Run = False
            Lose_win = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            click = "Sí"
    window.fill(colores("azul"))

    cuadro1 = pygame.draw.rect(window, colores("verde"), [(W // 2 - 50, H // 2), (100, 100)], 0)

    if click == "Sí":
        if pygame.Rect.collidepoint(cuadro1, mouse_pos):
            Ini_win = False
            click = "No"
    pygame.display.update()

while Run:     

    time.sleep(0.6)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                Run = False
                Lose_win = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction != "Right":
                    snake_head = pygame.image.load("Head_Left.png")
                    direction = "Left"
            if event.key == pygame.K_RIGHT:
                if direction != "Left":
                    snake_head = pygame.image.load("Head_Right.png")
                    direction = "Right"
            if event.key == pygame.K_DOWN:
                if direction != "Up":
                    snake_head = pygame.image.load("Head_Down.png")
                    direction = "Down"
            if event.key == pygame.K_UP:
                if direction != "Down":
                    snake_head = pygame.image.load("Head_Up.png")
                    direction = "Up"

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

    dibuja_cuadricula()

    dibuja_circulo([W_snake,H_snake])

    write("Score: "+ str(score),score_p_i_W, score_p_i_H)

    pygame.display.update()

s_scores.append(score)

def fin_max(list):
    max = 0
    for x in list:
        if x > max:
            max = x
    return max

while Lose_win:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            Lose_win = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            click = "Sí"

    if click == "Sí":
        if pygame.Rect.collidepoint(cuadro2, mouse_pos):
            Ini_win = False
            click = "No"

    pygame.draw.rect(window, colores("verde"), [(W // 2 - 250, H // 2 - 250), (500, 500)], 0)

    cuadro2 = pygame.draw.rect(window, colores("negro"), [(W // 2 - 50, H // 2), (100, 100)], 0)

    write("Max score: " + str(fin_max(s_scores)), 300, 200)
    write("Score: "+ str(score),300, 230)

    pygame.display.update()