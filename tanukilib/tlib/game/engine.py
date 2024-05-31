import sys
import pygame
from tlib.graphics.graphics import BGRA


class TanuGameEngine:
    """TANU Game Engine"""

    def __init__(self, 
            wnd_width:int = 800,
            wnd_height:int = 640,
            fps:int = 60,
            draw_fps:bool = False,
            caption:str = "TANU GAME (=^_^=)",
            start_after_right_after_init:bool = False,
            base_background_fill_color:BGRA = BGRA(0, 0, 0)):
        print("initialize pygame engine...")
        pygame.init()
        pygame.display.set_caption(caption)
        self._fps = fps
        self.wnd_width = wnd_height
        self.wnd_height = wnd_height
        self.base_background_fill_color = base_background_fill_color
        print("initialize display...")
        self.scr = pygame.display.set_mode((wnd_width, wnd_height))
        print("initialize default background...")
        self.bg = pygame.surface.Surface((wnd_width, wnd_height))
        self.bg.fill(base_background_fill_color.to_tuple_rgb())
        self.scr.blit(self.bg, (0, 0))
        print("initialize clock ...")
        self.clock = pygame.time.Clock()
        self.draw_fps = draw_fps
        self._main_loop = False
        pygame.display.flip()
        print("TANU initialization done.")
        if start_after_right_after_init:
            self.start()


    def start(self):
        """Start TANU game engine"""
        self._main_loop = True

        print("starting TANU..")

        while self._main_loop:
            if self.draw_fps:
                self.scr.blit(self.fps_to_str(), (10, 30))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._main_loop = False
                
            self.clock.tick(self._fps)
            pygame.display.flip()


    def fps_to_str(self):
        """Update FPS description on window"""
        fps = str(f"{int(self.clock.get_fps())} FPS")
        fps_text = self.font.render(fps, True, pygame.Color("coral"))
        print(fps_text)
        return fps_text



    @property
    def fps(self) -> int:
        return self._fps

    