import flet as ft

def top_view(to_midi) :
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
                                content = ft.Text("key mapping", size = 30)
                            ),
                            data="key_mapping", on_click=to_midi
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text("midi mapping", size = 30)
                            ),
                            data="midi_mapping", on_click=to_midi
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]))
        ]
    )

