
import pygame
import sys

# Colores de SpaceBeat
FONDO = (33, 22, 69)
LAVANDA = (216, 180, 254)
TURQUESA = (165, 243, 252)
ROSADO = (251, 207, 232)
BLANCO = (255, 255, 255)

fuente_titulo = pygame.font.SysFont("arial", 28, bold=True)
fuente_teclas = pygame.font.SysFont("arial", 76, bold=True)
fuente_pequena = pygame.font.SysFont("arial", 18)
fuente_boton = pygame.font.SysFont("arial", 22, bold=True)


def dibujar_texto(pantalla, texto, fuente, color, x, y):
    imagen = fuente.render(texto, True, color)
    rectangulo = imagen.get_rect(center=(x, y))
    pantalla.blit(imagen, rectangulo)


def dibujar_boton_volver(pantalla, tiempo_delta, mouse_pos):
    rect = pygame.Rect(30, 30, 230, 55)
    encima = rect.collidepoint(mouse_pos)

    color = TURQUESA if encima else LAVANDA

    pygame.draw.rect(
        pantalla, color, rect, border_radius=15
    )

    dibujar_texto(
        pantalla, "VOLVER AL MENU", fuente_boton,
        FONDO, rect.centerx, rect.centery
    )


def dibujar(pantalla, tiempo_delta):
    pantalla.fill(FONDO)

    # Estrellas
    estrellas = [
        (80, 160), (190, 300), (300, 100),
        (1000, 140), (1130, 400), (980, 600),
        (260, 620), (900, 280), (1080, 80),
    ]

    for x, y in estrellas:
        pygame.draw.circle(pantalla, BLANCO, (x, y), 2)

    dibujar_texto(
        pantalla, "PREPARATE PARA EL RITMO",
        fuente_titulo, ROSADO, 640, 100
    )

    # Pistas diagonales
    izquierda = [
        (390, 150), (565, 150),
        (620, 620), (445, 620),
    ]

    derecha = [
        (715, 150), (890, 150),
        (835, 620), (660, 620),
    ]

    pygame.draw.polygon(pantalla, (75, 53, 120), izquierda)
    pygame.draw.polygon(pantalla, (48, 91, 125), derecha)

    pygame.draw.lines(
        pantalla, LAVANDA, True, izquierda, 4
    )

    pygame.draw.lines(
        pantalla, TURQUESA, True, derecha, 4
    )

    # Zonas de impacto
    pygame.draw.line(
        pantalla, ROSADO, (425, 510), (610, 510), 5
    )

    pygame.draw.line(
        pantalla, ROSADO, (670, 510), (855, 510), 5
    )

    # Teclas provisionales
    dibujar_texto(
        pantalla, "F", fuente_teclas, LAVANDA, 515, 570
    )

    dibujar_texto(
        pantalla, "J", fuente_teclas, TURQUESA, 765, 570
    )

    dibujar_texto(
        pantalla, "Las notas apareceran aqui",
        fuente_pequena, BLANCO, 640, 665
    )

    dibujar_boton_volver(
        pantalla, tiempo_delta, pygame.mouse.get_pos()
    )


def manejar_evento(evento):
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        rect_volver = pygame.Rect(30, 30, 230, 55)

        if rect_volver.collidepoint(evento.pos):
            return "menu"

    return None
