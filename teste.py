import pygame
import tkinter as tk
from tkinter import simpledialog
import os


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projeto de Guilherme Tagliari e Lorenzo Pasa")


icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)


pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)


markings = []

def draw_markings():
    for marking in markings:
        pygame.draw.circle(screen, RED, marking[0], 10)
        font = pygame.font.Font(None, 20)
        text = font.render(marking[1], True, BLACK)
        screen.blit(text, marking[0])

def save_markings():
    with open("markings.txt", "w") as file:
        for marking in markings:
            file.write(f"{marking[0][0]},{marking[0][1]},{marking[1]}\n")

def load_markings():
    if os.path.exists("markings.txt"):
        with open("markings.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                x, y, name = line.strip().split(",")
                markings.append([(int(x), int(y)), name])

def clear_markings():
    markings.clear()

def open_dialog():
    root = tk.Tk()
    root.withdraw()
    name = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return name


background = pygame.image.load("bg.jpg")


running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_markings()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                name = open_dialog()
                position = pygame.mouse.get_pos()
                markings.append([position, name])

    screen.blit(background, (0, 0))
    draw_markings()
    pygame.display.flip()

pygame.quit()
