import re
import flet as ft
from module.util import midi_converter
from module.ui.pages import top, midi, map, key_mapping_from, key_mapping_to, create_key_mapping, edit_key_mapping, generate_converter, convert_end
from module import _init
from module.util import create_midi_map, yaml_util

def create_view(page, conf):
    convert_type: str = ""
    midi_file: str = ""
    mapping_file: str = ""
    key_mapping_from_file: str = ""
    key_mapping_to_file: str = ""
    key_mapping_edit_file: str = ""
    map_cache_fileName = ""
    gen_map_obj = {}
    from_or_to = ""

    def route_change(e):
        page.views.clear()
        page.views.append(
            top.top_view(to_midi)
        )
        if page.route == "/midi":
            page.views.append(
                midi.midi_view(create_dataTable, conf['convert_midi_files'])
            )
        if page.route == "/map":
            page.views.append(
                map.map_view(create_dataTable, conf['mapping_files'])
            )
        if page.route == "/key_mapping_from":
            page.views.append(
                key_mapping_from.key_mapping_from_view(create_mappingDataTable, go_create_key_mapping_view ,conf['key_mapping_files'])
            )
        if page.route == "/key_mapping_to":
            page.views.append(
                key_mapping_to.key_mapping_to_view(create_mappingDataTable, go_create_key_mapping_view, conf['key_mapping_files'])
            )
        if page.route == "/create_key_mapping":
            page.views.append(
                create_key_mapping.create_key_mapping_view(go_edit_key_mapping_view, conf['key_mapping_files'])
            )
        if page.route == "/edit_key_mapping":
            page.views.append(
                edit_key_mapping.edit_key_mapping_view(go_next_page_from_edit_key, key_mapping_edit_file, conf)
            )
        if page.route == "/generate_converter":
            page.views.append(
                generate_converter.generate_converter_view(create_cache_fileName, set_gen_map_obj, load_map_cache, save_map_cache, create_converter, key_mapping_from_file, key_mapping_to_file, conf)
            )
        if page.route == "/convert_end":
            page.views.append(
                convert_end.convert_end_view(return_top)
            )
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
    
    def create_mappingDataTable(strings, page_path):
        table = ft.DataTable(
            columns=[
                ft.DataColumn(
                    label = ft.Container(
                        width=400,
                        content=ft.Text("File Name")
                    ),
                ),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text(""))
            ],
            rows=create_mappingRows(strings, page_path),
        )

        # スクロール可能にする
        lv = ft.ListView(expand=1)
        lv.controls.append(table)
        return lv

    def create_mappingRows(strings, page_path): 
        rtnRows = []
        for string in strings: 
            rtnRows.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(string)),
                    ft.DataCell(ft.OutlinedButton(
                        text="選択",
                        data=string,
                        on_click=lambda e: click_rowData(e.control.data, page_path)
                    )),
                    ft.DataCell(ft.OutlinedButton(
                        text="編集",
                        data=string,
                        on_click=lambda e: click_edit_button(e.control.data, page_path)
                    ))
                ]
            ))
        return rtnRows
    
    def click_edit_button(file_name, page_code):
        nonlocal from_or_to
        nonlocal key_mapping_from_file
        nonlocal key_mapping_to_file
        nonlocal key_mapping_edit_file
        if page_code == "key_mapping_from":
            from_or_to = "from"
            key_mapping_from_file = file_name
        if page_code == "key_mapping_to":
            from_or_to = "to"
            key_mapping_to_file = file_name
        key_mapping_edit_file = file_name
        page.go("/edit_key_mapping")
    
    def go_create_key_mapping_view(page_code): 
        nonlocal from_or_to
        if page_code == "key_mapping_from":
            from_or_to = "from"
        if page_code == "key_mapping_to":
            from_or_to = "to"
        page.go("/create_key_mapping")
    
    def go_edit_key_mapping_view(string):
        nonlocal from_or_to
        nonlocal key_mapping_from_file
        nonlocal key_mapping_to_file
        nonlocal key_mapping_edit_file
        if from_or_to == "from":
            key_mapping_from_file = string + ".yml"
        if from_or_to == "to":
            key_mapping_to_file = string + ".yml"
        key_mapping_edit_file = string + ".yml"
        page.go("/edit_key_mapping")
    
    def go_next_page_from_edit_key():
        nonlocal from_or_to
        if from_or_to == "from":
            page.go("/key_mapping_to")
        if from_or_to == "to":
            page.go("/generate_converter")

    def click_rowData(rowData, page_code):
        nonlocal midi_file
        nonlocal mapping_file
        nonlocal key_mapping_from_file
        nonlocal key_mapping_to_file
        if page_code == "midi": 
            midi_file = rowData
            if convert_type == "key_mapping": 
                page.go("/key_mapping_from")
            if convert_type == "midi_mapping": 
                page.go("/map")
        if page_code == "map":
            mapping_file = rowData
            page.go("/convert")
        if page_code == "key_mapping_from":
            key_mapping_from_file = rowData
            page.go("/key_mapping_to")
        if page_code == "key_mapping_to":
            key_mapping_to_file = rowData
            page.go("/generate_converter")
        if page_code == "generate_converter":
            page.go("/convert_end")

    def set_gen_map_obj(key, value):
        nonlocal gen_map_obj
        gen_map_obj[key] = value

    def create_converter(key_map_from_obj, key_map_to_obj):
        create_midi_map.create_midi_map(gen_map_obj, key_map_from_obj, key_map_to_obj)

    def load_map_cache():
        nonlocal gen_map_obj
        nonlocal map_cache_fileName
        if map_cache_fileName in conf["map_cache_files"]:
            gen_map_obj = yaml_util.load_yaml(conf["root_path"] + "/key_mapping/_map_caches/" + map_cache_fileName)
        else: 
            gen_map_obj = {}
        return gen_map_obj
    
    def save_map_cache():
        nonlocal gen_map_obj
        nonlocal map_cache_fileName
        yaml_util.save_yaml(gen_map_obj, conf["root_path"] + "/key_mapping/_map_caches/" + map_cache_fileName)
        nonlocal midi_file
        nonlocal key_mapping_from_file
        nonlocal key_mapping_to_file
        midi_filepath = conf["root_path"] + '/midi_ready/' + midi_file
        converted_midi_filepath = conf["root_path"] + '/midi_converted/' + re.sub(r"\..*$", "", midi_file) + "_converted_from_" + re.sub(r"\..*$", "", key_mapping_from_file) + "_to_" + re.sub(r"\..*$", "", key_mapping_to_file) + ".mid"
        mapping_filepath = conf["root_path"] + "/key_mapping/_map_caches/" + map_cache_fileName
        key_mapping_from_filepath = conf["root_path"] + "/key_mapping/" + key_mapping_from_file
        key_mapping_to_filepath = conf["root_path"] + "/key_mapping/" + key_mapping_to_file
        midi_converter.midi_converter(midi_filepath, converted_midi_filepath, mapping_filepath, key_mapping_from_filepath, key_mapping_to_filepath)
        page.go("/convert_end")


    def create_cache_fileName():
        nonlocal map_cache_fileName
        map_cache_fileName = (re.sub(r"\..*$", "", key_mapping_from_file) + "_" + re.sub(r"\..*$", "", key_mapping_to_file) + ".yml")
        
    page.on_route_change = route_change
    page.on_view_pop = return_top

    page.go(page.route)
