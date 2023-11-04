import os, pathlib
from module.util import string_util

class ConfClass():
    __root_path: str
    __mapping_files: list[str]
    __key_mapping_files: list[str]
    __convert_midi_files: list[str]
    __converted_midi_files: list[str]
    __map_cache_files: list[str]

    def __init__(self) -> None:
        self.__root_path = str(pathlib.Path('__file__').resolve().parent)
        self.__mapping_files = string_util.get_filename(os.listdir(self.__root_path + '/mapping'), "yml")
        self.__key_mapping_files = string_util.get_filename(os.listdir(self.__root_path + '/key_mapping'), "yml")
        self.__convert_midi_files = string_util.get_filename(os.listdir(self.__root_path + '/assets/midi_ready'), "mid")
        self.__converted_midi_files = string_util.get_filename(os.listdir(self.__root_path + '/midi_converted'), "mid")
        self.__map_cache_files = string_util.get_filename(os.listdir(self.__root_path + "/key_mapping/_map_caches/"), "yml")
    
    def get_root_path(self):
        return self.__root_path
    
    def get_mapping_file(self):
        return self.__mapping_files
    
    def get_key_mapping_files(self):
        return self.__key_mapping_files
    
    def get_convert_midi_files(self):
        return self.__convert_midi_files

    def get_converted_midi_files(self):
        return self.__converted_midi_files
    
    def get_map_cache_files(self):
        return self.__map_cache_files
