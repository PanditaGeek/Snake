import pygame
import time
import random
import copy

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

    def get_rect(self):
        current_rect = pygame.Rect(self.pos_x, self.pos_y, 40, 40)
        return current_rect

    def __str__(self):
        return str(self.pos_x)+","+str(self.pos_y)

#La clase que indica el estado de la comida (si fue comida o no)
class Food(Square):
    is_eaten = False

    def renderer(self,window):
        current_rect = pygame.Rect(self.pos_x, self.pos_y, 40, 40)
        pygame.draw.rect(window, colores["fantasma"], current_rect)

class Wall(Square):

    def __init__(self, x, y):
        super().__init__(x, y)

    def renderer(self,window):
        current_rect = pygame.Rect(self.pos_x, self.pos_y, 40, 40)
        pygame.draw.rect(window, colores["malva"], current_rect)
    

#La clase que indica el estado de la colisión de la serpiente
class SnakeSquare(Square):
    is_collisioned = False

#La clase de la serpiente, su cuerpo, que crezca
class Snake:
    squares_list = []
    current_direction = "Right"

    print(squares_list)

    def __init__(self):
        
        self.squares_list = [SnakeSquare(10,330),SnakeSquare(50,330),SnakeSquare(90,330),SnakeSquare(90,330)]
        self.current_direction = "Right"

    def eat(self):
        square = Square(1,2)
        self.squares_list.append()

    def renderer(self, window):
        for rect in self.squares_list:
            current_rect = pygame.Rect(rect.pos_x, rect.pos_y, 40, 40)
            pygame.draw.rect(window, colores["higado"], current_rect)

    def change_direction(self, direcction):
        self.current_direction = direcction

    def move_head(self):
        if self.current_direction == "Left":
            change_x = -40
            self.squares_list[len(self.squares_list) - 1].pos_x += change_x
        elif self.current_direction == "Right":
            change_x = 40
            self.squares_list[len(self.squares_list) - 1].pos_x += change_x
        if self.current_direction == "Down":
            change_y = 40
            self.squares_list[len(self.squares_list) - 1].pos_y += change_y
        elif self.current_direction == "Up":
            change_y = -40
            self.squares_list[len(self.squares_list) - 1].pos_y += change_y

    def move_body(self):
        body_len = len(self.squares_list) - 1
        for index in range(body_len):
            self.squares_list[index].pos_x = self.squares_list[index + 1].pos_x
            self.squares_list[index].pos_y = self.squares_list[index + 1].pos_y

    def move(self):
        self.move_head()
        self.move_body()

    def collision_checker(self, walls):

        head = self.squares_list[-1]

        for wall in walls:
            collide = pygame.Rect.colliderect(wall.get_rect(),head.get_rect())
            if collide:
                return True

        for index in range(len(self.squares_list) - 2):
            collide = pygame.Rect.colliderect(self.squares_list[index].get_rect(),head.get_rect())
            if collide:
                return True
        return False

    def update(self, food):
        head = self.squares_list[-1]
        collide = pygame.Rect.colliderect(head.get_rect(),food.get_rect())
        if collide:
            food.is_eaten = True
            self.squares_list.append(SnakeSquare(food.pos_x,food.pos_y))

#El diccionario de colores

colores = {
    "verde": (0,128,55),
    "rojo": (255,22,22),
    "turquesa": (64,224,208),
    "negro": (0,0,0),
    "azul": (0,0,255),
    "blanco": (255,255,255),
    "malva": (225,178,255),
    "bordo": (168,33,39),
    "higado": (107,75,62),
    "laton": (196,158,133),
    "naranja_claro": (255,214,175),
    "fantasma": (248,244,249),
    "glicina": (190,167,229)
    }

#Para dibujar la cuadrícula donde jugarás

def dibuja_cuadricula(color1 = colores["naranja_claro"], color2 = colores["laton"]):
    pygame.draw.rect(window, color1, [10, 90, 800, 520], 0)
    for i in range(90, H-10, 40):
        for j in range(10, W-10, 40):
                pygame.draw.rect(window, color2, [j, i, 40, 40], 3)

#Para encontrar el valor máximo de una lista, que servirá para hallar el máximo score

def fin_max(list):
    max = 0
    for x in list:
        if x > max:
            max = x
    return max

#score

type_word = pygame.font.Font('freesansbold.ttf', 20)

def write(str,x,y):
        score_render = type_word.render(str,True, (255,255,255))
        window.blit(score_render,(x,y))

score_p_i_W = 10
score_p_i_H = 10

max_p_i_W = 40
max_p_i_H = 10

#Inicializar la pantalla

window = pygame.display.set_mode((W, H))

#Colocar un icono y el nombre de la ventana

icon_game_i = pygame.image.load("icono.jpg")
icon_game = pygame.transform.scale(icon_game_i, (32, 32))

pygame.display.set_caption("Snake")

pygame.display.set_icon(icon_game)

#Creación de la lista de puntajes

s_scores = []

#Inicializando la primera pantalla del juego

