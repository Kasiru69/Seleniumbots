import pygame
import sys

class SPEED:
    pygame.init()
    pygame.font.init()
    def __init__(self):
        self.delay=0.5
        self.selected_speed = "Medium"
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (200, 200, 200)
        self.buttons = {"Slow": (100, 100), "Medium": (100, 150), "Fast": (100, 200)}
        self.button2 = {"Continue": (100, 300)}
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.screen = pygame.display.set_mode((400, 400))

    def set_speed(self,selected_speed):
        if selected_speed == "Slow":
            self.delay = 1
        elif selected_speed == "Medium":
            self.delay = 0.5
        elif selected_speed == "Fast":
            self.delay = 0.2
        #print(f"You selected {selected_speed} speed with {self.delay} seconds delay.")
        return self.delay

    def draw_buttons(self):
        for speed, pos in self.buttons.items():
            color = self.BLUE if speed == self.selected_speed else self.GRAY
            pygame.draw.rect(self.screen, color, (*pos, 200, 40))
            button_text = self.small_font.render(speed, True, self.WHITE if color == self.BLUE else self.BLACK)
            self.screen.blit(button_text, (pos[0] + 70, pos[1] + 10))
        for speed, pos in self.button2.items():
            color = self.BLACK
            pygame.draw.rect(self.screen, color, (*pos, 200, 40))
            button_text = self.small_font.render(speed, True, self.WHITE)
            self.screen.blit(button_text, (pos[0] + 70, pos[1] + 10))

    def mainfunc(self):
        pygame.display.set_caption("Typing Speed Selector")

        self.screen.fill(self.WHITE)
        title_text = self.font.render("Select Typing Speed", True, self.BLACK)
        self.screen.blit(title_text, (80, 30))

        self.draw_buttons()
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for speed, pos in self.buttons.items():
                        if pos[0] <= mouse_pos[0] <= pos[0] + 200 and pos[1] <= mouse_pos[1] <= pos[1] + 40:
                            self.selected_speed = speed
                            self.screen.fill(self.WHITE)
                            self.screen.blit(title_text, (80, 30))
                            self.draw_buttons()
                            pygame.display.flip()
                    for speed,pos in self.button2.items():
                        if pos[0] <= mouse_pos[0] <= pos[0] + 200 and pos[1] <= mouse_pos[1] <= pos[1] + 40:
                            return self.set_speed(self.selected_speed)
                            #pygame.quit()
                            #sys.exit()
        return self.delay




