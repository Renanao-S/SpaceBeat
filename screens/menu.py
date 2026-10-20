
import pygame
import sys

FONDO = (33, 22, 69)
LAVANDA = (216, 180, 254)
TURQUESA = (165, 243, 252)
ROSADO = (251, 207, 232)
BLANCO = (255, 255, 255)
MORADO_OSCURO = (33, 22, 69)

fuente_titulo = pygame.font.SysFont("arial", 76, bold=True)
fuente_subtitulo = pygame.font.SysFont("arial", 25)
fuente_botones = pygame.font.SysFont("arial", 28, bold=True)

botones = [
    {
        "texto": "JUGAR",
        "rect": pygame.Rect(465, 405, 350, 65),
        "color": LAVANDA,
        "accion": "jugar",
        "escala": 1.0,
    },
    {
        "texto": "CANCIONES",
        "rect": pygame.Rect(465, 490, 350, 65),
        "color": TURQUESA,
        "accion": "canciones",
        "escala": 1.0,
    },
    {
        "texto": "SALIR",
        "rect": pygame.Rect(465, 575, 350, 65),
        "color": ROSADO,
        "accion": "salir",
        "escala": 1.0,
    },
]


def dibujar_texto(pantalla, texto, fuente, color, x, y):
    imagen = fuente.render(texto, True, color)
    rectangulo = imagen.get_rect(center=(x, y))
    pantalla.blit(imagen, rectangulo)


def dibujar_planeta(pantalla, x, y, radio, color):
    pygame.draw.ellipse(
        pantalla, color,
        (x - radio - 18, y - 9, radio * 2 + 36, 18), 4
    )

    pygame.draw.circle(pantalla, color, (x, y), radio)

    pygame.draw.circle(
        pantalla, FONDO,
        (x - radio // 3, y - radio // 3),
        max(1, radio // 5)
    )


def dibujar_boton(pantalla, boton, tiempo_delta):
    mouse_pos = pygame.mouse.get_pos()
    pulsado = pygame.mouse.get_pressed()[0]
    encima = boton["rect"].collidepoint(mouse_pos)

    if encima and pulsado:
        objetivo = 1.10
    elif encima:
        objetivo = 1.07
    else:
        objetivo = 1.0

    factor = min(1.0, 12 * tiempo_delta)

    boton["escala"] += (
        objetivo - boton["escala"]
    ) * factor

    rect_original = boton["rect"]

    ancho = round(rect_original.width * boton["escala"])
    alto = round(rect_original.height * boton["escala"])

    rect_animado = pygame.Rect(0, 0, ancho, alto)
    rect_animado.center = rect_original.center

    pygame.draw.rect(
        pantalla, boton["color"],
        rect_animado, border_radius=18
    )

    dibujar_texto(
        pantalla, boton["texto"], fuente_botones,
        MORADO_OSCURO,
        rect_animado.centerx, rect_animado.centery
    )


def dibujar(pantalla, tiempo_delta):
    pantalla.fill(FONDO)

    estrellas = [
        (100, 100, 3), (230, 190, 2), (1100, 130, 3),
        (1000, 270, 2), (180, 340, 2), (1090, 520, 3),
        (330, 80, 2), (940, 90, 2), (870, 350, 2),
        (250, 620, 3), (1050, 650, 2), (390, 280, 2),
    ]

    for x, y, radio in estrellas:
        pygame.draw.circle(pantalla, BLANCO, (x, y), radio)

    dibujar_planeta(pantalla, 180, 250, 48, TURQUESA)
    dibujar_planeta(pantalla, 1230, 300, 200, LAVANDA)

    dibujar_texto(
        pantalla, "SPACEBEAT", fuente_titulo,
        ROSADO, 640, 130
    )

    dibujar_texto(
        pantalla, "El sonido del universo",
        fuente_subtitulo, TURQUESA, 640, 195
    )

    for boton in botones:
        dibujar_boton(pantalla, boton, tiempo_delta)


def manejar_evento(evento):
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        for boton in botones:
            if boton["rect"].collidepoint(evento.pos):
                return boton["accion"]

    return None
