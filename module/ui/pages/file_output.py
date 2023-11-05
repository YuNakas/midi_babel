import os
import re
import shutil
import flet as ft
from module.ui.components import app_bar
from gv import g

def file_output_view(page, page_go, return_top):
    def open_scs_dlg(msg):
        dlg = ft.AlertDialog(
            title=ft.Text(
                value=msg,
                size=16
            ),
            on_dismiss=lambda e: return_top(e)
        )

        page.dialog = dlg
        dlg.open = True
        page.update()
    
    def open_err_dlg(msg):
        dlg = ft.AlertDialog(
            title=ft.Text(
                value=msg,
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
                root_dir=g.MY_CONF.get_root_path() + "/assets/key_mapping"
            )
            open_scs_dlg("ファイルの保存が完了しました")
        except:
            open_err_dlg("ファイルの保存に失敗しました")

    def pick_setting_files(e: ft.FilePickerResultEvent):
        if e.files == None:
            return None
        
        temp_setting_path: str = g.MY_CONF.get_root_path() + "/assets/temp/key_mapping"
        if os.path.isdir(temp_setting_path):
            shutil.rmtree(temp_setting_path)
        shutil.unpack_archive(
            filename=e.files[0].path,
            extract_dir=temp_setting_path
        )
        
        try:
            shutil.copytree(
                src=temp_setting_path,
                dst=g.MY_CONF.get_root_path() + "/assets/key_mapping",
                dirs_exist_ok=True
            )
            open_scs_dlg("設定のインポートが完了しました")
            if os.path.isdir(temp_setting_path):
                shutil.rmtree(temp_setting_path)
        except:
            open_err_dlg("設定のインポートに失敗しました")

    save_files_dialog = ft.FilePicker(on_result=save_setting_files)
    page.overlay.append(save_files_dialog)

    pick_files_dialog = ft.FilePicker(on_result=pick_setting_files)
    page.overlay.append(pick_files_dialog)

    return ft.View(
        "/file_output",
        [
            app_bar.app_bar("ファイルのインポート/エクスポートを行います"),
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
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
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
                                    value="設定ファイルを\nインポート",
                                    size=20,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: pick_files_dialog.pick_files(
                                allow_multiple=False,
                                allowed_extensions=["zip"]
                            )
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
                            content=ft.Container(
                                padding = 16,
                                content = ft.Text(
                                    value="変換済みmidiファイルを\nエクスポート",
                                    size=20,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8)
                            ),
                            on_click=lambda e: page_go("/midi_file_output")
                        )
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]))
        ]
    )