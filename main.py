import pygame
import time
import random

pygame.init()

W = 820
H = 620

#La clase para los puntos del snake
class Square:
    pos_x = 0
    pos_y = 0
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

#La clase que indica el estado de la comida (si fue comida o no)
class Food(Square):
    is_eated = False

#La clase que indica el estado de la colisión de la serpiente
class SnakeSquare(Square):
    is_collisioned = False

#La clase de la serpiente, su cuerpo, que crezca
class Snake:
    squares_list = []

    def __init__(self, squares_list):
        self.squares_list = squares_list
        self.squares_list.append(SnakeSquare(200, 300))
        self.squares_list.append(SnakeSquare(150, 300))
        self.squares_list.append(SnakeSquare(100, 300))
        self.squares_list.append(SnakeSquare(50, 300))
        self.current_size = 4

    def eat(self):
        ++self.current_size
        square = Square(1,2)
        self.squares_list.append()

    def renderer(self, window):
        for rect in range(self.current_size):
            current_rect = pygame.Rect(200, 500, 50, 50)
            pygame.draw.rect(window, (0,   255,   0), current_rect)

    def change_direction(self, direcction):
        self.current_direction = direcction

    def move_head(self):
        if self.current_direction == "Left":
            change_x = -40
            return change_x
        elif self.current_direction == "Right":
            change_x = 40
            return change_x
        if self.current_direction == "Down":
            change_y = 40
            return change_y
        elif self.current_direction == "Up":
            change_y = -40
            return change_y

    def move_body(self):
        body_len = len(self.squares_list)
        for index in range(body_len):
            self.squares_list[index].pos_x = self.squares_list[index + 1].pos_x
            self.squares_list[index].pos_y = self.squares_list[index + 1].pos_y

    def collision_checker(self):
        pass

#El diccionario de colores

colores = {
    "verde": (0,128,55),
    "rojo": (255,22,22),
    "turquesa": (64,224,208),
    "negro": (0,0,0),
    "azul": (0,0,255),
    "blanco": (255,255,255),
    "malva": (225,178,255),
    "bordo": (168,33,39)
    }

def dibuja_cuadricula(color1 = colores["rojo"], color2 = colores["blanco"]):
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

def fin_max(list):
    max = 0
    for x in list:
        if x > max:
            max = x
    return max

def dibuja_circulo(coordenadas, radio = 20):
    pygame.draw.circle(window, colores["turquesa"], coordenadas, radio)

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

icon_game = pygame.image.load("imagen_icono.png")

pygame.display.set_caption("Snake")

pygame.display.set_icon(icon_game)

s_scores = []

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

def juego_first():

    Ini_win = True

    click = ""

    while Ini_win:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Ini_win = False
                Run = False
                Lose_win = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                click = "Sí"
        window.fill(colores["malva"])

        cuadro1 = pygame.draw.rect(window, colores["bordo"], [(W // 2 - 50, H // 2), (100, 100)], 0)

        if click == "Sí":
            if pygame.Rect.collidepoint(cuadro1, mouse_pos):
                Ini_win = False
                click = "No"
        pygame.display.update()

def juego_ini():

    Run = True

    direction = ""

    change_x = 0
    change_y = 0

    H_snake = 350
    W_snake = 110

    foods_available = []
    for number in range(1000):
        foods_available.append(Food(random.randint(20, 780), random.randint(20, 780)))

    current_food = foods_available.pop()

    while Run:

        if current_food.is_eated:
            current_food = foods_available.pop()

        time.sleep(0.6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    Run = False
                    Lose_win = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != "Right":
                        direction = "Left"
                if event.key == pygame.K_RIGHT:
                    if direction != "Left":
                        direction = "Right"
                if event.key == pygame.K_DOWN:
                    if direction != "Up":
                        direction = "Down"
                if event.key == pygame.K_UP:
                    if direction != "Down":
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

        window.fill(colores["negro"])

        dibuja_cuadricula()

        dibuja_circulo([W_snake,H_snake])

        write("Score: "+ str(score),score_p_i_W, score_p_i_H)

        pygame.display.update()

        if Run == False:

            Lose_win = True

            def juego_fin():

                Lose_win = True

                click = ""

                s_scores.append(score)

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
                            Lose_win = False
                            click = "No"
                            juego_ini()

                    pygame.draw.rect(window, colores["verde"], [(W // 2 - 250, H // 2 - 250), (500, 500)], 0)

                    cuadro2 = pygame.draw.rect(window, colores["negro"], [(W // 2 - 50, H // 2), (100, 100)], 0)

                    write("Max score: " + str(fin_max(s_scores)), 300, 200)
                    write("Score: "+ str(score),300, 230)

                    pygame.display.update()

            juego_fin()

juego_first()

juego_ini()