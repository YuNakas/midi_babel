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

from module.classes import conf_class, midi_class, state_class

MY_CONF = conf_class.ConfClass()
MY_MIDI = midi_class.MidiClass()
MY_STATE = state_class.StateClass()

def reset_class():
    MY_CONF.__init__()
    MY_MIDI.__init__()
    MY_STATE.__init__()