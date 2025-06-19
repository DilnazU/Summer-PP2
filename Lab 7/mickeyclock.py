import pygame
import datetime

# Размер экрана
width, height = 829, 836

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

# Загружаем изображения (внимание на правильные пути!)
main = pygame.image.load(r'C:\Users\77478\labs\Lab 7\Mickey\main-clock.png')
rh = pygame.image.load(r'C:\Users\77478\labs\Lab 7\Mickey\right-hand.png')
lh = pygame.image.load(r'C:\Users\77478\labs\Lab 7\Mickey\left-hand.png')

# Ограничим FPS
clock = pygame.time.Clock()
running = True

while running:
    screen.blit(main, (0, 0))  # Отображаем фон
    now = datetime.datetime.now()

    # Вращаем секундную (левая рука)
    rot1 = pygame.transform.rotate(lh, -now.second * 6)
    rot1_rect = rot1.get_rect(center=(width / 2, height / 2))
    screen.blit(rot1, rot1_rect)

    # Вращаем минутную (правая рука)
    rot2 = pygame.transform.rotate(rh, -now.minute * 6)
    rot2_rect = rot2.get_rect(center=(width / 2, height / 2))
    screen.blit(rot2, rot2_rect)

    pygame.display.update()
    clock.tick(60)  # Ограничение 60 кадров в секунду

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()