import flet as ft
from module import _init
from module.ui import create_view

# 初期化処理
conf = _init.init_config()

def main(page: ft.Page):
    page.title = "MIDI Babel"
    page.window_width = 800
    page.window_height = 600
    create_view.create_view(page, conf)

ft.app(target=main)
