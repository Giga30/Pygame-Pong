import pygame

def draw_text(text, font, text_size, text_col, x, y, surface):
    img = pygame.font.SysFont(font, text_size, bold=False, italic=False).render(text, True, text_col)
    img_rect = img.get_rect(center=(x, y))
    surface.blit(img, img_rect)