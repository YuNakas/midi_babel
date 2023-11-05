import flet as ft
from module.ui.components import app_bar
from module.util import yaml_util
from gv import g

def edit_key_mapping_view(page_go):
    new_key_name: str = ""
    key_mapping_edit_file: str = ""
    if g.MY_STATE.get_from_or_to() == 'from':
        key_mapping_edit_file = g.MY_STATE.get_key_mapping_from_file()
    if g.MY_STATE.get_from_or_to() == 'to':
        key_mapping_edit_file = g.MY_STATE.get_key_mapping_to_file()

    if key_mapping_edit_file in g.MY_CONF.get_key_mapping_files():
        key_map_obj = yaml_util.load_yaml(g.MY_CONF.get_root_path() + "/assets/key_mapping/" + key_mapping_edit_file)
    else:
        key_map_obj = {}
    annotation: ft.Text = ft.Text(color=ft.colors.RED)

    def create_row(keyStr: str):
        return ft.DataRow(
            data=keyStr,
            cells=[
                ft.DataCell(ft.Text(keyStr)),
                ft.DataCell(
                    ft.Container(
                        content = ft.TextField(
                            content_padding=ft.padding.symmetric(0, 8),
                            data=keyStr,
                            text_size=13,
                            value=str(key_map_obj[keyStr]["primary"]),
                            on_change=lambda e: on_change_primary(e),
                        ),
                        height=32,
                        padding=0,
                        margin=0
                    )
                ),
                ft.DataCell(
                    ft.Container(
                        content = ft.TextField(
                            content_padding=ft.padding.symmetric(0, 8),
                            data=keyStr,
                            text_size=13,
                            value=", ".join(map(str, key_map_obj[keyStr]["note"])),
                            hint_text="カンマ区切りで入力(e.g. 3,5,8)",
                            on_change=lambda e: on_change_note(e)
                        ),
                        height=32,
                        padding=0,
                        margin=0
                    )
                ),
                ft.DataCell(ft.OutlinedButton(
                    content = ft.Text("削除"),
                    data = keyStr,
                    style = ft.ButtonStyle(
                        color=ft.colors.RED,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    on_click = row_delete
                ))
            ]
        )

    def change_text(e):
        nonlocal new_key_name
        new_key_name = e.control.value
    def add_key(string):
        nonlocal annotation
        nonlocal key_map_obj
        new_key_text_field.controls.append(annotation)
        if string == "" or string in key_map_obj.keys():
            annotation.value = "キーが入力されていないか、すでに存在するキーです"
        else:
            key_map_obj[string] = {
                "primary": "",
                "note": []
            }

            key_map_row = create_row(string)
            key_map_dataTable.rows.append(key_map_row)
            annotation.value = ""
        new_key_text_field.update()
        key_map_dataTable.update()
    new_key_text_field = ft.Row(
        alignment=ft.alignment.Alignment(-0.8, 0),
        height=32,
        controls=[
            ft.Container(
                content=ft.TextField(
                    content_padding=ft.padding.symmetric(0, 8),
                    height=32,
                    text_align=ft.alignment.Alignment(-0.8, 0),
                    on_change=change_text
                ),
                height=32,
                padding=0,
                margin=0
            ),
            ft.OutlinedButton(on_click=lambda e: add_key(new_key_name), text="追加")
        ]
    )

    def next():
        save_setting()
        if g.MY_STATE.get_from_or_to() == "from":
            page_go("/key_mapping_to")
        if g.MY_STATE.get_from_or_to() == "to":
            page_go("/generate_converter")
    def save_setting():
        nonlocal key_map_obj
        yaml_util.save_yaml(key_map_obj, g.MY_CONF.get_root_path() + "/assets/key_mapping/" + key_mapping_edit_file)
    determined_button = ft.Container(ft.Column([
        ft.Row(
            controls=[
                ft.OutlinedButton(
                    content = ft.Text("保存"),
                    on_click=lambda e: save_setting()
                ),
                ft.Container(
                    padding=0,
                    margin=0,
                    content = ft.OutlinedButton(
                        content = ft.Text("この内容で決定する"),
                        style = ft.ButtonStyle(color=ft.colors.RED),
                        on_click=lambda e: next()
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.END
        )
    ]))

    def row_delete(e):
        nonlocal key_map_obj
        for row in key_map_dataTable.rows:
            if row.data == e.control.data:
                key_map_dataTable.rows.remove(row)
        key_map_dataTable.update()
        del key_map_obj[e.control.data]
    def on_change_primary(e):
        nonlocal key_map_obj
        key_map_obj[e.control.data]["primary"] = e.control.value.replace(" ", "")
    def on_change_note(e):
        nonlocal key_map_obj
        note_str = e.control.value.replace(" ", "")
        key_map_obj[e.control.data]["note"] = note_str.split(",")

    key_map_dataTable = ft.DataTable(
        width=780,
        column_spacing=20,
        horizontal_margin=0,
        columns=[
            ft.DataColumn(
                label = ft.Container(
                    width=180,
                    content=ft.Text("ファイル名")
                )
            ),
            ft.DataColumn(
                label = ft.Container(
                    width=80,
                    content=ft.Text("優先ノート")
                )
            ),
            ft.DataColumn(
                label = ft.Container(
                    width=270,
                    content=ft.Text("ノート一覧")
                )
            ),
            ft.DataColumn(
                label = ft.Container(
                    width=80,
                    content=ft.Text("")
                )
            )
        ]
    )
    for key in key_map_obj.keys(): 
        key_map_dataTable.rows.append(create_row(key))

    # スクロール可能にする
    key_map_lv = ft.ListView(expand=1, padding=ft.padding.symmetric(0, 10))
    key_map_lv.controls.append(key_map_dataTable)

    return ft.View(
        "/edit_key_mapping",
        [
            app_bar.app_bar("キーマップを編集してください"),
            determined_button,
            new_key_text_field,
            key_map_lv
        ]
    )
