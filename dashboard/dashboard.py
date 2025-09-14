from dashboard.button import Button, Switch
from dashboard.text_area import TextArea
from service.setting import Setting
import pygame

setting = Setting

class Dashboard:
    def __init__(self, screen, setting):
        self.screen = screen
        self.width = setting.width
        self.height = setting.dashboard_height
        self.surface = pygame.Surface((self.width, self.height))
        self._border = 5
        self._buttons_number = 6 #планируемое количество свичей, кнопок и текста
        self._current_data = self.width/self._buttons_number
        
        self.buttons = [Button(self.surface, (210, 210, 250), pygame.Rect(0, 0, self._current_data, self.height), "speed +", (0, 0, 0), setting.font_size),
                        Button(self.surface, (250, 210, 210), pygame.Rect(self._current_data, 0, self._current_data, self.height), "speed -", (0, 0, 0), setting.font_size),
                        Button(self.surface, (210, 250, 210), pygame.Rect(1*self._current_data, 0, self._current_data, self.height), "save genom", (0, 0, 0), setting.font_size),
                        Button(self.surface, (250, 250, 210), pygame.Rect(2*self._current_data, 0, self._current_data, self.height), "new simulation", (0, 0, 0), setting.font_size),
                        Button(self.surface, (255, 0, 0), pygame.Rect(3*self._current_data, 0, self._current_data, self.height), "menu", (0, 0, 0), setting.font_size)]       
        
        self.text_areas = [TextArea(self.surface, (210, 250, 250), pygame.Rect(4*self._current_data, 0, self._current_data, self.height), "itteration: ", (0, 0, 0),setting.font_size)]
        self.switches = [Switch(self.surface, (250, 210, 250), pygame.Rect(5*self._current_data, 0, self._current_data, self.height), "step mode", (0, 0, 0), setting.font_size)]


    def draw(self):
        for obj in self.buttons + self.text_areas + self.switches:
            obj.draw()


    def blit(self, pos):
        self.screen.blit(self.surface, pos)

