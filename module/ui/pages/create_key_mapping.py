import flet as ft
from _gv import g

def create_key_mapping_view(go_edit_key_mapping_view):
    text_field_text = ""
    annotation = ft.Text(color=ft.colors.RED)

    def change_text(e):
        nonlocal text_field_text
        text_field_text = e.control.value
    
    def on_click_determined(text_field_text):
        if (text_field_text + ".yml") in g.MY_CONF.key_mapping_files or text_field_text == "":
            nonlocal annotation
            annotation.value = "すでに存在するファイル名か、ファイル名が入力されていません"
            textField_row.update()
        else:
            go_edit_key_mapping_view(text_field_text)
    textField = ft.TextField(
        on_change=change_text
    ),
    btn = ft.OutlinedButton(
        text="決定",
        on_click=lambda e: on_click_determined()
    )
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
            ft.AppBar(title=ft.Text("キーマップファイル名を入力してください")),
            textField_row
        ]
    )

