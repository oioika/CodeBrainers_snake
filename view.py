import pygame

def draw(board, screen):
    for coordinates, value in board.items():
        if value == "SnakeHead":
            head_x = coordinates[0] * 20
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x , head_y, 20, 20)
            pygame.draw.rect(screen, (128, 128, 128), head_rect)
        elif value is None:
            head_x = coordinates[0] * 20
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (90, 100, 50), head_rect)