import mido
from _gv import g

def midi_converter(midi_filepath: str, converted_midi_filepath: str): 
    converter = g.MY_STATE.midi_map_obj

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

def drums_converter():
    """channelを 9 に設定して、リズム楽器として読み込まれるように変換する"""
    pass