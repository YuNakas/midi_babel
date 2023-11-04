import re
import flet as ft
from module.util import midi_converter
from module.ui.components import app_bar
from gv import g

def convert_end_view(return_top):
    midi_filepath = g.MY_CONF.get_root_path() + '/assets/midi_ready/' + g.MY_STATE.get_midi_file()
    converted_midi_filepath = g.MY_CONF.get_root_path()\
        + '/assets/midi_converted/' + re.sub(r"\..*$", "", g.MY_STATE.get_midi_file())\
        + "_converted_from_" + re.sub(r"\..*$", "", g.MY_STATE.get_key_mapping_from_file())\
        + "_to_" + re.sub(r"\..*$", "", g.MY_STATE.get_key_mapping_to_file()) + ".mid"
    midi_converter.midi_converter(midi_filepath, converted_midi_filepath)
    
    return ft.View(
        "/convert_end",
        [
            app_bar.app_bar("変換が完了しました"),
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