import mido

class MidiClass():
    selected_track: mido.MidiTrack
    setting_track: mido.MidiTrack
    track_type: str

    def set_track(self, selected_track, track_type):
        self.selected_track = selected_track
        self.track_type = track_type
    
    def set_setting_track(self, setting_track):
        self.setting_track = setting_track