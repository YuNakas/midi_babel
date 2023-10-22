def create_midi_map(gen_map_obj, key_map_from_obj, key_map_to_obj):
    print(gen_map_obj, key_map_from_obj, key_map_to_obj)
    obj = {}
    for key in gen_map_obj:
        print(key)
        print(key_map_from_obj[key])
        for from_note in key_map_from_obj[key]['note']:
            obj[from_note] = key_map_to_obj[gen_map_obj[key]]['primary']
    print(obj)
    map_obj = {}
    return map_obj