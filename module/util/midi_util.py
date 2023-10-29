import mido
from _gv import g

def read_midi_obj(filepath: str):
    rtn_midi_tracks_obj = {}
    midi_track_names: list[str] = []
    def get_track_name(track) -> str:
        rtn_str: str = "(トラック名がありません)"
        for msg in track:
            if type(msg) == mido.midifiles.meta.MetaMessage:
                if msg.type == "track_name":
                    rtn_str = msg.name
                    break
        return rtn_str
    mid = mido.MidiFile(filepath)
    for i, track in enumerate(mid.tracks):
        track_name = get_track_name(track)
        midi_track_names.append(track_name)
        rtn_midi_tracks_obj[track_name] = track
    g.MY_STATE.set_midi_track_names(rtn_midi_tracks_obj)
    return rtn_midi_tracks_obj