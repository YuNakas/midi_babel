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

import yaml

def load_yaml(file_path): 
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
    
def save_yaml(yaml_obj, file_path):
    with open(file_path, "w") as file:
        yaml.dump(yaml_obj, file, default_flow_style=False)