import flet as ft
from module.midi_converter import midi_converter

def create_view(page, conf):
    convert_type: str = ""
    midi_file: str = ""
    mapping_file: str = ""
    key_mapping_from_file: str = ""
    key_mapping_to_file: str = ""

    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text('変換方式を選んでください'), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Container(ft.Column([
                        ft.Row([
                            ft.Container(
                                margin = 8,
                                width = 320,
                                content = ft.OutlinedButton(
                                    content=ft.Container(
                                        padding = 16,
                                        content = ft.Text("key mapping", size = 30)
                                    ),
                                    data="key_mapping", on_click=to_midi
                                )
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Container(
                                margin = 8,
                                width = 320,
                                content = ft.OutlinedButton(
                                    content=ft.Container(
                                        padding = 16,
                                        content = ft.Text("midi mapping", size = 30)
                                    ),
                                    data="midi_mapping", on_click=to_midi
                                )
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ]))
                ]
            )
        )
        if page.route == "/midi":
            page.views.append(
                ft.View(
                    "/midi",
                    [
                        ft.AppBar(title=ft.Text("変換したいmidiファイルを選んでください"), bgcolor=ft.colors.SURFACE_VARIANT),
                        create_dataTable(conf['convert_midi_files'], 'midi')
                    ],
                )
            )
        if page.route == "/map":
            page.views.append(
                ft.View(
                    "/map",
                    [
                        ft.AppBar(title=ft.Text("変換に使うマッピングファイルを選んでください"), bgcolor=ft.colors.SURFACE_VARIANT),
                        create_dataTable(conf['mapping_files'], 'map')
                    ],
                )
            )
        if page.route == "/key_mapping_from":
            page.views.append(
                ft.View(
                    "/key_mapping_from",
                    [
                        ft.AppBar(title=ft.Text("変換元のキーマップファイルを選んでください"), bgcolor=ft.colors.SURFACE_VARIANT),
                        create_dataTable(conf['mapping_files'], 'key_mapping_from')
                    ],
                )
            )
        if page.route == "/key_mapping_to":
            page.views.append(
                ft.View(
                    "/key_mapping_from",
                    [
                        ft.AppBar(title=ft.Text("変換先のキーマップファイルを選んでください"), bgcolor=ft.colors.SURFACE_VARIANT),
                        create_dataTable(conf['mapping_files'], 'key_mapping_to')
                    ],
                )
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
                ft.View(
                    "/convert",
                    [
                        ft.AppBar(title=ft.Text("変換が完了しました"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Topへ戻る",
                                    icon = "CHECK_CIRCLE_OUTLINE",
                                    on_click = return_top
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ]
                )
            )
            midi_converter(conf["root_path"], midi_file, mapping_file)
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    def return_top(e):
        page.go("/")
    
    def to_midi(e):
        nonlocal convert_type
        convert_type =  e.control.data
        page.go("/midi")

    def create_dataTable(strings, page_path):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("File Name"))
            ],
            rows=create_rows(strings, page_path)
        )

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
    page.on_view_pop = view_pop

    page.go(page.route)
