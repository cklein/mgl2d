#!/usr/bin/env python
from mgl2d.app import App
from mgl2d.graphics.screen import Screen

app = App()
screen = Screen(800, 600, 'Test')
screen.print_info()

def draw_frame(screen):
    pass


def update_frame(delta_ms):
    pass


app.run(screen, draw_frame, update_frame)
