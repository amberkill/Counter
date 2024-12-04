import pygame

class IncreasCount: 
    clock = pygame.time.Clock()
    running = True
    def __init__(self):
         self.screen_w = 300
         self.screen_h = 400
         self.bg = ('assets/power_off.png')

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    def count_up(event):
        count = 0
        if event.key == pygame.K_UP:
            count += 1
            print(count)
        else:
            print(count)
 # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()