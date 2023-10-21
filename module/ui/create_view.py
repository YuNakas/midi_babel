import flet as ft
from module.util.midi_converter import midi_converter
from module.ui.pages import top, file_select, convert
from module import _init

def create_view(page, conf):
    convert_type: str = ""
    midi_file: str = ""
    mapping_file: str = ""
    key_mapping_from_file: str = ""
    key_mapping_to_file: str = ""

    def route_change(e):
        page.views.clear()
        page.views.append(
            top.top_view(to_midi)
        )
        if page.route == "/midi":
            page.views.append(
                file_select.file_select_view(create_dataTable, conf['convert_midi_files'], "変換したいmidiファイルを選んでください", "midi")
            )
        if page.route == "/map":
            page.views.append(
                file_select.file_select_view(create_dataTable, conf['mapping_files'], "変換に使うマッピングファイルを選んでください", "map")
            )
        if page.route == "/key_mapping_from":
            page.views.append(
                file_select.file_select_view(create_dataTable, conf['key_mapping_files'], "変換元のキーマップファイルを選んでください", "key_mapping_from")
            )
        if page.route == "/key_mapping_to":
            page.views.append(
                file_select.file_select_view(create_dataTable, conf['key_mapping_files'], "変換先のキーマップファイルを選んでください", "key_mapping_to")
            )
        if page.route == "/generate_converter":
            page.views.append(
                ft.View(
                    "/generate_converter",
                    [
                        ft.AppBar(title=ft.Text("変換表を生成します"), bgcolor=ft.colors.SURFACE_VARIANT),
                        create_dataTable(conf['mapping_files'], 'generate_converter')
                    ],
                )
            )
        if page.route == "/convert":
            page.views.append(
                convert.convert_view(return_top)
            )
            midi_converter(conf["root_path"], midi_file, mapping_file)
        page.update()
    
    def return_top(e):
        # ファイル名等を再取得
        nonlocal conf
        conf = _init.init_config()

        page.go("/")

    def to_midi(e):
        nonlocal convert_type
        convert_type =  e.control.data
        page.go("/midi")

    def create_dataTable(strings, page_path):
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("File Name"))
            ],
            rows=create_rows(strings, page_path),
        )

        # スクロール可能にする
        lv = ft.ListView(expand=1)
        lv.controls.append(table)
        return lv

    def create_rows(strings, page_path): 
        rtnRows = []
        for string in strings: 
            rtnRows.append(ft.DataRow(
                cells=[ft.DataCell(ft.Text(string))],
                on_select_changed=lambda e: click_rowData(e.control.cells[0].content.value, page_path)
            ))
        return rtnRows

    def click_rowData(rowData, page_code): 
        if page_code == "midi": 
            nonlocal midi_file
            midi_file = rowData
            if convert_type == "key_mapping": 
                page.go("/key_mapping_from")
            if convert_type == "midi_mapping": 
                page.go("/map")
        if page_code == "map":
            nonlocal mapping_file
            mapping_file = rowData
            page.go("/convert")
        if page_code == "key_mapping_from":
            nonlocal key_mapping_from_file
            key_mapping_from_file = rowData
            page.go("/key_mapping_to")
        if page_code == "key_mapping_to":
            nonlocal key_mapping_to_file
            key_mapping_to_file = rowData
            page.go("/generate_converter")
        if page_code == "generate_converter":
            page.go("/convert")

    page.on_route_change = route_change
    page.on_view_pop = return_top

    page.go(page.route)
