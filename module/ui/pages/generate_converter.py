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

import re
import flet as ft
from module.ui.components import app_bar
from module.util import yaml_util, create_midi_map
from gv import g

def load_key_mapping(file_path):
    return yaml_util.load_yaml(g.MY_CONF.get_root_path() + "/assets/key_mapping/" + file_path)

def generate_converter_view(page_go):
    key_map_from_obj = load_key_mapping(g.MY_STATE.get_key_mapping_from_file())
    key_map_to_obj = load_key_mapping(g.MY_STATE.get_key_mapping_to_file())
    g.MY_STATE.set_map_cache_fileName(re.sub(r"\..*$", "", g.MY_STATE.get_key_mapping_from_file()) + "_" + re.sub(r"\..*$", "", g.MY_STATE.get_key_mapping_to_file()) + ".yml")

    def load_map_cache():
        map_cache_fileName = g.MY_STATE.get_map_cache_fileName()

        map_obj = {}
        if map_cache_fileName in g.MY_CONF.get_map_cache_files():
            map_obj = (yaml_util.load_yaml(g.MY_CONF.get_root_path() + "/assets/key_mapping/_map_caches/" + map_cache_fileName))

        return map_obj
    gen_map_obj = load_map_cache()

    def create_convertTable():
        table = ft.DataTable(
            heading_row_height=40,
            width = 800,
            columns=[
                ft.DataColumn(ft.Text(
                    value="変換元",
                    size = 18,
                    height=40
                )),
                ft.DataColumn(ft.Text(
                    value="変換先",
                    size = 18,
                    height=40
                ))
            ],
            rows=create_row()
        )
        
        # スクロール可能にする
        lv = ft.ListView(expand=1)
        lv.controls.append(table)
        return lv

    def create_row():
        rtnRows = []
        for key in key_map_from_obj.keys():
            cache_text = ""
            if key in gen_map_obj:
                cache_text = gen_map_obj[key]
            rtnRows.append(ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Container(
                            content = ft.Text(
                                height=32,
                                size=16,
                                value=key,
                                text_align = ft.TextAlign.CENTER
                            ),
                            height=32,
                            padding=0,
                            margin=0
                        )
                    ),
                    ft.DataCell(
                        ft.Container(
                            content = ft.Dropdown(
                                key = key,
                                hint_text = cache_text,
                                content_padding=ft.padding.symmetric(0, 8),
                                height=32,
                                options = create_options(key_map_to_obj.keys()),
                                on_change = lambda e: change_dropdown(e)
                            ),
                            height=32,
                            padding=0,
                            margin=0
                        )
                    )
                ]
            ))
        
        return rtnRows
        
    def create_options(strings):
        rtnOptions = []
        for string in strings:
            rtnOptions.append(ft.dropdown.Option(string))
        
        return rtnOptions

    def change_dropdown(e):
        nonlocal gen_map_obj
        gen_map_obj[e.control.key] = e.data

    def next(e):
        create_midi_map.create_midi_map(gen_map_obj, key_map_from_obj, key_map_to_obj)
        yaml_util.save_yaml(gen_map_obj, g.MY_CONF.get_root_path() + "/assets/key_mapping/_map_caches/" + g.MY_STATE.get_map_cache_fileName())
        page_go("/convert_end")

    return ft.View(
        "/generate_converter",
        [
            app_bar.app_bar("変換表を生成します"),
            ft.Container(
                padding = 0,
                content = ft.OutlinedButton(
                    on_click = next,
                    content=ft.Text("決定"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8)
                    )
                )
            ),
            create_convertTable(),
        ]
    )
