import flet as ft

def create_data_table(strings, click_callback):
    def create_rows(): 
        rtnRows = []
        for string in strings: 
            rtnRows.append(ft.DataRow(
                cells=[ft.DataCell(ft.Text(string))],
                on_select_changed=lambda e: click_callback(e.control.cells[0].content.value)
            ))
        return rtnRows
    
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("File Name"))
        ],
        rows=create_rows(),
    )

    # スクロール可能にする
    lv = ft.ListView(expand=1)
    lv.controls.append(table)
    return lv
