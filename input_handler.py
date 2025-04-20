import pygame

class input_handler():
    def __init__(self):
        self.key_state = {
            pygame.K_w: False,
            pygame.K_s: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False
        }

    def update(self):
        keys = pygame.key.get_pressed()
        self.key_state[pygame.K_w] = keys[pygame.K_w]
        self.key_state[pygame.K_s] = keys[pygame.K_s]
        self.key_state[pygame.K_UP] = keys[pygame.K_UP]
        self.key_state[pygame.K_DOWN] = keys[pygame.K_DOWN]

    def is_key_pressed(self, key):
        return self.key_state.get(key, False)
