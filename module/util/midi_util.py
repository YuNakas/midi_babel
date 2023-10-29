import mido
from _gv import g
from module.util import yaml_util

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
    
    def check_setting_track(track) -> bool:
        for msg in track:
            if type(msg) == mido.midifiles.meta.MetaMessage:
                if msg.type == "set_tempo":
                    return True
        return False

    mid = mido.MidiFile(filepath)
    for i, track in enumerate(mid.tracks):
        track_name = get_track_name(track)
        if i == 0 and check_setting_track(track):
            # 1トラック目にset_tempo情報がある場合、
            # テンポ等の情報と判断してオブジェクトに追加する
            rtn_midi_tracks_obj["setting_track"] = track
        else:
            midi_track_names.append(track_name)
            rtn_midi_tracks_obj[track_name] = track
    g.MY_STATE.set_midi_track_names(midi_track_names)
    return rtn_midi_tracks_obj