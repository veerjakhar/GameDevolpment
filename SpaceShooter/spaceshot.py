import pygame

pygame.font.init()

WIDTH = 900
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPACE = pygame.transform.scale(pygame.image.load("Aroura.png"),(WIDTH, HEIGHT))

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

def draw_window():
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

Run = True

while Run:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            pygame.quit()
    draw_window()
