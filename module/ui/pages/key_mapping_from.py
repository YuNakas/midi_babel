import flet as ft

def key_mapping_from_view(create_dataTable, files: list):
    return ft.View(
        "/key_mapping_from",
        [
            ft.AppBar(title=ft.Text("変換元のキーマップファイルを選んでください")),
            create_dataTable(files, "key_mapping_from")
        ]
    )