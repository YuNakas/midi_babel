import flet as ft

def map_view(create_dataTable, files: list):
    return ft.View(
        "/map",
        [
            ft.AppBar(title=ft.Text("変換に使うマッピングファイルを選んでください")),
            create_dataTable(files, "map")
        ]
    )