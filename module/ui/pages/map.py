import flet as ft
from _gv import g
from module.ui.components import data_table

def map_view(page_go):
    return ft.View(
        "/map",
        [
            ft.AppBar(title=ft.Text("変換に使うマッピングファイルを選んでください")),
            data_table.create_data_table(g.MY_CONF.mapping_files, on_click)
        ]
    )

def on_click():
    pass