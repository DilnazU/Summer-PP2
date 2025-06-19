import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("PyGame Player")

playlist = [
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - A monster.mp3",
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - Angel.mp3",
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - Bad Liar.mp3",
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - believer.mp3",
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - Bones.mp3",
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - Enemy (Feat. JID).mp3",
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - thunder.mp3",
    r"C:\Users\77478\labs\Lab 7\Player\Imagine Dragons - Whatever It Takes.mp3"
]

i = 0  
j = 0  

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
          
            if event.key == pygame.K_SPACE:
                i += 1
                if i == 1:
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                elif i % 2 == 0:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

         
            elif event.key == pygame.K_RIGHT:
                j += 1
                if j >= len(playlist):
                    j = 0
                i = 1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(playlist[j])
                pygame.mixer.music.play()

          
                
                