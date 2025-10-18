import pygame
import os

pygame.font.init()
pygame.mixer.init()

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

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.Sysfont('comicsans', 100)
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

YSM = pygame.image.load("yellowm.png")
RSM = pygame.image.load("redm.png")

YS = pygame.transform.rotate(pygame.transform.scale(YSM, (55, 40)), 90)
RS = pygame.transform.rotate(pygame.transform.scale(RSM, (55, 40)), 270)

BULLET_VEL = 7
RED_HIT = pygame.USEREVENT + 2
YELLOW_HIT = pygame.USEREVENT + 1
MAX_BULLETS = 3

def draw_window(red, yellow, red_bullets, yellow_bullets, Red_Health, Yellow_Health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(Red_Health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(Yellow_Health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(YS, (yellow.x, yellow.y))
    WIN.blit(RS, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()

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

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width / 2, HEIGHT / 2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, 300, 55, 40)
    yellow = pygame.Rect(100, 300, 55, 40)
    red_bullets = []
    yellow_bullets = []
    RedHealth = 10
    YellowHealth = 10
    Run = True
    clock = pygame.time.Clock()

    while Run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

            if event.type == RED_HIT:
                RedHealth -= 1

            if event.type == YELLOW_HIT:
                YellowHealth -= 1

        winner_text = ""
        if RedHealth <= 0:
            winner_text = "Yellow Wins"

        if YellowHealth <= 0:
            winner_text = "Red Wins"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellowHW(keys_pressed, yellow)
        redHW(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets)

if __name__ == "__main__":
    main()