import flet as ft
from _gv import g

def map_view(create_dataTable):
    return ft.View(
        "/map",
        [
            ft.AppBar(title=ft.Text("変換に使うマッピングファイルを選んでください")),
            create_dataTable(g.MY_CONF.mapping_files, "map")
        ]
    )