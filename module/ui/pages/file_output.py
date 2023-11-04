import os
import re
import shutil
import flet as ft
from module.ui.components import app_bar
from gv import g

def file_output_view(page, page_go, return_top):
    def open_scs_dlg():
        dlg = ft.AlertDialog(
            title=ft.Text(
                value="ファイルの保存が完了しました",
                size=16
            ),
            on_dismiss=lambda e: return_top(e)
        )

        page.dialog = dlg
        dlg.open = True
        page.update()
    
    def open_err_dlg():
        dlg = ft.AlertDialog(
            title=ft.Text(
                value="ファイルの保存に失敗しました",
                size=16
            ),
            on_dismiss=lambda e: print(e)
        )

        page.dialog = dlg
        dlg.open = True
        page.update()

    def save_setting_files(e: ft.FilePickerResultEvent):
        if e.path == None:
            return None
        
        output_path = re.sub(r"\.zip$", "", e.path)

        try:
            shutil.make_archive(
                base_name=output_path,
                format="zip",
                root_dir=g.MY_CONF.get_root_path() + "/key_mapping"
            )
            open_scs_dlg()
        except:
            open_err_dlg()

    save_files_dialog = ft.FilePicker(on_result=save_setting_files)
    page.overlay.append(save_files_dialog)
    return ft.View(
        "/file_output",
        [
            app_bar.app_bar("エクスポートするファイルを選んでください"),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text(
                                    value="設定ファイルを\nエクスポート",
                                    size=20,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            on_click=lambda e: save_files_dialog.save_file(
                                file_name="midi_babel_settings.zip",
                                allowed_extensions=["zip"]
                            )
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),
            ])),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text(
                                    value="変換済みmidiファイルを\nエクスポート",
                                    size=20,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            on_click=lambda e: page_go("/midi_file_output")
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]))
        ]
    )