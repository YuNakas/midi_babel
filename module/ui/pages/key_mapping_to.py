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

import flet as ft
from module.ui.components import app_bar, data_table
from gv import g

def key_mapping_to_view(page_go):
    def click_new(): 
        g.MY_STATE.set_from_or_to("to")
        page_go("/create_key_mapping")
    
    def click_select(row_data):
        g.MY_STATE.set_key_mapping_to_file(row_data)
        page_go("/generate_converter")

    def click_edit(row_data):
        g.MY_STATE.set_key_mapping_to_file(row_data)
        g.MY_STATE.set_from_or_to("to")
        page_go("/edit_key_mapping")
    
    return ft.View(
        "/key_mapping_to",
        [
            app_bar.app_bar("変換先のキーマップファイルを選んでください"),
            ft.OutlinedButton(on_click=lambda e: click_new(), text="新規作成"),
            data_table.create_mappingDataTable(g.MY_CONF.get_key_mapping_files(), click_select, click_edit)
        ]
    )