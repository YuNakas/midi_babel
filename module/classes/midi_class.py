"""
Copyright (C) 2023  Yu Nakas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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