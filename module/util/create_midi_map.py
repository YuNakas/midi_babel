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

from gv import g

def create_midi_map(gen_map_obj, key_map_from_obj, key_map_to_obj):
    obj = {}
    for key in gen_map_obj:
        for from_note in key_map_from_obj[key]['note']:
            obj[from_note] = key_map_to_obj[gen_map_obj[key]]['primary']
    
    g.MY_STATE.set_midi_map_obj(obj)
