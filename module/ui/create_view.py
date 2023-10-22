import re
import flet as ft
from module.util.midi_converter import midi_converter
from module.ui.pages import top, midi, map, key_mapping_from, key_mapping_to, file_select, generate_converter, convert
from module import _init
from module.util import create_midi_map, yaml_util

def create_view(page, conf):
    convert_type: str = ""
    midi_file: str = ""
    mapping_file: str = ""
    key_mapping_from_file: str = ""
    key_mapping_to_file: str = ""
    map_cache_fileName = ""
    gen_map_obj = {}

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
                key_mapping_from.key_mapping_from_view(create_dataTable, conf['key_mapping_files'])
            )
        if page.route == "/key_mapping_to":
            page.views.append(
                key_mapping_to.key_mapping_to_view(create_dataTable, conf['key_mapping_files'])
            )
        if page.route == "/create_key_mapping":
            page.views.append()
        if page.route == "/edit_key_mapping":
            page.views.append()
        if page.route == "/generate_converter":
            page.views.append(
                generate_converter.generate_converter_view(create_cache_fileName, set_gen_map_obj, load_map_cache, save_map_cache, create_converter, key_mapping_from_file, key_mapping_to_file, conf)
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

    def set_gen_map_obj(key, value):
        nonlocal gen_map_obj
        gen_map_obj[key] = value

    def create_converter(key_map_from_obj, key_map_to_obj):
        create_midi_map.create_midi_map(gen_map_obj, key_map_from_obj, key_map_to_obj)

    def load_map_cache():
        nonlocal gen_map_obj
        if map_cache_fileName in conf["map_cache_files"]:
            gen_map_obj = yaml_util.load_yaml(conf["root_path"] + "/key_mapping/_map_caches/" + map_cache_fileName)
        return gen_map_obj
    
    def save_map_cache():
        nonlocal gen_map_obj
        print(gen_map_obj)
        yaml_util.save_yaml(gen_map_obj, conf["root_path"] + "/key_mapping/_map_caches/" + map_cache_fileName)


    def create_cache_fileName():
        nonlocal map_cache_fileName
        map_cache_fileName = (re.sub(r"\..*$", "", key_mapping_from_file) + "_" + re.sub(r"\..*$", "", key_mapping_to_file) + ".yml")
        
    page.on_route_change = route_change
    page.on_view_pop = return_top

    page.go(page.route)
