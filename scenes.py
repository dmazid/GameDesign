import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.options = ["Start Game", "Exit"]
        self.selected_option = 0

    def display_menu(self):
        self.screen.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 150 + i * 100))

    def navigate(self, direction):
        self.selected_option = (self.selected_option + direction) % len(self.options)

    def select_option(self):
        return self.options[self.selected_option]
