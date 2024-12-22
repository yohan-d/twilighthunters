import pygame
import sys
import os
from main import Game

def show_credits(surface):
    credits = ["Yohan", "Fatema", "Tomoghna", "Maani"]
    font = pygame.font.Font(None, 60)
    surface.fill(BLACK)
    for i, name in enumerate(credits):
        text_surf = font.render(name, True, WHITE)
        text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100 + i * 100))
        surface.blit(text_surf, text_rect)
    pygame.display.flip()
    pygame.time.wait(8000)

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FONT_SIZE = 40
BUTTON_WIDTH, BUTTON_HEIGHT = 250, 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (200, 50, 50)
HOVER_RED = (255, 100, 100)
YELLOW = (255, 223, 0)
HOVER_YELLOW = (255, 255, 102)
LIGHT_BLUE = (48,213,200)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Twilight Hunters")

font = pygame.font.Font(None, FONT_SIZE)

background_image = pygame.image.load("bg.png").convert()

hover_effects = {
    "START": (YELLOW, HOVER_YELLOW),
    "CREDITS": (LIGHT_BLUE, GRAY),
    "QUIT": (RED, HOVER_RED)
}

def draw_button(surface, text, rect, hover, base_color, hover_color):
    color = hover_color if hover else base_color
    pygame.draw.rect(surface, color, rect, border_radius=10)
    pygame.draw.rect(surface, BLACK, rect, 3, border_radius=10)
    text_surf = font.render(text, True, BLACK if hover else WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

buttons = [
    {"text": "START", "rect": pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT)},
    {"text": "CREDITS", "rect": pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)},
    {"text": "QUIT", "rect": pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)},
]

running = True
while running:
    screen.blit(background_image, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_clicked = True

    for button in buttons:
        hover = button["rect"].collidepoint(mouse_pos)
        base_color, hover_color = hover_effects[button["text"]]
        draw_button(screen, button["text"], button["rect"], hover, base_color, hover_color)

        if hover and mouse_clicked:
            if button["text"] == "START":
                game = Game()
                game.run()
            elif button["text"] == "CREDITS":
                show_credits(screen)
            elif button["text"] == "QUIT":
                running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
