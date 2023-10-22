import flet as ft

def midi_view(create_dataTable, files: list):
    return ft.View(
        "/midi",
        [
            ft.AppBar(title=ft.Text("変換したいmidiファイルを選んでください")),
            create_dataTable(files, "midi")
        ]
    )