def juego_first():

    Ini_win = True

    click = ""

    while Ini_win:

        #Comprobación de los eventos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Ini_win = False
                Run = False
                Lose_win = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                click = "Sí"
        window.fill(colores["malva"])

        cuadro1 = pygame.draw.rect(window, colores["bordo"], [(W // 2 - 50, H // 2 - 90), (100, 100)], 0)

        if click == "Sí":
            if pygame.Rect.collidepoint(cuadro1, mouse_pos):
                Ini_win = False
                click = "No"
        
        write("¿Empezar", 360, 220)
        write("juego?", 360, 241)

        pygame.display.update()

#Inicializando el juego

def juego_ini():

    snake_i = Snake()
    snake = copy.deepcopy(snake_i)

    Run = True

    direction = ""

    change_x = 0
    change_y = 0

    H_snake = 350
    W_snake = 110

    foods_available = []

    food_posible_x = list(range(10, 800, 40))
    food_posible_y = list(range(90, 600, 40))

    for number in range(1000):
        foods_available.append(Food(random.choice(food_posible_x), random.choice(food_posible_y)))

    walls = []

    walls.append(Wall(10,50))
    walls.append(Wall(50,50))
    walls.append(Wall(90,50))
    walls.append(Wall(130,50))
    walls.append(Wall(170,50))
    walls.append(Wall(210,50))
    walls.append(Wall(250,50))
    walls.append(Wall(290,50))
    walls.append(Wall(330,50))
    walls.append(Wall(370,50))
    walls.append(Wall(410,50))
    walls.append(Wall(450,50))
    walls.append(Wall(490,50))
    walls.append(Wall(530,50))
    walls.append(Wall(570,50))
    walls.append(Wall(610,50))
    walls.append(Wall(650,50))
    walls.append(Wall(690,50))
    walls.append(Wall(730,50))
    walls.append(Wall(770,50))

    walls.append(Wall(10,610))
    walls.append(Wall(50,610))
    walls.append(Wall(90,610))
    walls.append(Wall(130,610))
    walls.append(Wall(170,610))
    walls.append(Wall(210,610))
    walls.append(Wall(250,610))
    walls.append(Wall(290,610))
    walls.append(Wall(330,610))
    walls.append(Wall(370,610))
    walls.append(Wall(410,610))
    walls.append(Wall(450,610))
    walls.append(Wall(490,610))
    walls.append(Wall(530,610))
    walls.append(Wall(570,610))
    walls.append(Wall(610,610))
    walls.append(Wall(650,610))
    walls.append(Wall(690,610))
    walls.append(Wall(730,610))
    walls.append(Wall(770,610))

    walls.append(Wall(-30,50))
    walls.append(Wall(-30,90))
    walls.append(Wall(-30,130))
    walls.append(Wall(-30,170))
    walls.append(Wall(-30,210))
    walls.append(Wall(-30,250))
    walls.append(Wall(-30,290))
    walls.append(Wall(-30,330))
    walls.append(Wall(-30,370))
    walls.append(Wall(-30,410))
    walls.append(Wall(-30,450))
    walls.append(Wall(-30,490))
    walls.append(Wall(-30,530))
    walls.append(Wall(-30,570))
    walls.append(Wall(-30,610))
    walls.append(Wall(-30,650))
    walls.append(Wall(-30,690))
    walls.append(Wall(-30,730))
    walls.append(Wall(-30,770))
    walls.append(Wall(-30,810))

    walls.append(Wall(810,50))
    walls.append(Wall(810,90))
    walls.append(Wall(810,130))
    walls.append(Wall(810,170))
    walls.append(Wall(810,210))
    walls.append(Wall(810,250))
    walls.append(Wall(810,290))
    walls.append(Wall(810,330))
    walls.append(Wall(810,370))
    walls.append(Wall(810,410))
    walls.append(Wall(810,450))
    walls.append(Wall(810,490))
    walls.append(Wall(810,530))
    walls.append(Wall(810,570))
    walls.append(Wall(810,610))
    walls.append(Wall(810,650))
    walls.append(Wall(810,690))
    walls.append(Wall(810,730))
    walls.append(Wall(810,770))
    walls.append(Wall(810,810))


    current_food = foods_available.pop()

    score = 0

    max_score = 0

    while Run:

        snake.update(current_food)

        if current_food.is_eaten:
            current_food = foods_available.pop()
            score += 100

        time.sleep(0.6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    Run = False
                    Lose_win = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != "Right":
                        snake.current_direction = "Left"
                if event.key == pygame.K_RIGHT:
                    if direction != "Left":
                        snake.current_direction = "Right"
                if event.key == pygame.K_DOWN:
                    if direction != "Up":
                        snake.current_direction = "Down"
                if event.key == pygame.K_UP:
                    if direction != "Down":
                        snake.current_direction = "Up"

        window.fill(colores["negro"])

        dibuja_cuadricula()

        snake.renderer(window)

        snake.move()

        write("Score: "+ str(score),score_p_i_W, score_p_i_H)

        current_food.renderer(window)

        for wall in walls:
            wall.renderer(window)

        pygame.display.update()

        if snake.collision_checker(walls):
            Run = False
            snake.squares_list = []

        if Run == False:

            Lose_win = True

            #Inicializando la última pantalla del juego

            def juego_fin():

                lose_wini = pygame.image.load("imagen_Fin_del_Juego.jpg")
                lose_win_im = pygame.transform.scale(lose_wini, (400, 457))

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

                    imagen_fin = window.blit(lose_win_im, (W // 2 - lose_win_im.get_size()[0] // 2, H // 2 - lose_win_im.get_size()[1] // 2))

                    if click == "Sí":
                        if pygame.Rect.collidepoint(imagen_fin, mouse_pos):
                            Lose_win = False
                            juego_ini()

                        click = "No"

                    write("Max score: " + str(fin_max(s_scores)), 335, 195)
                    write("Score: "+ str(score),335, 216)
                    write("¿Jugar de nuevo?", 320, 270)

                    pygame.display.update()

            juego_fin()

juego_first()

juego_ini()