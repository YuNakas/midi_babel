import flet as ft
from module.ui.components import app_bar
from gv import g

def appendix_view(page_go):
    def click_btn(callback):
        callback()
        page_go("/midi")

    def click_tautology():
        g.MY_STATE.set_convert_mode("tautology")

    def click_octave_up():
        g.MY_STATE.set_convert_mode("octave_up")
    
    def click_octave_down():
        g.MY_STATE.set_convert_mode("octave_down")

    def create_btn(tooltip: str, label: str, callback):
        return ft.Container(ft.Column([
            ft.Row([
                ft.Container(
                    margin = 8,
                    width = 320,
                    content=ft.Tooltip(
                        message=tooltip,
                        content=ft.OutlinedButton(
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            content=ft.Text(
                                value=label,
                                size=18
                            ),
                            on_click=lambda e: click_btn(callback)
                        )
                    )
                )
            ], alignment=ft.MainAxisAlignment.CENTER)
        ]))

    return ft.View(
        "/appendix",
        [
            app_bar.app_bar("変換モードを選んでください"),
            create_btn(
                tooltip="音階を変更せずにmidiファイルを出力します。\n\
                    1トラックだけ抽出する場合などに使います。",
                label="Tautology",
                callback=click_tautology
            ),
            create_btn(
                tooltip="全てのノートを1オクターブ上げます。",
                label="Octave Up",
                callback=click_octave_up
            ),
            create_btn(
                tooltip="全てのノートを1オクターブ下げます。",
                label="Octave Down",
                callback=click_octave_down
            )
        ]
    )
