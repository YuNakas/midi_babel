import flet as ft
from _gv import g

def midi_view(create_dataTable):
    return ft.View(
        "/midi",
        [
            ft.AppBar(title=ft.Text("変換したいmidiファイルを選んでください")),
            create_dataTable(g.MY_CONF.convert_midi_files, "midi")
        ]
    )