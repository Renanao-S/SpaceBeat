import pygame

pygame.init()

ancho = 1280
alto = 720

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("SpaceBeat")

fondo = (13,10,35)
lavanda=(190,155,255)
turquesa = (100,235,220)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(fondo)
    pygame.draw.rect(pantalla, lavanda, (420, 0, 170, alto))
    pygame.draw.rect(pantalla, turquesa, (690, 0, 170, alto))

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame al salir
pygame.quit()