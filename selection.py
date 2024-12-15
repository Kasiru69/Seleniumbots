import pygame
import sys

class Selection:
    pygame.init()
    def __init__(self):
        self.title = "Select a Bot"
        self.WIDTH = 500
        self.HEIGHT = 300
        self.BG_COLOR = (30, 30, 30)
        self.BUTTON_COLOR = (70, 130, 180)
        self.BUTTON_HOVER_COLOR = (100, 149, 237)
        self.TEXT_COLOR = (255, 255, 255)
        self.FONT = pygame.font.Font(None, 36)
        self.typing_bot_button = pygame.Rect(150, 80, 200, 50)
        self.dino_bot_button = pygame.Rect(150, 160, 200, 50)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))


    def draw_button(self,screen, rect, text, is_hovered):
        color = self.BUTTON_HOVER_COLOR if is_hovered else self.BUTTON_COLOR
        pygame.draw.rect(screen, color, rect, border_radius=10)
        text_surface = self.FONT.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    def main_menu(self):

        pygame.display.set_caption(self.title)
        while True:
            self.screen.fill(self.BG_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.typing_bot_button.collidepoint(mouse_pos):
                        print("Typing Bot selected!")
                        return "typing_bot"
                    elif self.dino_bot_button.collidepoint(mouse_pos):
                        print("Dino Bot selected!")
                        return "dino_bot"

            mouse_pos = pygame.mouse.get_pos()

            self.draw_button(self.screen, self.typing_bot_button, "Typing Bot", self.typing_bot_button.collidepoint(mouse_pos))
            self.draw_button(self.screen, self.dino_bot_button, "Dino Bot", self.dino_bot_button.collidepoint(mouse_pos))

            pygame.display.flip()

