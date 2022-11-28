import pygame
import random

class Square:
    pos_x = 0
    post_y = 0
    def __init__(self, x, y):
        self.pos_x = x
        self.post_y = y

class Food(Square):
    is_eated = False

class SnakeSquare(Square):
    is_collisioned = False

foods_available = []
for number in range(1000):
    foods_available.append(Food(random.randint(20, 780), random.randint(20, 780)))

current_food = foods_available.pop()
while True:
    if(current_food.is_eated):
        current_food = foods_available.pop()

class Snake:
    current_size = 4
    squares_list = []

    def __init__(self):
        self.squares_list.append(SnakeSquare(200, 300))
        self.squares_list.append(SnakeSquare(150, 300))
        self.squares_list.append(SnakeSquare(100, 300))
        self.squares_list.append(SnakeSquare(50, 300))


    def eat(self):
        ++self.current_size
        square = Square(1,2)
        self.squares_list.append()

    def renderer(self, window):
        for rect in range(self.current_size):
            current_rect = Rect(200, 500, 50, 50)
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