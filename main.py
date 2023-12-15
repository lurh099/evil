import pygame
import random

# pygame-Initialisierung
pygame.init()

# Bildschirmgröße und Titel setzen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Glücksrad')

# Font und Schriftgröße
font = pygame.font.Font(None, 36)

# Gewinnmöglichkeiten
preise = ['10% Rabatt', '20% Rabatt', '100% Rabatt', 'Nicht Gewonnen']

# Zufallszahl generieren, um die Position des Gewinns festzulegen
gewinn = random.randint(0, 3)

# Bildschirm aktualisieren
pygame.display.flip()

# Spielschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Glücksrad zeichnen
    screen.fill((255, 255, 255))
    radius = 200
    center = (400, 300)
    start_angle = 0
    end_angle = 360
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    for i in range(4):
        if gewinn == i:
            text = font.render(preise[i], True, (0, 0, 0))
            screen.blit(text, (center[0] - text.get_width() // 2, center[1] - text.get_height() // 2 - 20))
        pygame.draw.arc(screen, colors[i], (center[0] - radius, center[1] - radius, 2 * radius, 2 * radius), start_angle, end_angle, 1)
        start_angle += 90
        end_angle += 90

    # Bildschirm aktualisieren
    pygame.display.flip()

# pygame beenden
pygame.quit()