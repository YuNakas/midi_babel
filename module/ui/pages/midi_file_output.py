import os
import re
import shutil
import flet as ft
from module.ui.components import app_bar
from gv import g

def midi_file_output_view(page, return_top):
    clicked_filename = ""
    def row_click(row_str: str):
        nonlocal clicked_filename
        clicked_filename = row_str
        save_file_dialog.save_file(
            file_name=clicked_filename,
            allowed_extensions=["mid"]
        )

    def create_rows(): 
        rtnRows = []
        for string in g.MY_CONF.get_converted_midi_files(): 
            rtnRows.append(ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Container(
                            width = 800,
                            padding = 0,
                            margin = 0,
                            data = string,
                            alignment = ft.alignment.Alignment(-0.95, 0),
                            content = ft.Text(
                                value = string
                            ),
                            on_click = lambda e: row_click(e.control.data)
                        )
                    )
                ],
            ))
        return rtnRows
    
    table = ft.DataTable(
        width = 800,
        column_spacing=0,
        columns=[
            ft.DataColumn(
                label = ft.Container(
                    width = 800,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(-0.95, 0),
                    content = ft.Text(
                        value = "ファイル名",
                        size = 18
                    )
                )
            )
        ],
        rows=create_rows(),
    )

    # スクロール可能にする
    lv = ft.ListView(expand=1)
    lv.controls.append(table)

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

    def save_midi_file(e: ft.FilePickerResultEvent):
        if e.path == None:
            return None
        
        try:
            shutil.copy(
                src=g.MY_CONF.get_root_path() + "/assets/midi_converted/" + clicked_filename,
                dst=e.path
            )
            open_scs_dlg()

        except:
            open_err_dlg()

    save_file_dialog = ft.FilePicker(on_result=save_midi_file)
    page.overlay.append(save_file_dialog)
    return ft.View(
        "/midi_file_output",
        [
            app_bar.app_bar("エクスポートするファイルを選んでください"),
            lv
        ]
    )