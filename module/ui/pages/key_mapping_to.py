import flet as ft
from _gv import g
from module.ui.components import data_table

def key_mapping_to_view(page_go):
    def click_new(): 
        g.MY_STATE.set_from_or_to("to")
        page_go("/create_key_mapping")
    
    def click_select(row_data):
        g.MY_STATE.set_key_mapping_to_file(row_data)
        page_go("/generate_converter")

    def click_edit(row_data):
        g.MY_STATE.set_key_mapping_to_file(row_data)
        page_go("/edit_key_mapping")
    
    return ft.View(
        "/key_mapping_to",
        [
            ft.AppBar(title=ft.Text("変換先のキーマップファイルを選んでください")),
            ft.OutlinedButton(on_click=lambda e: click_new(), text="新規作成"),
            data_table.create_mappingDataTable(g.MY_CONF.key_mapping_files, click_select, click_edit)
        ]
    )