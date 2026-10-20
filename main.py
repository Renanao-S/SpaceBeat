

import pygame
import sys

# Inicializar Pygame antes de cargar las pantallas
pygame.init()
pygame.font.init()

from screens import menu, songs, gameplay

ANCHO = 1280
ALTO = 720

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("SpaceBeat")

reloj = pygame.time.Clock()

pantalla_actual = "menu"
ejecutando = True

# Datos de la canción elegida
cancion_actual = None
dificultad_actual = "Normal"


while ejecutando:
    tiempo_delta = reloj.tick(60) / 1000

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        # Menu principal
        elif pantalla_actual == "menu":
            accion = menu.manejar_evento(evento)

            if accion == "jugar" or accion == "canciones":
                pantalla_actual = "canciones"

        # Selector de canciones
        elif pantalla_actual == "canciones":
            accion = songs.manejar_evento(evento)

            if accion == "menu":
                pantalla_actual = "menu"

            elif accion == "comenzar":
                cancion_actual = songs.obtener_cancion_seleccionada()
                dificultad_actual = songs.obtener_dificultad()

                print("Cancion elegida:", cancion_actual["nombre"])
                print("Dificultad:", dificultad_actual)

                pantalla_actual = "juego"

        # Pantalla de juego
        elif pantalla_actual == "juego":
            accion = gameplay.manejar_evento(evento)

            if accion == "menu":
                pantalla_actual = "menu"

    # Dibujar la pantalla actual
    if pantalla_actual == "menu":
        menu.dibujar(pantalla, tiempo_delta)

    elif pantalla_actual == "canciones":
        songs.dibujar(pantalla, tiempo_delta)

    elif pantalla_actual == "juego":
        gameplay.dibujar(pantalla, tiempo_delta)

    pygame.display.flip()

pygame.quit()
sys.exit()
