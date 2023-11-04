import mido

class MidiClass():
    __selected_track: mido.MidiTrack
    __setting_track: mido.MidiTrack
    __track_type: str

    def __init__(self) -> None:
        self.__selected_track = mido.MidiTrack()
        self.__setting_track = mido.MidiTrack()
        self.__track_type = ""

    def set_track(self, selected_track, track_type) -> None:
        self.__selected_track = selected_track
        self.__track_type = track_type
    
    def set_setting_track(self, setting_track) -> None:
        self.__setting_track = setting_track
    
    def get_selected_track(self) -> mido.MidiTrack:
        return self.__selected_track
    
    def get_setting_track(self) -> mido.MidiTrack:
        return self.__setting_track
    
    def get_track_type(self) -> str:
        return self.__track_type