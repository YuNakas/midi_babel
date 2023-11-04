import flet as ft
from module.ui.components import app_bar
from module.util import midi_util
from gv import g

def select_midi_track_view(page_go):
    midi_filepath = g.MY_CONF.get_root_path() + "/assets/midi_ready/" + g.MY_STATE.get_midi_file()
    midi_obj = midi_util.read_midi_obj(midi_filepath)

    def click_button(e, button_type: str):
        if "setting_track" in midi_obj.keys():
            g.MY_MIDI.set_setting_track(midi_obj["setting_track"])
        g.MY_MIDI.set_track(midi_obj[e.control.data], button_type)
        page_go("/key_mapping_from")

    def create_row(string):
        return ft.DataRow(
            cells=[
                ft.DataCell(
                    content = ft.Container(
                        alignment = ft.alignment.Alignment(-0.8, 0),
                        content = ft.Text(string)
                    )
                ),
                ft.DataCell(
                    content = ft.Container(
                        alignment = ft.alignment.Alignment(0, 0),
                        content = ft.OutlinedButton(
                            content=ft.Text(
                                value="メロディトラックとして選択",
                                size=12
                            ),
                            data=string,
                            on_click=lambda e: click_button(e, "melody")
                        )
                    )
                ),
                ft.DataCell(
                    content = ft.Container(
                        alignment = ft.alignment.Alignment(0, 0),
                        content = ft.OutlinedButton(
                            content=ft.Text(
                                value="リズムトラックとして選択",
                                size=12
                            ),
                            data=string,
                            on_click=lambda e: click_button(e, "rhythm")
                        )
                    )
                )
            ]
        )

    table = ft.DataTable(
        width = 800,
        column_spacing = 0,
        horizontal_margin = 0,
        columns=[
            ft.DataColumn(
                label = ft.Container(
                    width = 360,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(-0.8, 0),
                    content = ft.Text(
                        value = "ファイル名",
                        size = 18
                    )
                ),
            ),
            ft.DataColumn(
                label = ft.Container(
                    width = 220,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(0, 0),
                    content = ft.Text("")
                )
            ),
            ft.DataColumn(
                label = ft.Container(
                    width = 220,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(0, 0),
                    content = ft.Text("")
                )
            )
        ]
    )
    for track_name in g.MY_STATE.get_midi_track_names():
        table.rows.append(create_row(track_name))

    # スクロール可能にする
    lv = ft.ListView(expand = 1, spacing = 0, padding = 0, width = 840)
    lv.controls.append(table)

    return ft.View(
        "/select_midi_track",
        [
            app_bar.app_bar("変換したいmidiトラックを選んでください"),
            lv
        ]
    )