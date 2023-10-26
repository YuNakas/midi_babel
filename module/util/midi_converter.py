import mido
from module.util import yaml_util

def midi_converter (midi_filepath: str, converted_midi_filepath: str, mapping_filepath: str, key_mapping_from_filepath, key_mapping_to_filepath) : 
    mapping = yaml_util.load_yaml(mapping_filepath)
    key_mapping_from = yaml_util.load_yaml(key_mapping_from_filepath)
    key_mapping_to = yaml_util.load_yaml(key_mapping_to_filepath)
    converter = create_converter(mapping, key_mapping_from, key_mapping_to)

    mid = mido.MidiFile(midi_filepath)
    new_mid = mido.MidiFile()
    for i, track in enumerate(mid.tracks):
        new_track = mido.MidiTrack() 
        new_mid.tracks.append(new_track)
        for msg in track:
            if type(msg) == mido.messages.messages.Message:
                if str(msg.note) in converter:
                    new_message = msg
                    new_message.note = int(converter[str(msg.note)])
                    new_track.append(new_message)
                else:
                    new_track.append(msg)
            else:
                new_track.append(msg)

    new_mid.save(converted_midi_filepath)

def create_converter(mapping, key_mapping_from, key_mapping_to):
    rtnObj = {}
    for key in mapping.keys():
        for note_from in key_mapping_from[key]["note"]:
            rtnObj[note_from] = key_mapping_to[mapping[key]]["primary"]
    print(rtnObj)
    return rtnObj

def drums_converter():
    """channelを 9 に設定して、リズム楽器として読み込まれるように変換する"""
    pass