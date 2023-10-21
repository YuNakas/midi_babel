import mido, yaml

def midi_converter (root_path: str, midi_file_name: str, mapping_filename: str) : 
    mapping = read_yaml(mapping_filename)
    mid = mido.MidiFile(root_path + '/midi_ready/' + midi_file_name)
    new_mid = mido.MidiFile()
    for i, track in enumerate(mid.tracks):
        new_track = mido.MidiTrack() 
        new_mid.tracks.append(new_track)
        for msg in track:
            if type(msg) == mido.messages.messages.Message:
                if str(msg.note) in mapping:
                    new_message = msg
                    new_message.note = int(mapping[str(msg.note)])
                    new_track.append(new_message)
                else:
                    new_track.append(msg)
            else:
                new_track.append(msg)

    new_mid.save(root_path + '/midi_converted/converted_' + midi_file_name)

def read_yaml (yaml_filename: str) : 
    return yaml.safe_load(yaml_filename)