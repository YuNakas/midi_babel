import re
import flet as ft
from _gv import g
from module.util import midi_converter

def convert_end_view(return_top):
    midi_filepath = g.MY_CONF.root_path + '/midi_ready/' + g.MY_STATE.midi_file
    converted_midi_filepath = g.MY_CONF.root_path\
        + '/midi_converted/' + re.sub(r"\..*$", "", g.MY_STATE.midi_file)\
        + "_converted_from_" + re.sub(r"\..*$", "", g.MY_STATE.key_mapping_from_file)\
        + "_to_" + re.sub(r"\..*$", "", g.MY_STATE.key_mapping_to_file) + ".mid"
    midi_converter.midi_converter(midi_filepath, converted_midi_filepath)
    
    return ft.View(
        "/convert_end",
        [
            ft.AppBar(title=ft.Text("変換が完了しました"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Row(
                [
                    ft.ElevatedButton(
                        "Topへ戻る",
                        icon = "CHECK_CIRCLE_OUTLINE",
                        on_click = return_top
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ]
    )