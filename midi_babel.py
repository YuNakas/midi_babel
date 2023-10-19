import flet as ft
from module import _init, create_view

# 初期化処理
conf = _init.init_config()

def main(page: ft.Page):
    page.title = "MIDI Babel"
    create_view.create_view(page, conf)

ft.app(target=main)
