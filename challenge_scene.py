import pygame

class ChallengeScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.challenge_text = "Write a Python function to add two numbers."
        self.user_code = ""
        self.running = True

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key == pygame.K_BACKSPACE:
                self.user_code = self.user_code[:-1]
            elif event.key == pygame.K_RETURN:
                self.check_code()
            else:
                self.user_code += event.unicode

    def check_code(self):
        try:
            exec(self.user_code)
            # Example function call and check
            if add_numbers(1, 2) == 3:
                print("Correct!")
                self.running = False
            else:
                print("Incorrect. Try again.")
        except:
            print("Error in code.")

    def update(self):
        # Update challenge logic here
        pass

    def render(self):
        self.screen.fill((200, 200, 200))  # Change background color for challenge scene
        challenge_surface = self.font.render(self.challenge_text, True, (0, 0, 0))
        self.screen.blit(challenge_surface, (20, 20))
        code_surface = self.font.render(self.user_code, True, (0, 0, 0))
        self.screen.blit(code_surface, (20, 80))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_events(event)

            self.update()
            self.render()
            pygame.display.flip()
