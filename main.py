import pygame
pygame .init()
tamanho= (800,600)
branco = (255,255,255)
tela = pygame.display.set_mode( tamanho ) 
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()

