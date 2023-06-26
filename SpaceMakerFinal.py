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