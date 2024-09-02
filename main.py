import pygame
import sys
from scenes import MainMenu
from game_scene import GameScene

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CodeQuest: Python Adventures')

# Initialize scenes
main_menu = MainMenu(screen)
game_scene = GameScene(screen)

# Current scene
current_scene = "MainMenu"

def run_game():
    global current_scene
    current_scene = "GameScene"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif current_scene == "MainMenu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_menu.navigate(-1)
                elif event.key == pygame.K_DOWN:
                    main_menu.navigate(1)
                elif event.key == pygame.K_RETURN:
                    option = main_menu.select_option()
                    if option == "Start Game":
                        run_game()  # Switch to the game scene
                    elif option == "Exit":
                        pygame.quit()
                        sys.exit()
        elif current_scene == "GameScene":
            game_scene.handle_events(event)

    if current_scene == "MainMenu":
        main_menu.display_menu()
    elif current_scene == "GameScene":
        game_scene.update()
        game_scene.render()

    pygame.display.flip()
