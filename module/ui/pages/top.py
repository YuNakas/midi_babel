import flet as ft

def top_view(page_go) :
    return ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text('変換方式を選んでください'), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text("key mapping", size = 20)
                            ),
                            data="key_mapping", on_click=lambda e: page_go("/midi")
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]))
        ]
    )

