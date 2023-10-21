import flet as ft

def map_view(create_dataTable, mapping_files): 
    return ft.View(
        "/map",
        [
            ft.AppBar(title=ft.Text("変換に使うマッピングファイルを選んでください"), bgcolor=ft.colors.SURFACE_VARIANT),
            create_dataTable(mapping_files, 'map')
        ],
    )