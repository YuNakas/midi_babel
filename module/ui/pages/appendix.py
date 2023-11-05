import os
import shutil
import flet as ft
from module.ui.components import app_bar, data_table
from gv import g

def appendix_view(page_go):
    def click_tautology(e):
        pass

    def click_octave_up(e):
        pass
    
    def click_octave_down(e):
        pass

    def create_btn(tooltip: str, label: str, callback):
        return ft.Tooltip(
            message=tooltip,
            content=ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content=ft.OutlinedButton(
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            content=ft.Text(
                                value=label,
                                size=18
                            ),
                            on_click=lambda e: callback
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]))
        )

    return ft.View(
        "/appendix",
        [
            app_bar.app_bar("変換モードを選んでください"),
            create_btn(
                tooltip="音階を変更せずにmidiファイルを出力します。",
                label="Tautology",
                callback=click_tautology
            ),
            create_btn(
                tooltip="hoge",
                label="Octave Up",
                callback=click_octave_up
            ),
            create_btn(
                tooltip="hoge",
                label="Octave Down",
                callback=click_octave_down
            )
        ]
    )
