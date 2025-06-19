import pygame
import datetime


width, height = 829, 836

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

main = pygame.image.load(r'C:\Users\77478\labs\Lab 7\Mickey\main-clock.png')
rh = pygame.image.load(r'C:\Users\77478\labs\Lab 7\Mickey\right-hand.png')
lh = pygame.image.load(r'C:\Users\77478\labs\Lab 7\Mickey\left-hand.png')


clock = pygame.time.Clock()
running = True

while running:
    screen.blit(main, (0, 0))  
    now = datetime.datetime.now()

   
    rot1 = pygame.transform.rotate(lh, -now.second * 6)
    rot1_rect = rot1.get_rect(center=(width / 2, height / 2))
    screen.blit(rot1, rot1_rect)

   
    rot2 = pygame.transform.rotate(rh, -now.minute * 6)
    rot2_rect = rot2.get_rect(center=(width / 2, height / 2))
    screen.blit(rot2, rot2_rect)

    pygame.display.update()
    clock.tick(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
