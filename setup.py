import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    # 取り込みたいパッケージをこの中に記載します。
    "packages": [
        "flet", "mido", "yaml"
    ],
    "include_files": [
        "assets/"
    ]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Midi Babel",
    version="1.0.0",
    description="Midi Converter",
    options={
        "build_exe": build_exe_options,
    },
    executables=[
        Executable(
            # 実行ファイル名を記載します。
            script="midi_babel.py",
            base=base,
        ),
    ],
)