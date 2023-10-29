import flet as ft
from _gv import g
from module.util import midi_util

def select_midi_track_view(page_go):
    midi_filepath = g.MY_CONF.root_path + "/midi_ready/" + g.MY_STATE.midi_file
    midi_obj = midi_util.read_midi_obj(midi_filepath)

    def click_melody_button(e):
        g.MY_MIDI.set_track(midi_obj[e.control.data], "melody")
        page_go("/key_mapping_from")

    def click_rhythm_button(e):
        g.MY_MIDI.set_track(midi_obj[e.control.data], "rhythm")
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
                            text="メロディトラックとして選択",
                            data=string,
                            on_click=click_melody_button
                        )
                    )
                ),
                ft.DataCell(
                    content = ft.Container(
                        alignment = ft.alignment.Alignment(0, 0),
                        content = ft.OutlinedButton(
                            text="リズムトラックとして選択",
                            data=string,
                            on_click=click_rhythm_button
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
    for track_name in g.MY_STATE.midi_track_names:
        table.rows.append(create_row(track_name))

    # スクロール可能にする
    lv = ft.ListView(expand = 1, spacing = 0, padding = 0, width = 840)
    lv.controls.append(table)

    return ft.View(
        "/select_midi_track",
        [
            ft.AppBar(title=ft.Text("変換したいmidiトラックを選んでください")),
            lv
        ]
    )