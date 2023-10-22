import flet as ft

def key_mapping_from_view(create_mappingDataTable, go_create_key_mapping_view, files: list):
    return ft.View(
        "/key_mapping_from",
        [
            ft.AppBar(title=ft.Text("変換元のキーマップファイルを選んでください")),
            ft.OutlinedButton(on_click=lambda e: go_create_key_mapping_view("key_mapping_from"), text="新規作成"),
            create_mappingDataTable(files, "key_mapping_from")
        ]
    )