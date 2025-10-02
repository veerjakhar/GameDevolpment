import pygame

pygame.font.init()

WIDTH = 900
HEIGHT = 500

VEL = 2

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("!1ST GAME!")

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPACE = pygame.transform.scale(pygame.image.load("Aroura.png"),(WIDTH, HEIGHT))
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

YSM = pygame.image.load("yellowm.png")
RSM = pygame.image.load("redm.png")

YS = pygame.transform.rotate(pygame.transform.scale(YSM, (55, 40)), 90)
RS = pygame.transform.rotate(pygame.transform.scale(RSM, (55, 40)), 270)

def draw_window(red, yellow):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YS, (yellow.x, yellow.y))
    WIN.blit(RS, (red.x, red.y))

def yellowHW(keypress, yellow):
    if keypress[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keypress[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL
    if keypress[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH - 15:
        yellow.x += VEL
    if keypress[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL 

def redHW(keypress, red):
    if keypress[pygame.K_LEFT] and red.x - VEL > 0:
        red.x -= VEL
    if keypress[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL
    if keypress[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH - 15:
        red.x += VEL
    if keypress[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL 

red = pygame.Rect(700, 300, 55, 40)
yellow = pygame.Rect(100, 300, 55, 40)

red_bullets = []
yellow_bullets = []

Run = True

while Run:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            pygame.quit()
    draw_window(red, yellow)

    keypressed = pygame.key.get_pressed()
    yellowHW(keypressed, yellow)
    redHW(keypressed, red)
