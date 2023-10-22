import yaml

def load_yaml(file_path): 
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
    
def save_yaml(yaml_obj, file_path):
    with open(file_path, "w") as file:
        yaml.dump(yaml_obj, file, default_flow_style=False)