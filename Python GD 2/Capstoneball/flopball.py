import pgzrun
from random import randint

TITLE = "FLAPPYBALL"
HEIGHT = 600
WIDTH = 800
R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)
clr = R, G, B

GRAVITY = 2000.0 #pixels per second

class Ball:
    def __init__(self, intial_x, intial_y):
        self.x = intial_x
        self.y = intial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
        
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, clr)

ball = Ball(50, 100)
def draw():
    screen.clear()
    ball.draw()

def update(dt):
    # Apply constant acceleration formulae
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt

    # detect and handle bounce
    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy = -ball.vy * 0.9 
        
    # X coponent doesn't have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx 

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()