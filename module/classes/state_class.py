class StateClass():
    convert_type: str # 変換タイプ: key mapping
    midi_file: str # 選択したmidiファイル名
    midi_obj: object # midiオブジェクト
    midi_track_obj: object # 変換対象のmidiオブジェクトのトラック名
    midi_track_names: list[str]
    mapping_file: str
    key_mapping_from_file: str
    key_mapping_to_file: str
    key_mapping_edit_file: str
    map_cache_fileName: object
    gen_map_obj: object
    midi_map_obj: object
    from_or_to: str

    def set_convert_type(self, convert_type: str):
        self.convert_type = convert_type
    
    def set_midi_file(self, midi_file: str):
        self.midi_file = midi_file
    
    def set_midi_obj(self, midi_obj: object):
        self.midi_obj = midi_obj
    
    def set_midi_track_obj(self, midi_track_obj: object):
        self.midi_track_obj = midi_track_obj
    
    def set_midi_track_names(self, midi_track_names: list[str]):
        self.midi_track_names = midi_track_names
    
    def set_mapping_file(self, mapping_file):
        self.mapping_file = mapping_file
    
    def set_key_mapping_from_file(self, key_mapping_from_file):
        self.key_mapping_from_file = key_mapping_from_file
    
    def set_key_mapping_to_file(self, key_mapping_to_file):
        self.key_mapping_to_file = key_mapping_to_file
    
    def set_key_mapping_edit_file(self, key_mapping_edit_file):
        self.key_mapping_edit_file = key_mapping_edit_file
    
    def set_map_cache_fileName(self, map_cache_fileName):
        self.map_cache_fileName = map_cache_fileName
    
    def set_gen_map_obj(self, gen_map_obj):
        self.gen_map_obj = gen_map_obj

    def set_midi_map_obj(self, midi_map_obj):
        self.midi_map_obj = midi_map_obj
    
    def set_from_or_to(self, from_or_to):
        self.from_or_to = from_or_to
    