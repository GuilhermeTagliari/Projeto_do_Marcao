import pygame
import tkinter as tk
from tkinter import simpledialog
import os
pygame.init()
screenW = 800
screenH = 600
branco = (255, 255, 255)
preto = (0, 0, 0)
tela = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Projeto de Guilherme Tagliari e Lorenzo Pasa")
icone = pygame.image.load("icon2.png")
pygame.display.set_icon(icone)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
background = pygame.image.load("imagem dos pilares da criação.png")
marcacoes = []
clock = pygame.time.Clock()
running = True
pontos_salvos = False
botao_mouse = False
posi_atual = None

def marcar():
    posi_mouse = pygame.mouse.get_pos()

    for itens in range(len(marcacoes)):
        posi, nome = marcacoes[itens]
        if posi is not None:  # Verificar se as coordenadas são válidas
            pygame.draw.circle(tela, branco, posi, 5)
            fonte = pygame.font.Font(None, 20)
            texto = fonte.render(nome, True, preto)
            tela.blit(texto, posi)

    for itens in range(1, len(marcacoes)):
        posi, nome = marcacoes[itens]
        posi_previa, _ = marcacoes[itens - 1]
        pygame.draw.line(tela, branco, posi_previa, posi)
        dife_x = posi[0] - posi_previa[0]
        dife_y = posi[1] - posi_previa[1]
        texto_dife = f"({dife_x}, {dife_y})"
        medio_x = (posi[0] + posi_previa[0]) // 2
        medio_y = (posi[1] + posi_previa[1]) // 2
        if dife_cord(posi_mouse, posi_previa, posi):
            texto = fonte.render(str(texto_dife), True, branco)
            tela.blit(texto, (medio_x - 30, medio_y + 10))


def dife_cord(posi_mouse, posi_inicial, posi_final):
    limitador = 5
    x1, y1 = posi_inicial
    x2, y2 = posi_final
    x, y = posi_mouse
    distancia = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distancia <= limitador

def salvar_marcas():
    try:
        with open("markings.txt", "w") as file:
            for posi, nome in marcacoes:
                if "Desconhecida" in nome:
                    file.write(f"{nome}\n")
                else:
                    file.write(f"{posi[0]},{posi[1]},{nome}\n")
    except IOError:
        print("Erro ao salvar os pontos!")

def carregar_marcas():
    if os.path.exists("markings.txt"):
        try:
            with open("markings.txt", "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    try:
                        salvar = linha.strip().split(",")
                        if len(salvar) == 3:
                            x, y, nome = salvar
                            if x == "-1" and y == "-1":
                                posi = None
                            else:
                                posi = (int(x), int(y))
                            marcacoes.append((posi, nome))
                        else:
                            print("Formato inválido para a linha:", linha)
                    except ValueError:
                        print("Erro ao carregar as coordenadas das estrelas!")
        except IOError:
            print("Erro ao carregar os pontos!")
    else:
        print("Arquivo de marcações não encontrado.")

def limpar():
    if os.path.exists("markings.txt"):
        try:
            os.remove("markings.txt")
        except OSError:
            print("Erro ao deletar os pontos!")

def nome_estrelas():
    teste = tk.Tk()
    teste.withdraw()
    teste.update()
    try:
        nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
        if nome is not None:  
            return nome
        else:
            return None
    except Exception as erro:
        print("Erro ao exibir o diálogo:", str(erro))
        return None

def mostar_texto(texto, fonte, cor, x, y):
    txt = fonte.render(texto, True, cor)
    tela.blit(txt, (x, y))


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvar_marcas()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                botao_mouse = True
                posi_atual = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and botao_mouse:
                botao_mouse = False
            if posi_atual:
                nome = nome_estrelas()
            if nome is not None and nome != "":  
                marcacoes.append((posi_atual, nome))
            elif nome == "":
                x, y = posi_atual
                marcacoes.append((posi_atual, f" {x}, {y},Desconhecida"))
            posi_atual = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                if not pontos_salvos:
                    salvar_marcas()
                    pontos_salvos = True
            elif event.key == pygame.K_F11:
                carregar_marcas()
                pontos_salvos = False
            elif event.key == pygame.K_ESCAPE:
                salvar_marcas()
                running = False
            elif event.key == pygame.K_F12:
                limpar()
                pontos_salvos = False

    tela.blit(background, (0, 0))
    marcar()
    fonte = pygame.font.Font(None, 20)
    mostar_texto("F10 Para salvar os pontos", fonte, branco, 10, 10)
    mostar_texto("F11 Para carregar os pontos salvos", fonte, branco, 10, 30)
    mostar_texto("F12 Para deletar os pontos", fonte, branco, 10, 50)
    if pontos_salvos:
        mostar_texto("Pontos salvos!", fonte, branco, 10, 70)

    pygame.display.flip()

pygame.quit()