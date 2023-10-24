class StateClass():
    convert_type: str
    midi_file: str
    mapping_file: str
    key_mapping_from_file: str
    key_mapping_to_file: str
    key_mapping_edit_file: str
    map_cache_fileName: object
    gen_map_obj: object
    from_or_to: str

    def set_convert_type(self, convert_type: str):
        self.convert_type = convert_type
    
    def set_midi_file(self, midi_file: str):
        self.midi_file = midi_file
    
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
    
    def set_from_or_to(self, from_or_to):
        self.from_or_to = from_or_to
    