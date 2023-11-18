"""
Copyright (C) 2023  Yu Nakas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os, pathlib
from module.util import string_util

class ConfClass():
    __root_path: str
    __key_mapping_files: list[str]
    __convert_midi_files: list[str]
    __converted_midi_files: list[str]
    __map_cache_files: list[str]

    def __init__(self) -> None:
        self.__root_path = str(pathlib.Path('__file__').resolve().parent)
        self.__key_mapping_files = string_util.get_filename(os.listdir(self.__root_path + '/assets/key_mapping'), "yml")
        self.__convert_midi_files = string_util.get_filename(os.listdir(self.__root_path + '/assets/midi_ready'), "mid")
        self.__converted_midi_files = string_util.get_filename(os.listdir(self.__root_path + '/assets/midi_converted'), "mid")
        self.__map_cache_files = string_util.get_filename(os.listdir(self.__root_path + "/assets/key_mapping/_map_caches/"), "yml")
    
    def get_root_path(self):
        return self.__root_path
    
    def get_key_mapping_files(self):
        return self.__key_mapping_files
    
    def get_convert_midi_files(self):
        return self.__convert_midi_files

    def get_converted_midi_files(self):
        return self.__converted_midi_files
    
    def get_map_cache_files(self):
        return self.__map_cache_files
