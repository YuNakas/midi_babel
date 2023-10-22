import flet as ft
from module.util import yaml_util

def load_key_mapping(file_path, conf):
    return yaml_util.load_yaml(conf["root_path"] + "/key_mapping/" + file_path)

def generate_converter_view(create_cache_fileName, set_gen_map_obj, load_map_cache, save_map_cache, create_converter, key_mapping_from_file, key_mapping_to_file, conf):
    create_cache_fileName()
    key_map_from_obj = load_key_mapping(key_mapping_from_file, conf)
    key_map_to_obj = load_key_mapping(key_mapping_to_file, conf)
    gen_map_obj = load_map_cache()

    def create_convertTable():
        table = ft.DataTable(
            width = 800,
            data_row_min_height = 80,
            data_row_max_height = 80,
            columns=[
                ft.DataColumn(ft.Text("Convert From")),
                ft.DataColumn(ft.Text("Convert To"))
            ],
            rows=create_row()
        )
        
        # スクロール可能にする
        lv = ft.ListView(expand=1)
        lv.controls.append(table)
        return lv

    def create_row():
        rtnRows = []
        for key in key_map_from_obj.keys():
            cache_text = ""
            if key in gen_map_obj:
                cache_text = gen_map_obj[key]
            rtnRows.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(key)),
                    ft.DataCell(ft.Dropdown(
                        key = key,
                        hint_text = cache_text,
                        options = create_options(key_map_to_obj.keys()),
                        on_change = lambda e: change_dropdown(e)
                    )
                )]
            ))
        
        return rtnRows
        
    def create_options(strings):
        rtnOptions = []
        for string in strings:
            rtnOptions.append(ft.dropdown.Option(string))
        
        return rtnOptions

    def change_dropdown(e):
        set_gen_map_obj(e.control.key, e.data)

    def next(e):
        create_converter(key_map_from_obj, key_map_to_obj)
        save_map_cache()

    return ft.View(
        "/generate_converter",
        [
            ft.AppBar(title=ft.Text("変換表を生成します")),
            ft.Container(
                padding = 8,
                content = ft.Container(
                    padding = 8,
                    content = ft.OutlinedButton(on_click = next, content=ft.Text("決定", size = 16))
                )
            ),
            create_convertTable(),
        ]
    )
