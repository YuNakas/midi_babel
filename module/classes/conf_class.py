import os, pathlib
from module.util import string_util


class ConfClass():
    root_path: str
    mapping_files: list[str]
    key_mapping_files: list[str]
    convert_midi_files: list[str]
    map_cache_files: list[str]

    def __init__(self) -> None:
        self.root_path = str(pathlib.Path('__file__').resolve().parent)
        self.mapping_files = string_util.get_filename(os.listdir(self.root_path + '/mapping'), "yml")
        self.key_mapping_files = string_util.get_filename(os.listdir(self.root_path + '/key_mapping'), "yml")
        self.convert_midi_files = string_util.get_filename(os.listdir(self.root_path + '/midi_ready'), "mid")
        self.map_cache_files = string_util.get_filename(os.listdir(self.root_path + "/key_mapping/_map_caches/"), "yml")
