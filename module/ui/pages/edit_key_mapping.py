import flet as ft
from module.util import yaml_util
from _gv import g

def edit_key_mapping_view(go_next_page_from_edit_key, key_mapping_edit_file):
    new_key_name = ""
    if key_mapping_edit_file in g.MY_CONF.key_mapping_files:
        key_map_obj = yaml_util.load_yaml(g.MY_CONF.root_path + "/key_mapping/" + key_mapping_edit_file)
    else:
        key_map_obj = {}
    annotation = ft.Text(color=ft.colors.RED)

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
            key_map_obj[string] = {}

            key_map_row = ft.DataRow(
                data = string,
                cells = [
                    ft.DataCell(ft.Text(string)),
                    ft.DataCell(ft.TextField(
                        data=string,
                        value="",
                        on_change=lambda e: on_change_primary(e)
                    )),
                    ft.DataCell(ft.TextField(
                        data=string,
                        value="",
                        hint_text="カンマ区切りで入力(e.g. 3,5,8)",
                        on_change=lambda e: on_change_note(e)
                    )),
                    ft.DataCell(ft.OutlinedButton(
                        content = ft.Text("削除"),
                        data = string,
                        style = ft.ButtonStyle(color=ft.colors.RED),
                        on_click = row_delete
                    ))
                ]
            )
            key_map_dataTable.rows.append(key_map_row)
            annotation.value = ""
        new_key_text_field.update()
        key_map_dataTable.update()
    new_key_text_field = ft.Row(controls=[
        ft.TextField(on_change=change_text),
        ft.OutlinedButton(on_click=lambda e: add_key(new_key_name), text="追加")
    ])

    def next():
        save_setting()
        go_next_page_from_edit_key()
    def save_setting():
        nonlocal key_map_obj
        yaml_util.save_yaml(key_map_obj, g.MY_CONF.root_path + "/key_mapping/" + key_mapping_edit_file)
    determined_button = ft.Container(ft.Column([
        ft.Row([
            ft.OutlinedButton(
                content = ft.Text("保存"),
                on_click=lambda e: save_setting()
            ),
            ft.Container(
                margin = 8,
                content = ft.OutlinedButton(
                    content = ft.Text("この内容で決定する"),
                    style = ft.ButtonStyle(color=ft.colors.RED),
                    on_click=lambda e: next()
                )
            )
        ], alignment=ft.MainAxisAlignment.END)
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
        width=800,
        data_row_min_height = 80,
        data_row_max_height = 80,
        columns=[
            ft.DataColumn(
                label = ft.Container(
                    width=80,
                    content=ft.Text("ファイル名")
                )
            ),
            ft.DataColumn(
                label = ft.Container(
                    width=60,
                    content=ft.Text("優先ノート")
                )
            ),
            ft.DataColumn(
                label = ft.Container(
                    width=320,
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
        key_map_dataTable.rows.append(ft.DataRow(
            data=key,
            cells=[
                ft.DataCell(ft.Text(key)),
                ft.DataCell(
                    ft.TextField(
                        data=key,
                        value=str(key_map_obj[key]["primary"]),
                        on_change=lambda e: on_change_primary(e),
                    )
                ),
                ft.DataCell(
                    ft.TextField(
                        data=key,
                        value=", ".join(map(str, key_map_obj[key]["note"])),
                        hint_text="カンマ区切りで入力(e.g. 3,5,8)",
                        on_change=lambda e: on_change_note(e)
                    )
                ),
                ft.DataCell(ft.OutlinedButton(
                    content = ft.Text("削除"),
                    data = key,
                    style = ft.ButtonStyle(color=ft.colors.RED),
                    on_click = row_delete
                ))
            ]
        ))
    # スクロール可能にする
    key_map_lv = ft.ListView(expand=1)
    key_map_lv.controls.append(key_map_dataTable)

    return ft.View(
        "/edit_key_mapping",
        [
            ft.AppBar(title=ft.Text("キーマップを編集してください")),
            determined_button,
            new_key_text_field,
            key_map_lv
        ]
    )
