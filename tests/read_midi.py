import pathlib
import mido
import yaml

root = str(pathlib.Path('__file__').resolve().parent)
file_paths = ['test_drum_ezd']
# file_paths = ['test_drum_ezd', 'test_drum_flat', 'test_drum_gp7']

def save_yaml(yaml_obj, file_path):
    with open(file_path, "w") as file:
        yaml.dump(yaml_obj, file, default_flow_style=False)
for file_path in file_paths:
    mid = mido.MidiFile(root + '/tests/midi/' + file_path + '.mid')
    new_mid = mido.MidiFile()
    for i, track in enumerate(mid.tracks):
        new_track = mido.MidiTrack() 
        for msg in track:
            if type(msg) == mido.messages.messages.Message:
                new_msg = msg
                new_msg.channel = 9
                new_track.append(msg)
            else:
                new_track.append(msg)
        new_mid.tracks.append(new_track)
    new_mid.save(root + '/tests/midi/' + file_path + '_conv.mid')
    # save_yaml(mid, root + '/tests/yml/' + file_path + '.yml')
