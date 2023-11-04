import flet as ft
from module.ui.components import app_bar
from gv import g

def create_key_mapping_view(page_go):
    def go_edit_key_mapping_view(string):
        if g.MY_STATE.get_from_or_to() == "from":
            g.MY_STATE.set_key_mapping_from_file(string + ".yml")
        if g.MY_STATE.get_from_or_to() == "to":
            g.MY_STATE.set_key_mapping_to_file(string + ".yml")
        g.MY_STATE.set_key_mapping_edit_file(string + ".yml")
        page_go("/edit_key_mapping")
    
    text_field_text = ""
    annotation = ft.Text(color=ft.colors.RED)

    def change_text(e):
        nonlocal text_field_text
        text_field_text = e.control.value
    
    def on_click_determined(text_field_text):
        if (text_field_text + ".yml") in g.MY_CONF.get_key_mapping_files() or text_field_text == "":
            nonlocal annotation
            annotation.value = "すでに存在するファイル名か、ファイル名が入力されていません"
            textField_row.update()
        else:
            go_edit_key_mapping_view(text_field_text)
    
    textField_row = ft.Row(
        controls=[
            ft.TextField(on_change=change_text),
            ft.OutlinedButton(
                text="決定",
                on_click=lambda e: on_click_determined(text_field_text)
            ),
            annotation
        ]
    )

    return ft.View(
        "/create_key_mapping",
        [
            app_bar.app_bar("キーマップファイル名を入力してください"),
            textField_row
        ]
    )

