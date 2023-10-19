import flet as ft
from module.midi_converter import midi_converter

def create_view(page, conf):
    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text('変換方式を選んでください'), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("key mapping", on_click=to_midi),
                    ft.ElevatedButton("midi mapping", on_click=to_midi)
                ],
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
        global convert_type
        convert_type =  e.control.text
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
            global midi_file
            midi_file = rowData
            page.go("/map")
        if page_code == "map":
            global mapping_file
            mapping_file = rowData
            page.go("/convert")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)
