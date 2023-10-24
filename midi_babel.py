import flet as ft
from module import _init
from module.ui import create_view
from _gv import g

def main(page: ft.Page):
    page.title = "MIDI Babel"
    page.window_width = 800
    page.window_height = 600
    create_view.create_view(page)

if __name__ == '__main__':
    # 初期化処理
    _init.init_config()
    _init.init_state()
    
    ft.app(target=main)
