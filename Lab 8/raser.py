import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

fps = 60
width = 400
height = 600
speed = 5
score = 0
point = 0

red = (255, 0, 0)
black = (0, 0, 0)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

# Используем raw строки
background = pygame.image.load(r"C:\Users\77478\labs\Lab 8\racer\street.webp")

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")
t = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\77478\labs\Lab 8\racer\Enemy.webp")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0) 

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\77478\labs\Lab 8\racer\money.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0) 

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0) 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\77478\labs\Lab 8\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height - 80)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] and self.rect.bottom < height:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < width:
            self.rect.move_ip(5, 0)

# Создание объектов
P1 = Player()
E1 = Enemy()
M1 = Money()

# Создание групп
enemies = pygame.sprite.Group()
enemies.add(E1)

cash = pygame.sprite.Group()
cash.add(M1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, M1)

# Событие увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    scores = font_small.render(f"Score: {score}", True, black)
    screen.blit(scores, (10, 10))

    points = font_small.render(f"Money: {point}", True, black)
    screen.blit(points, (300, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Столкновение с монетами
    money_collisions = pygame.sprite.spritecollide(P1, cash, dokill=True)
    point += len(money_collisions)

    pygame.display.update()
    t.tick(fps)
