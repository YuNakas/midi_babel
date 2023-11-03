import flet as ft
from module.ui import create_view

def main(page: ft.Page):
    page.title = "MIDI Babel"
    page.fonts = {
        "NotoSansJP": "/fonts/NotoSansJP-Regular.otf"
    }
    page.theme = ft.Theme(font_family="NotoSansJP")
    page.window_width = 840
    page.window_height = 800
    create_view.create_view(page)

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
