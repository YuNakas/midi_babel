import flet as ft

def file_select_view(create_dataTable, files: list, message: str, page_id: str):
    return ft.View(
        "/" + page_id,
        [
            ft.AppBar(title=ft.Text(message)),
            create_dataTable(files, page_id)
        ]
    )