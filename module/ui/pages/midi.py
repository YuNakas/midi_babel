import flet as ft
from module.ui.components import app_bar, data_table
from _gv import g

def midi_view(page_go):
    def on_click(data):
        g.MY_STATE.set_midi_file(data)
        page_go("/select_midi_track")
    
    return ft.View(
        "/midi",
        [
            app_bar.app_bar("変換したいmidiファイルを選んでください"),
            data_table.create_data_table(g.MY_CONF.convert_midi_files, on_click)
        ]
    )
