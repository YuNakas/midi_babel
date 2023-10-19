import os, pathlib

def init_config():
  root_path: str = str(pathlib.Path('__file__').resolve().parent)
  mapping_files: str = os.listdir(root_path + '/mapping')
  convert_midi_files: str = os.listdir(root_path + '/convert_from')

  return {
    "root_path": root_path,
    "mapping_files": mapping_files,
    "convert_midi_files": convert_midi_files
  }
