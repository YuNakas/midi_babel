import flet as ft

def key_mapping_to_view(create_mappingDataTable, go_create_key_mapping_view, files: list):
    return ft.View(
        "/key_mapping_to",
        [
            ft.AppBar(title=ft.Text("変換先のキーマップファイルを選んでください")),
            ft.OutlinedButton(on_click=lambda e: go_create_key_mapping_view("key_mapping_to"), text="新規作成"),
            create_mappingDataTable(files, "key_mapping_to")
        ]
    )