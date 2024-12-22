import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

def game_over_screen(game):
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        game_over_surf = font.render("GAME OVER", True, (255, 0, 0))
        restart_surf = font.render("Press ESC to QUIT", True, (255, 255, 255))

        game_over_rect = game_over_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        restart_rect = restart_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        screen.blit(game_over_surf, game_over_rect)
        screen.blit(restart_surf, restart_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game.running = False
                return