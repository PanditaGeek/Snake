import pygame 
pygame.init()

W = 800
H = 600
window = pygame.display.set_mode((W, H))
#icon_game = pygame.image.load("Dragon.png")
pygame.display.set_caption("Snake")
#pygame.display.set_icon(icon_game)
board = pygame.image.load("Board.jpeg")
snake_head = pygame.image.load("Head_Right.png")
#direction = ""
def head_direction(event,snake_head):
    snake_head == pygame.image.load("Head_Right.png") 
    if event.key == pygame.K_LEFT:
        snake_head = pygame.image.load("Head_Left.png")
    if event.key == pygame.K_RIGHT:
        snake_head = pygame.image.load("Head_Right.png")
    if event.key == pygame.K_DOWN:
        snake_head = pygame.image.load("Head_Down.png")
    if event.key == pygame.K_UP:
        snake_head = pygame.image.load("Head_Up.png")
    return snake_head
change_x = 0
change_y = 0
H = 322
W = 50
change = 0
Run = True
direction = ""
while Run:
    if direction == "Left":
        W -= 0.3  
    if direction == "Right":
        W += 0.3
    if direction == "Up":
        H -= 0.3
    if direction == "Down":
        H += 0.3  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                Run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_head = pygame.image.load("Head_Left.png")
                direction = "Left"
                
            if event.key == pygame.K_RIGHT:
                snake_head = pygame.image.load("Head_Right.png")
                direction = "Right"
               
            if event.key == pygame.K_DOWN:
                direction = "Down"
                snake_head = pygame.image.load("Head_Down.png")
                
            if event.key == pygame.K_UP:
                direction = "Up"
                snake_head = pygame.image.load("Head_Up.png")
                
    window.fill((0,0,0))
    window.blit(board,(-1,82))
    window.blit(snake_head,(W,H))
    pygame.display.update()
    
