import mido
from _gv import g

def midi_converter(midi_filepath: str, converted_midi_filepath: str): 
    converter = g.MY_STATE.midi_map_obj

    new_mid = mido.MidiFile()
    try:
        new_mid.tracks.append(g.MY_MIDI.setting_track)
    except:
        pass
    new_track = mido.MidiTrack()
    for msg in g.MY_MIDI.selected_track:
        if type(msg) == mido.messages.messages.Message:
            if str(msg.note) in converter:
                new_message = msg
                new_message.note = int(converter[str(msg.note)])
                new_track.append(new_message)
            else:
                new_track.append(msg)
        else:
            new_track.append(msg)
    if g.MY_MIDI.track_type == "rhythm":
        new_track = drums_converter(new_track)
    new_mid.tracks.append(new_track)
    new_mid.save(converted_midi_filepath)

def drums_converter(track):
    """channelを 9 に設定して、リズム楽器として読み込まれるように変換する"""
    rtnTrack = mido.MidiTrack()
    for msg in track:
        if type(msg) == mido.messages.messages.Message:
            new_msg = msg
            new_msg.channel = 9
            rtnTrack.append(msg)
        else:
            rtnTrack.append(msg)
    return rtnTrack