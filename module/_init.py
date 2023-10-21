import os, pathlib
import re

def init_config():
    root_path: str = str(pathlib.Path('__file__').resolve().parent)
    mapping_files = get_filename(os.listdir(root_path + '/mapping'), "yml")
    key_mapping_files = get_filename(os.listdir(root_path + '/key_mapping'), "yml")
    convert_midi_files = get_filename(os.listdir(root_path + '/midi_ready'), "mid")

    return {
        "root_path": root_path,
        "mapping_files": mapping_files,
        "key_mapping_files": key_mapping_files,
        "convert_midi_files": convert_midi_files
    }

# 特定の拡張子のファイル名を取り出す
def get_filename(strings: list, extension: str):
    rtnList = []
    for string in strings: 
        match = re.search(r"\." + extension + "$", string)
        if match:
            rtnList.append(string)
            
    return rtnList
