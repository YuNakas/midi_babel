import os
import shutil
import flet as ft
from module.ui.components import app_bar, data_table
from gv import g

def midi_view(page, page_go, return_top):
    def on_click(data):
        g.MY_STATE.set_midi_file(data)
        page_go("/select_midi_track")

    def reload_this_page(e):
        return_top(e)
        page_go("/midi")

    def open_scs_dlg():
        dlg = ft.AlertDialog(
            title=ft.Text(
                value="ファイル取込が完了しました",
                size=16
            ),
            on_dismiss=lambda e: reload_this_page(e)
        )

        page.dialog = dlg
        dlg.open = True
        page.update()

    def open_err_dlg():
        dlg = ft.AlertDialog(
            title=ft.Text(
                value="ファイル取込に失敗しました",
                size=16
            ),
            on_dismiss=lambda e: print(e)
        )

        page.dialog = dlg
        dlg.open = True
        page.update()

    def file_import(e: ft.FilePickerResultEvent):
        if e.files == None:
            return None
        
        try:
            shutil.copy(
                src=e.files[0].path,
                dst=g.MY_CONF.get_root_path() + "/assets/midi_ready/" + os.path.basename(e.files[0].path)
            )
            open_scs_dlg()

        except:
            open_err_dlg()

    pick_file_dialog = ft.FilePicker(on_result=file_import)
    page.overlay.append(pick_file_dialog)

    def create_rows(): 
        rtnRows = []
        for string in g.MY_CONF.get_convert_midi_files(): 
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
                            on_click = lambda e: on_click(e.control.data)
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

    return ft.View(
        "/midi",
        [
            app_bar.app_bar("変換したいmidiファイルを選んでください"),
            ft.Container(
                padding=0,
                content=ft.OutlinedButton(
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    text="ファイルの取り込み",
                    on_click=lambda e: pick_file_dialog.pick_files(
                        allowed_extensions=["mid"],
                        allow_multiple=False
                    )
                )
            ),
            data_table.create_data_table(g.MY_CONF.get_convert_midi_files(), on_click)
        ]
    )
