import flet as ft
from _gv import g
from module.ui.components import data_table

def midi_view(page_go):
    def on_click(data):
        g.MY_STATE.set_midi_file(data)
        page_go("/select_midi_track")
    
    return ft.View(
        "/midi",
        [
            ft.AppBar(title=ft.Text("変換したいmidiファイルを選んでください")),
            data_table.create_data_table(g.MY_CONF.convert_midi_files, on_click)
        ]
    )
