import flet as ft

def midi_view(create_dataTable, convert_midi_files):
    return ft.View(
        "/midi",
        [
            ft.AppBar(title=ft.Text("変換したいmidiファイルを選んでください"), bgcolor=ft.colors.SURFACE_VARIANT),
            create_dataTable(convert_midi_files, 'midi')
        ]
    )