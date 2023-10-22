import mido
from module.util import yaml_util

def midi_converter (midi_filepath: str, converted_midi_filepath: str, mapping_filepath: str) : 
    mapping = yaml_util.load_yaml(mapping_filepath)
    mid = mido.MidiFile(midi_filepath)
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

    new_mid.save(converted_midi_filepath)
