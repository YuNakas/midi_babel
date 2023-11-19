"""
Copyright (C) 2023  Yu Nakas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
            ])),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.TextButton(
                            text = "マニュアル(外部リンク)",
                            url = "https://yunakas.github.io/midi_babel/midi_babel_manual/"
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.alignment.bottom_center))
        ]
    )

