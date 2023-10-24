import flet as ft

def create_data_table(strings, click_callback):
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("File Name"))
        ],
        rows=create_rows(strings, click_callback),
    )

    # スクロール可能にする
    lv = ft.ListView(expand=1)
    lv.controls.append(table)
    return lv

def create_rows(strings, click_callback): 
    rtnRows = []
    for string in strings: 
        rtnRows.append(ft.DataRow(
            cells=[ft.DataCell(ft.Text(string))],
            on_select_changed=lambda e: click_callback(e.control.cells[0].content.value)
        ))
    return rtnRows