import pygame
import random
pygame.init()
W=800
H=600
windonw= pygame.display.set_mode((W,H))
icon_juego= pygame.image.load("Dragon.jpeg")
pygame.display.set_icon(icon_juego)
pygame.display.set_caption("Snake")
board= pygame.image.load("Board.jpeg")   
#apple
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
    score=0
    type_word=pygame.font.Font('freesansbold.ttf', 28)
    word_p_i_W=10
    word_p_i_H=10

    def show_score(x,y):
        score_render = type_word.render("Score: "+ str(score),True, (255,255,255))
        windonw.blit(score_render,(x,y))
    show_score(word_p_i_W, word_p_i_H)
    pygame.display.update()

global comida
comida=food(windonw)
correr=True
while correr:
    for evento in pygame.event.get():
        if evento.type== pygame.QUIT:
            correr = False
    windonw.blit(board,(0,0)) 
    redraw(windonw)
    pygame.display.update()

    
    
