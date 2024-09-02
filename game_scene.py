import pygame
from challenge_scene import ChallengeScene

class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.challenge_scene = ChallengeScene(screen)
        self.running = True

    def handle_events(self, event):
        self.challenge_scene.handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self):
        self.challenge_scene.update()

    def render(self):
        self.challenge_scene.render()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_events(event)

            self.update()
            self.render()
            pygame.display.flip()
