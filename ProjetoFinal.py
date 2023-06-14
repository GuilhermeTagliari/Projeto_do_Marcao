import pygame
import tkinter as tk
from tkinter import simpledialog
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projeto de Guilherme Tagliari e Lorenzo Pasa")

icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

pygame.mixer.music.load("Space_Machine_Power.mp3")
<<<<<<< HEAD
pygame.mixer.music.play(-10)
=======
pygame.mixer.music.play(-1)
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441

markings = []

def draw_markings():
<<<<<<< HEAD
    mouse_pos = pygame.mouse.get_pos()

    for i in range(len(markings)):
        pos, name = markings[i]
        pygame.draw.circle(screen, WHITE, pos, 5)
        font = pygame.font.Font(None, 20)
        text = font.render(name, True, BLACK)
        screen.blit(text, pos)

        if i > 0:
            prev_pos, _ = markings[i - 1]
            pygame.draw.line(screen, WHITE, prev_pos, pos)
            diff_x = pos[0] - prev_pos[0]
            diff_y = pos[1] - prev_pos[1]
            diff_text = f"({diff_x}, {diff_y})"

            midpoint_x = (pos[0] + prev_pos[0]) // 2
            midpoint_y = (pos[1] + prev_pos[1]) // 2

            if mouse_por_cima_da_linha(mouse_pos, prev_pos, pos):
                text = font.render(str(diff_text), True, WHITE)
                screen.blit(text, (midpoint_x - 30, midpoint_y + 10))

def mouse_por_cima_da_linha(pos_mouse, pos_inicial, pos_final):
    threshold = 5
=======
    mouse_pos = pygame.mouse.get_pos()  

    for i in range(len(markings)):
        pygame.draw.circle(screen, WHITE, markings[i][0], 5)
        font = pygame.font.Font(None, 20)
        text = font.render(markings[i][1], True, BLACK)
        screen.blit(text, markings[i][0])

        if i > 0:
            pygame.draw.line(screen, WHITE, markings[i - 1][0], markings[i][0])

            
            diff_x = markings[i][0][0] - markings[i - 1][0][0]
            diff_y = markings[i][0][1] - markings[i - 1][0][1]
            diff_text = f"ΔX: {diff_x}, ΔY: {diff_y}"

        
            midpoint_x = (markings[i][0][0] + markings[i - 1][0][0]) // 2
            midpoint_y = (markings[i][0][1] + markings[i - 1][0][1]) // 2

            if is_mouse_over_line(mouse_pos, markings[i - 1][0], markings[i][0]):
                text = font.render(diff_text, True, WHITE)
                screen.blit(text, (midpoint_x - 30, midpoint_y + 10))

def is_mouse_over_line(pos_mouse, pos_inicial, pos_final):
    threshold = 5  
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441
    x1, y1 = pos_inicial
    x2, y2 = pos_final
    x, y = pos_mouse

<<<<<<< HEAD
=======
    
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441
    distancia = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

    return distancia <= threshold

def save_markings():
<<<<<<< HEAD
    try:
        with open("markings.txt", "w") as file:
            for pos, name in markings:
                file.write(f"{pos[0]},{pos[1]},{name}\n")
    except IOError:
        print("Erro ao salvar os pontos!")

def load_markings():
    markings.clear()
    if os.path.exists("markings.txt"):
        try:
            with open("markings.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    try:
                        x, y, name = line.strip().split(",")
                        pos = (int(x), int(y))
                        markings.append((pos, name))
                    except ValueError:
                        print("Erro ao carregar as coordenadas das estrelas!")
        except IOError:
            print("Erro ao carregar os pontos!")
=======
    with open("markings.txt", "a") as file:
        for marking in markings:
            file.write(f"{marking[0][0]},{marking[0][1]},{marking[1]}\n")

def load_markings():
    if os.path.exists("markings.txt"):
        with open("markings.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                x, y, name = line.strip().split(",")
                markings.append([(int(x), int(y)), name])
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441

def clear_markings():
    markings.clear()
    if os.path.exists("markings.txt"):
<<<<<<< HEAD
        try:
            os.remove("markings.txt")
        except OSError:
            print("Erro ao deletar os pontos!")
=======
        os.remove("markings.txt")
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441

def open_dialog():
    root = tk.Tk()
    root.withdraw()
<<<<<<< HEAD
    try:
        name = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
        return name
    except Exception as e:
        print("Erro ao exibir o diálogo:", str(e))
        return None
=======
    name = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return name
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441

def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

background = pygame.image.load("imagem dos pilares da criação.png")

clock = pygame.time.Clock()
running = True
saved_points = False
mouse_pressed = False
current_position = None

<<<<<<< HEAD
load_markings()

=======
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_markings()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pressed = True
                current_position = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and mouse_pressed:
                mouse_pressed = False
                if current_position:
                    name = open_dialog()
<<<<<<< HEAD
                    if name:
                        markings.append((current_position, name))
                    else:
                        markings.append((current_position, "Desconhecido"))
=======
                    markings.append([current_position, name])
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441
                    current_position = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                if not saved_points:
<<<<<<< HEAD
                    save_markings()
                    saved_points = True
            elif event.key == pygame.K_F11:
                load_markings()
=======
                    saved_points = True
            elif event.key == pygame.K_F11:
                clear_markings()
                load_markings()
            elif event.key == pygame.K_F12:
                clear_markings()
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441
                saved_points = False
            elif event.key == pygame.K_ESCAPE:
                save_markings()
                running = False
<<<<<<< HEAD
            elif event.key == pygame.K_F12:
                clear_markings()
                saved_points = False
=======
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441

    screen.blit(background, (0, 0))
    draw_markings()

    font = pygame.font.Font(None, 20)
    display_text("F10 Para salvar os pontos", font, WHITE, 10, 10)
    display_text("F11 Para carregar os pontos salvos", font, WHITE, 10, 30)
    display_text("F12 Para deletar os pontos", font, WHITE, 10, 50)

    if saved_points:
<<<<<<< HEAD
=======
        save_markings()
>>>>>>> 177e241200bf81cb83d7dad3b85ab8d4303c5441
        display_text("Pontos salvos!", font, WHITE, 10, 70)

    pygame.display.flip()

pygame.quit()
