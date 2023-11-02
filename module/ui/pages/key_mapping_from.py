import flet as ft
from module.ui.components import app_bar, data_table
from gv import g

def key_mapping_from_view(page_go):
    def click_new(): 
        g.MY_STATE.set_from_or_to("from")
        page_go("/create_key_mapping")
    
    def click_select(row_data):
        g.MY_STATE.set_key_mapping_from_file(row_data)
        page_go("/key_mapping_to")

    def click_edit(row_data):
        g.MY_STATE.set_key_mapping_from_file(row_data)
        g.MY_STATE.set_from_or_to("from")
        page_go("/edit_key_mapping")
    
    return ft.View(
        "/key_mapping_from",
        [
            app_bar.app_bar("変換元のキーマップファイルを選んでください"),
            ft.OutlinedButton(on_click=lambda e: click_new(), text="新規作成"),
            data_table.create_mappingDataTable(g.MY_CONF.key_mapping_files, click_select, click_edit)
        ]
    )
