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