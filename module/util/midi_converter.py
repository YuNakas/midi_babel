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
from gv import g

def midi_converter(converted_midi_filepath: str): 
    converter = g.MY_STATE.get_midi_map_obj()

    new_mid = mido.MidiFile()
    try:
        new_mid.tracks.append(g.MY_MIDI.get_setting_track())
    except:
        pass
    new_track = mido.MidiTrack()
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