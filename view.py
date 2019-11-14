import pygame


def draw(board, screen, score):
    for coordinates, value in board.items():
        if value == "SnakeHead":
            head_x = coordinates[0] * 20
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (128, 128, 128), head_rect)
        elif value is None:
            head_x = coordinates[0] * 20
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (90, 100, 50), head_rect)
        elif value == "Apple":
            head_x = coordinates[0] * 20
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (255, 0, 0), head_rect)

    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(str(score), True, (0, 0, 100))
    screen.blit(text, dest=(20,20))
