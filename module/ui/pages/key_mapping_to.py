import flet as ft

def key_mapping_to_view(create_dataTable, files: list):
    return ft.View(
        "/key_mapping_to",
        [
            ft.AppBar(title=ft.Text("変換先のキーマップファイルを選んでください")),
            create_dataTable(files, "key_mapping_to")
        ]
    )