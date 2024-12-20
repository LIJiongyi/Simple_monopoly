import pygame
import sys
import random
import string
from monopoly_game_logic import Monopolyclass, Playerclass
from All_slot import Property
from Board_back import Boardclass
from Gameboard import mainscreen
import os
import json

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_SIZE = 760
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Monopoly - Start")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)


def generate_random_name():
    length = random.randint(1, 20)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class Start_game:
    def __init__(self):
        self.board = None
        self.game = None
        # self.board = Boardclass()
        # self.game = Monopolyclass()
        self.font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 36)
        self.screen_size = SCREEN_SIZE
        self.screen = screen
        self.clock = pygame.time.Clock()
        # Button dimensions
        self.button_width = 200
        self.button_height = 50
        self.create_buttons()
        # Player name input
        self.collecting_names = False
        self.player_inputs = []
        self.max_players = 6
        self.min_players = 2
        self.current_player = 1
        self.running = True
        self.error_message = ""

    def initload(self):
        self.board = Boardclass()
        self.game = Monopolyclass()
        self.create_buttons()

    def create_buttons(self):
        # Define Start Button
        self.start_button_rect = pygame.Rect(
            (self.screen_size // 2) - (self.button_width // 2),
            (self.screen_size // 2) - 25,
            self.button_width,
            self.button_height
        )
        # Define Quit Button
        self.quit_button_rect = pygame.Rect(
            (self.screen_size // 2) - (self.button_width // 2),
            (self.screen_size // 2) + 50,
            self.button_width,
            self.button_height
        )

    def start_new_game(self):
        self.initload()
        self.collecting_names = True
        self.player_inputs.append(InputBox(
            self.screen_size // 2 - 100, self.screen_size // 2 -50, 200, 50))
        self.error_message = ""
        self.run()

    def load_saved_game(self, filename="save.json"):
        try:
            saved_games_dir = os.path.join(os.getcwd(), 'saved')
            filepath = os.path.join(saved_games_dir, filename)
            with open(filepath, "r") as file:
                game_state = json.load(file)
            self.board = Boardclass()  # 初始化 board
            self.game = Monopolyclass()  # 初始化 game
            self.game.players = []
            # self.game.players = []
            for player_data in game_state["players"]:
                player = Playerclass(player_data["name"], self.board)
                player.money = player_data["money"]
                player.position = player_data["position"]
                player.jail = player_data["jail"]
                player.jailturns = player_data["jailturns"]
                player.properties = [Property(name, price, rent) for name, price, rent in player_data["properties"]]
                self.game.players.append(player)

            self.game.round_count = game_state["round_count"]
            self.game.turn_count = game_state["turn_count"]
            self.game.current_position = game_state["current_position"]
            print(f"Game state loaded from {filename}")
            mainscreen(self.game, continue_game=True)
        except FileNotFoundError:
            print(f"No saved game found with the filename {filename}.")
        except Exception as e:
            print(f"An error occurred while loading the game: {e}")
        self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.draw_interface()
            pygame.display.flip()
            self.clock.tick(30)  # Limit to 30 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif self.collecting_names:
                if event.type == pygame.KEYDOWN:
                    if self.player_inputs:
                        current_input_box = self.player_inputs[-1]
                        if event.key == pygame.K_RETURN:
                            name = current_input_box.text.strip()
                            if name.lower() == 'done':
                                if len(self.game.players) >= self.min_players:
                                    self.collecting_names = False
                                    # Start the main game board
                                    mainscreen(self.game, continue_game=False)
                                else:
                                    self.error_message = f"Error: Need at least {self.min_players} players to start."
                            elif name:
                                if any(player.name == name for player in self.game.players):
                                    self.error_message = "Error: Name already taken. Please enter a different name."

                                else:
                                    self.game.add_player(name)
                                    self.error_message = ""
                                    self.current_player += 1
                                    if self.current_player > self.max_players or len(
                                            self.game.players) >= self.max_players:
                                        self.collecting_names = False
                                        # Start main board
                                        mainscreen(self.game, continue_game=False)

                                    else:
                                        # Prepare for next player input
                                        self.player_inputs.append(InputBox(
                                            self.screen_size // 2 - 100,
                                            self.screen_size // 2 - 50 + (self.current_player - 1) * 60, 200, 50))
                            else:
                                self.error_message = "Error: No name entered. Please enter a valid name."
                        elif event.key == pygame.K_BACKSPACE:
                            if current_input_box.text:
                                current_input_box.text = current_input_box.text[:-1]
                        else:
                            # Limit the input to reasonable length
                            if len(current_input_box.text) < 20:
                                current_input_box.text += event.unicode
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button_rect.collidepoint(mouse_pos):
                        # Start collecting player names
                        self.collecting_names = True
                        # Initialize first InputBox
                        self.player_inputs.append(InputBox(
                            self.screen_size // 2 - 100, self.screen_size // 2 + 100, 200, 50))
                        self.error_message = ""
                    elif self.quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

    def draw_interface(self):
        self.screen.fill(WHITE)

        if self.collecting_names:
            # Display player name collection
            prompt_text = small_font.render(f"Enter name for Player {self.current_player}:", True, BLACK)
            prompt_rect = prompt_text.get_rect(center=(self.screen_size // 2, self.screen_size // 2 - 100))
            self.screen.blit(prompt_text, prompt_rect)

            for input_box in self.player_inputs:
                input_box.draw(self.screen)
        else:
            # Display Welcome Screen with Start and Quit buttons
            # Welcome Text
            welcome_text = self.font.render("Welcome to Monopoly!", True, BLACK)
            welcome_rect = welcome_text.get_rect(center=(self.screen_size // 2, self.screen_size // 2 - 100))
            self.screen.blit(welcome_text, welcome_rect)

            # Start Button
            pygame.draw.rect(self.screen, GREEN, self.start_button_rect)
            start_text = small_font.render("Start Game", True, WHITE)
            start_rect = start_text.get_rect(center=self.start_button_rect.center)
            self.screen.blit(start_text, start_rect)

            # Quit Button
            pygame.draw.rect(self.screen, RED, self.quit_button_rect)
            quit_text = small_font.render("Quit", True, WHITE)
            quit_rect = quit_text.get_rect(center=self.quit_button_rect.center)
            self.screen.blit(quit_text, quit_rect)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = small_font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 10))


# Run the Start Game interface
if __name__ == "__main__":

    choice = input("Type 'new' to start a new game or 'load' to load a saved game: ").strip().lower()
    if choice == 'new':
        start_game = Start_game()
        start_game.start_new_game()
    elif choice == 'load':
        start_game = Start_game()
        start_game.load_saved_game()

    else:
        print("Invalid input. Please type 'new' or 'load'.")
