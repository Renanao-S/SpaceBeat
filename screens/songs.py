
import pygame

# Colores de SpaceBeat
FONDO = (33, 22, 69)
LAVANDA = (216, 180, 254)
TURQUESA = (165, 243, 252)
ROSADO = (251, 207, 232)
BLANCO = (255, 255, 255)
MORADO_TARJETA = (55, 42, 86)

# Fuentes
fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
fuente_subtitulo = pygame.font.SysFont("arial", 22)
fuente_cancion = pygame.font.SysFont("arial", 25, bold=True)
fuente_detalle = pygame.font.SysFont("arial", 17)
fuente_boton = pygame.font.SysFont("arial", 21, bold=True)

# Canciones provisionales.
# Más adelante agregaremos los archivos de audio reales.
canciones = [
    {
        "nombre": "Canción de ejemplo 01",
        "duracion": "2:30",
    },
    {
        "nombre": "Canción de ejemplo 02",
        "duracion": "3:15",
    },
    {
        "nombre": "Canción de ejemplo 03",
        "duracion": "2:48",
    },
]

indice_seleccionado = 0
dificultad = "Normal"


def dibujar_texto(pantalla, texto, fuente, color, x, y):
    imagen = fuente.render(texto, True, color)
    rectangulo = imagen.get_rect(center=(x, y))
    pantalla.blit(imagen, rectangulo)


def dibujar(pantalla, tiempo_delta):
    pantalla.fill(FONDO)

    # Estrellas decorativas
    estrellas = [
        (80, 120), (170, 250), (1120, 100),
        (1050, 320), (120, 590), (1150, 610),
        (350, 90), (900, 160), (980, 560),
        (220, 450), (1080, 220),
    ]

    for x, y in estrellas:
        pygame.draw.circle(pantalla, BLANCO, (x, y), 2)

    # Título
    dibujar_texto(
        pantalla, "SELECCIONA TU CANCION",
        fuente_titulo, ROSADO, 640, 75
    )

    dibujar_texto(
        pantalla, "Elige tu próxima batalla musical",
        fuente_subtitulo, TURQUESA, 640, 120
    )

    # Botón para volver
    rect_volver = pygame.Rect(30, 25, 205, 50)
    mouse_pos = pygame.mouse.get_pos()

    color_volver = (
        TURQUESA
        if rect_volver.collidepoint(mouse_pos)
        else LAVANDA
    )

    pygame.draw.rect(
        pantalla, color_volver, rect_volver,
        border_radius=14
    )

    dibujar_texto(
        pantalla, "VOLVER AL MENU",
        fuente_boton, FONDO,
        rect_volver.centerx, rect_volver.centery
    )

    # Lista de canciones
    for indice, cancion in enumerate(canciones):
        rect = pygame.Rect(250, 165 + indice * 100, 780, 82)

        if indice == indice_seleccionado:
            color_borde = TURQUESA
            grosor_borde = 4
        else:
            color_borde = LAVANDA
            grosor_borde = 2

        pygame.draw.rect(
            pantalla, MORADO_TARJETA, rect,
            border_radius=16
        )

        pygame.draw.rect(
            pantalla, color_borde, rect,
            grosor_borde, border_radius=16
        )

        # Número de la canción
        dibujar_texto(
            pantalla, f"{indice + 1:02}",
            fuente_cancion, TURQUESA,
            rect.x + 48, rect.centery
        )

        # Nombre
        dibujar_texto(
            pantalla, cancion["nombre"],
            fuente_cancion, BLANCO,
            rect.x + 320, rect.centery - 10
        )

        # Duración
        dibujar_texto(
            pantalla, f"Duracion: {cancion['duracion']}",
            fuente_detalle, LAVANDA,
            rect.x + 320, rect.centery + 18
        )

        if indice == indice_seleccionado:
            dibujar_texto(
                pantalla, "SELECCIONADA",
                fuente_detalle, TURQUESA,
                rect.right - 105, rect.centery
            )

    # Selector de dificultad
    dibujar_texto(
        pantalla, "DIFICULTAD",
        fuente_boton, BLANCO, 490, 500
    )

    rect_normal = pygame.Rect(590, 475, 150, 52)
    rect_dificil = pygame.Rect(755, 475, 150, 52)

    color_normal = (
        TURQUESA if dificultad == "Normal"
        else MORADO_TARJETA
    )

    color_dificil = (
        ROSADO if dificultad == "Dificil"
        else MORADO_TARJETA
    )

    pygame.draw.rect(
        pantalla, color_normal, rect_normal,
        border_radius=12
    )
    pygame.draw.rect(
        pantalla, color_dificil, rect_dificil,
        border_radius=12
    )

    pygame.draw.rect(
        pantalla, TURQUESA, rect_normal,
        2, border_radius=12
    )
    pygame.draw.rect(
        pantalla, ROSADO, rect_dificil,
        2, border_radius=12
    )

    dibujar_texto(
        pantalla, "NORMAL", fuente_boton,
        FONDO if dificultad == "Normal" else BLANCO,
        rect_normal.centerx, rect_normal.centery
    )

    dibujar_texto(
        pantalla, "DIFICIL", fuente_boton,
        FONDO if dificultad == "Dificil" else BLANCO,
        rect_dificil.centerx, rect_dificil.centery
    )

    # Botón para comenzar
    rect_comenzar = pygame.Rect(465, 570, 350, 65)

    pygame.draw.rect(
        pantalla, LAVANDA, rect_comenzar,
        border_radius=18
    )

    dibujar_texto(
        pantalla, "COMENZAR BATALLA",
        fuente_boton, FONDO,
        rect_comenzar.centerx, rect_comenzar.centery
    )


def manejar_evento(evento):
    global indice_seleccionado, dificultad

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        posicion = evento.pos

        # Volver al menú
        rect_volver = pygame.Rect(30, 25, 205, 50)

        if rect_volver.collidepoint(posicion):
            return "menu"

        # Seleccionar una canción
        for indice in range(len(canciones)):
            rect = pygame.Rect(250, 165 + indice * 100, 780, 82)

            if rect.collidepoint(posicion):
                indice_seleccionado = indice
                return None

        # Elegir dificultad
        rect_normal = pygame.Rect(590, 475, 150, 52)
        rect_dificil = pygame.Rect(755, 475, 150, 52)

        if rect_normal.collidepoint(posicion):
            dificultad = "Normal"

        elif rect_dificil.collidepoint(posicion):
            dificultad = "Dificil"

        # Comenzar el juego
        rect_comenzar = pygame.Rect(465, 570, 350, 65)

        if rect_comenzar.collidepoint(posicion):
            return "comenzar"

    return None


def obtener_cancion_seleccionada():
    return canciones[indice_seleccionado]


def obtener_dificultad():
    return dificultad
