import pygame
import tkinter as tk
from tkinter import simpledialog
import os

pygame.init()

display_W = 800
display_H = 500

mark = []
ilustracao = pygame.image.load("space.png")
pygame.display.set_icon(ilustracao)
display_game = pygame.display.set_mode((display_W, display_H))
pygame.display.set_caption("Projeto SpaceMaker de João Ricardo Biasi")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)

white=(255, 255, 255)
black=(0, 0, 0)

def mouse_over_line(mouse_position, pos_start, pos_end):
    limit = 5
    x, y = mouse_position
    x1, y1 = pos_start
    x2, y2 = pos_end

    denominator=((y2 -y1) ** 2 + (x2 -x1) **2)** 0.5
    if denominator !=0:
        distance=abs((y2 - y1) * x - (x2 -x1) * y + x2 * y1 -y2 * x1)/denominator
    else:
        distance=0
    return distance <= limit

def display_text(txt, font, color, x, y):
    text_surface = font.render(txt, True, color)
    display_game.blit(text_surface, (x, y))

def opening_dialog():
    r = tk.Tk()
    r.withdraw()
    r.update()
    try:
        name = simpledialog.askstring("NOME DA ESTRELA:", "DIGITE O NOME DA ESTRELA:")
        if name is not None:  
            return name
        else:
            return None
    except Exception as e:
        print("Erro ao exibir o diálogo:", str(e))
        return None

def draw_mark():
    mouse_position = pygame.mouse.get_pos()
    for x in range(len(mark)):
        pos, name = mark[x]
        if pos is not None:  
            pygame.draw.circle(display_game, white, pos, 5)
            font = pygame.font.Font(None, 20)
            txt = font.render(name, True, black)
            display_game.blit(txt, pos)

    for x in range(1, len(mark)):
        pos, name = mark[x]
        pos_prev, _ = mark[x - 1]
        pygame.draw.line(display_game, white, pos_prev, pos)
        a = pos[0] - pos_prev[0]
        b = pos[1] - pos_prev[1]
        diff_txt = f"({a}, {b})"

        point_a = (pos[0] + pos_prev[0]) // 2
        point_b = (pos[1] + pos_prev[1]) // 2

        if mouse_over_line(mouse_position, pos_prev, pos):
            txt = font.render(str(diff_txt), True, white)
            display_game.blit(txt, (point_a - 30, point_b + 10))

def save_mark():
    try:
        with open("mark.txt", "w") as file:
            for pos, name in mark:
                if "Desconhecida" in name:
                    file.write(f"{name}\n")
                else:
                    file.write(f"{pos[0]},{pos[1]},{name}\n")
    except IOError:
        print=("ERRO AO SALVAR OS PONTOS!")

def load_mark():
    if os.path.exists("mark.txt"):
        try:
            with open("mark.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    try:
                        virgula = line.strip().split(",")
                        if len(virgula) == 3:
                            x, y, name = virgula
                            if x == "-1" and y == "-1":
                                pos = None
                            else:
                                pos = (int(x), int(y))
                            mark.append((pos, name))
                        else:
                            print("FORMATO DE LINHA INVALIDO!", line)
                    except ValueError:
                        print("ERRO AO CARREGAR AS COORDENADAS!")
        except IOError:
            print("ERRO AO CERRAGAR OS PONTOS!")
    else:
        print("ARQUIVO NÃO ENCONTRADO.")

def clear_mark():
    if os.path.exists("mark.txt"):
        try:
            os.remove("mark.txt")
        except OSError:
            print("ERRO AO DELETAR OS PONTOS!")