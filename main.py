import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

while True:
    # Event for close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()
