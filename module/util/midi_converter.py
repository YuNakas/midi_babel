import mido
from gv import g

def midi_converter(converted_midi_filepath: str): 

    new_mid = mido.MidiFile()
    try:
        new_mid.tracks.append(g.MY_MIDI.get_setting_track())
    except:
        pass
    new_track = mido.MidiTrack()
    if g.MY_STATE.get_convert_mode() == "":
        converter = g.MY_STATE.get_midi_map_obj()
        for msg in g.MY_MIDI.get_selected_track():
            if type(msg) == mido.messages.messages.Message:
                if str(msg.note) in converter:
                    new_message = msg
                    new_message.note = int(converter[str(msg.note)])
                    new_track.append(new_message)
                else:
                    new_track.append(msg)
            else:
                new_track.append(msg)
    if g.MY_STATE.get_convert_mode() == "tautology":
        for msg in g.MY_MIDI.get_selected_track():
            if type(msg) == mido.messages.messages.Message:
                new_track.append(msg)
    if g.MY_STATE.get_convert_mode() == "octave_up":
        for msg in g.MY_MIDI.get_selected_track():
            if type(msg) == mido.messages.messages.Message:
                new_message = msg
                new_message.note = msg.note + 12
                new_track.append(msg)
    if g.MY_STATE.get_convert_mode() == "octave_up":
        for msg in g.MY_MIDI.get_selected_track():
            if type(msg) == mido.messages.messages.Message:
                new_message = msg
                new_message.note = msg.note - 12
                new_track.append(msg)
    if g.MY_MIDI.get_track_type() == "rhythm":
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