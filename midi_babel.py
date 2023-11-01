import flet as ft
from module import _init
from module.ui import create_view
from _gv import g

def main(page: ft.Page):
    page.title = "MIDI Babel"
    page.window_width = 840
    page.window_height = 800
    create_view.create_view(page)
    page.fonts = {
        "NotoSansJP": "/fonts/NotoSansJP-Regular.otf"
    }
    page.theme = ft.Theme(font_family="NotoSansJP")

if __name__ == '__main__':
    # 初期化処理
    _init.init_config()
    _init.init_state()
    _init.init_midi()
    
    ft.app(target=main, assets_dir="assets")
