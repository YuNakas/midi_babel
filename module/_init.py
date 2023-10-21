import os, pathlib

def init_config():
  root_path: str = str(pathlib.Path('__file__').resolve().parent)
  mapping_files: str = os.listdir(root_path + '/mapping')
  key_mapping_files: str = os.listdir(root_path + '/key_mapping')
  convert_midi_files: str = os.listdir(root_path + '/midi_ready')

  return {
    "root_path": root_path,
    "mapping_files": mapping_files,
    "key_mapping_files": key_mapping_files,
    "convert_midi_files": convert_midi_files
  }
