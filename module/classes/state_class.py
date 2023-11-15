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

class StateClass():
    __midi_file: str # 選択したmidiファイル名
    __midi_obj: object # midiオブジェクト
    __midi_track_names: list[str]
    __mapping_file: str
    __key_mapping_from_file: str
    __key_mapping_to_file: str
    __key_mapping_edit_file: str
    __map_cache_fileName: object
    __gen_map_obj: object
    __midi_map_obj: object
    __from_or_to: str
    
    def set_midi_file(self, midi_file: str):
        self.__midi_file = midi_file
    
    def set_midi_obj(self, midi_obj: object):
        self.__midi_obj = midi_obj
    
    def set_midi_track_names(self, midi_track_names: list[str]):
        self.__midi_track_names = midi_track_names
    
    def set_mapping_file(self, mapping_file):
        self.__mapping_file = mapping_file
    
    def set_key_mapping_from_file(self, key_mapping_from_file):
        self.__key_mapping_from_file = key_mapping_from_file
    
    def set_key_mapping_to_file(self, key_mapping_to_file):
        self.__key_mapping_to_file = key_mapping_to_file
    
    def set_key_mapping_edit_file(self, key_mapping_edit_file):
        self.__key_mapping_edit_file = key_mapping_edit_file
    
    def set_map_cache_fileName(self, map_cache_fileName):
        self.__map_cache_fileName = map_cache_fileName
    
    def set_gen_map_obj(self, gen_map_obj):
        self.__gen_map_obj = gen_map_obj

    def set_midi_map_obj(self, midi_map_obj):
        self.__midi_map_obj = midi_map_obj
    
    def set_from_or_to(self, from_or_to):
        self.__from_or_to = from_or_to
    
    def get_midi_file(self):
        return self.__midi_file
    
    def get_midi_obj(self):
        return self.__midi_obj
    
    def get_midi_track_names(self):
        return self.__midi_track_names
    
    def get_mapping_file(self):
        return self.__mapping_file
    
    def get_key_mapping_from_file(self):
        return self.__key_mapping_from_file
    
    def get_key_mapping_to_file(self):
        return self.__key_mapping_to_file
    
    def get_key_mapping_edit_file(self):
        return self.__key_mapping_edit_file
    
    def get_map_cache_fileName(self):
        return self.__map_cache_fileName
    
    def get_gen_map_obj(self):
        return self.__gen_map_obj
    
    def get_midi_map_obj(self):
        return self.__midi_map_obj
    
    def get_from_or_to(self):
        return self.__from_or_to