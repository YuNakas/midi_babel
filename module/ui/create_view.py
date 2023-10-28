import re
import flet as ft
from _gv import g
from module import _init
from module.util import midi_converter
from module.util import create_midi_map, yaml_util
from module.ui.pages import top, midi, map, key_mapping_from, key_mapping_to, create_key_mapping, edit_key_mapping, generate_converter, convert_end

def create_view(page):
    midi_file: str = ""
    key_mapping_from_file: str = ""
    key_mapping_to_file: str = ""
    map_cache_fileName = ""
    gen_map_obj = {}

    def route_change(e):
        page.views.clear()
        page.views.append(
            top.top_view(page.go)
        )
        if page.route == "/midi":
            page.views.append(
                midi.midi_view(page.go)
            )
        if page.route == "/map":
            page.views.append(
                map.map_view(page.go)
            )
        if page.route == "/key_mapping_from":
            page.views.append(
                key_mapping_from.key_mapping_from_view(page.go)
            )
        if page.route == "/key_mapping_to":
            page.views.append(
                key_mapping_to.key_mapping_to_view(page.go)
            )
        if page.route == "/create_key_mapping":
            page.views.append(
                create_key_mapping.create_key_mapping_view(page.go)
            )
        if page.route == "/edit_key_mapping":
            page.views.append(
                edit_key_mapping.edit_key_mapping_view(page.go)
            )
        if page.route == "/generate_converter":
            page.views.append(
                generate_converter.generate_converter_view(page.go)
            )
        if page.route == "/convert_end":
            page.views.append(
                convert_end.convert_end_view(return_top)
            )
        page.update()
    
    def return_top(e):
        # コンフィグ情報を再取得
        _init.init_config()

        # 選択した情報などを初期化
        _init.init_state()

        page.go("/")

    def set_gen_map_obj(key, value):
        nonlocal gen_map_obj
        gen_map_obj[key] = value

    def create_converter(key_map_from_obj, key_map_to_obj):
        create_midi_map.create_midi_map(gen_map_obj, key_map_from_obj, key_map_to_obj)
    
    def save_map_cache():
        nonlocal gen_map_obj
        nonlocal map_cache_fileName
        yaml_util.save_yaml(gen_map_obj, g.MY_CONF.root_path + "/key_mapping/_map_caches/" + map_cache_fileName)
        nonlocal midi_file
        nonlocal key_mapping_from_file
        nonlocal key_mapping_to_file
        midi_filepath = g.MY_CONF.root_path + '/midi_ready/' + midi_file
        converted_midi_filepath = g.MY_CONF.root_path + '/midi_converted/' + re.sub(r"\..*$", "", midi_file) + "_converted_from_" + re.sub(r"\..*$", "", key_mapping_from_file) + "_to_" + re.sub(r"\..*$", "", key_mapping_to_file) + ".mid"
        mapping_filepath = g.MY_CONF.root_path + "/key_mapping/_map_caches/" + map_cache_fileName
        key_mapping_from_filepath = g.MY_CONF.root_path + "/key_mapping/" + key_mapping_from_file
        key_mapping_to_filepath = g.MY_CONF.root_path + "/key_mapping/" + key_mapping_to_file
        midi_converter.midi_converter(midi_filepath, converted_midi_filepath, mapping_filepath, key_mapping_from_filepath, key_mapping_to_filepath)
        page.go("/convert_end")
        
    page.on_route_change = route_change
    page.on_view_pop = return_top

    page.go(page.route)
