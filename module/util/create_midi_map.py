from _gv import g

def create_midi_map(gen_map_obj, key_map_from_obj, key_map_to_obj):
    obj = {}
    for key in gen_map_obj:
        for from_note in key_map_from_obj[key]['note']:
            obj[from_note] = key_map_to_obj[gen_map_obj[key]]['primary']
    
    g.MY_STATE.set_midi_map_obj(obj)
