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

import re

def get_filename(strings: list[str], extension: str) -> list[str]:
    """特定の拡張子のファイル名を取り出す

    Args:
        strings (list[str]): ファイル名の配列
        extension (str): 取り出し対象の拡張子

    Returns:
        特定の拡張子のファイル名
    """

    rtnList = []
    for string in strings: 
        match = re.search(r"\." + extension + "$", string)
        if match:
            rtnList.append(string)
            
    return rtnList