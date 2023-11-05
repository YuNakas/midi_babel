import flet as ft

def create_data_table(strings, click_callback):
    def create_rows(): 
        rtnRows = []
        for string in strings: 
            rtnRows.append(ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Container(
                            width = 800,
                            padding = 0,
                            margin = 0,
                            data = string,
                            alignment = ft.alignment.Alignment(-0.95, 0),
                            content = ft.Text(
                                value = string
                            ),
                            on_click = lambda e: click_callback(e.control.data)
                        )
                    )
                ],
            ))
        return rtnRows
    
    table = ft.DataTable(
        heading_row_height=40,
        width = 800,
        column_spacing=0,
        columns=[
            ft.DataColumn(
                label = ft.Container(
                    width = 800,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(-0.95, 0),
                    content = ft.Text(
                        value = "ファイル名",
                        size = 18,
                        height=40
                    )
                )
            )
        ],
        rows=create_rows(),
    )

    # スクロール可能にする
    lv = ft.ListView(expand=1)
    lv.controls.append(table)
    return lv

def create_mappingDataTable(strings, click_select_button, click_edit_button):
    def create_mappingRows(): 
        rtnRows = []
        for string in strings: 
            rtnRows.append(ft.DataRow(
                cells=[
                    ft.DataCell(
                        content = ft.Container(
                            alignment = ft.alignment.Alignment(-0.8, 0),
                            content = ft.Text(string)
                        )
                    ),
                    ft.DataCell(
                        content = ft.Container(
                            alignment = ft.alignment.Alignment(0, 0),
                            content = ft.OutlinedButton(
                                text="選択",
                                data=string,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8)
                                ),
                                on_click=lambda e: click_select_button(e.control.data)
                            )
                        )
                    ),
                    ft.DataCell(
                        content = ft.Container(
                            alignment = ft.alignment.Alignment(0, 0),
                            content = ft.OutlinedButton(
                                text="編集",
                                data=string,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8)
                                ),
                                on_click=lambda e: click_edit_button(e.control.data)
                            )
                        )
                    )
                ]
            ))
        return rtnRows
    
    table = ft.DataTable(
        heading_row_height=40,
        width = 800,
        column_spacing = 0,
        horizontal_margin = 0,
        columns=[
            ft.DataColumn(
                label = ft.Container(
                    width = 480,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(-0.8, 0),
                    content = ft.Text(
                        value = "ファイル名",
                        size = 18,
                        height = 40
                    )
                ),
            ),
            ft.DataColumn(
                label = ft.Container(
                    width = 140,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(0, 0),
                    content = ft.Text("")
                )
            ),
            ft.DataColumn(
                label = ft.Container(
                    width = 140,
                    padding = 0,
                    margin = 0,
                    alignment = ft.alignment.Alignment(0, 0),
                    content = ft.Text("")
                )
            )
        ],
        rows=create_mappingRows()
    )

    # スクロール可能にする
    lv = ft.ListView(expand = 1, spacing = 0, padding = 0, width = 840)
    lv.controls.append(table)
    return lv
