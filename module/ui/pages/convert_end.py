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

import os
import re
import shutil
import flet as ft
from module.util import midi_converter
from module.ui.components import app_bar
from gv import g

def convert_end_view(page, return_top):
    converted_midi_filepath = g.MY_CONF.get_root_path()\
        + '/assets/midi_converted/' + re.sub(r"\..*$", "", g.MY_STATE.get_midi_file())\
        + "_converted_from_" + re.sub(r"\..*$", "", g.MY_STATE.get_key_mapping_from_file())\
        + "_to_" + re.sub(r"\..*$", "", g.MY_STATE.get_key_mapping_to_file()) + ".mid"
    midi_converter.midi_converter(converted_midi_filepath)

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

    def save_midi_files(e: ft.FilePickerResultEvent):
        if e.path == None:
            return None

        try:
            shutil.copy(
                src=converted_midi_filepath,
                dst=e.path
            )
            open_scs_dlg("ファイルの保存が完了しました")
        except:
            open_err_dlg("ファイルの保存に失敗しました")

    save_files_dialog = ft.FilePicker(on_result=save_midi_files)
    page.overlay.append(save_files_dialog)

    return ft.View(
        "/convert_end",
        [
            app_bar.app_bar("変換が完了しました"),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            text="MIDIエクスポート",
                            on_click = lambda e: save_files_dialog.save_file(
                                file_name=os.path.basename(converted_midi_filepath),
                                allowed_extensions=["mid"]
                            )
                        )
                    )
                ],alignment=ft.MainAxisAlignment.CENTER)
            ])),
            ft.Container(ft.Column([
                ft.Row([
                    ft.Container(
                        margin = 8,
                        width = 320,
                        content = ft.OutlinedButton(
                            text="Topへ戻る",
                            icon = "CHECK_CIRCLE_OUTLINE",
                            on_click = return_top
                        )
                    )
                ],alignment=ft.MainAxisAlignment.CENTER)
            ]))
        ]
    )