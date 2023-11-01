import flet as ft
from module.ui.components import app_bar, data_table
from _gv import g

def map_view(page_go):
    return ft.View(
        "/map",
        [
            app_bar.app_bar("変換に使うマッピングファイルを選んでください"),
            data_table.create_data_table(g.MY_CONF.mapping_files, on_click)
        ]
    )

def on_click():
    pass