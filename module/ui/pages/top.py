import flet as ft
from module.ui.components import app_bar

def top_view(page_go) :
    return ft.View(
        "/",
        [
            app_bar.app_bar('メインメニュー'),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text("MIDI変換", size = 20)
                            ),
                            on_click=lambda e: page_go("/midi")
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ])),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text("オマケ機能", size = 20)
                            ),
                            on_click=lambda e: page_go("/appendix")
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ])),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text("ファイルの保存・取込", size = 20)
                            ),
                            on_click=lambda e: page_go("/file_output")
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]))
        ]
    )

