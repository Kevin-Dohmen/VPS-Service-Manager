import os
import json

config_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'config.json')

default_config = {
    "services_location": None
}

def loadConfig() -> dict:
    json_config: dict = {}

    if os.path.exists(config_file_path):
        try:
            with open(config_file_path, 'r') as f:
                json_config = json.load(f)
        except json.JSONDecodeError:
            print("Error decoding JSON config file. Using default config.")
            json_config = {}

    for key, value in default_config.items():
        if key not in json_config:
            json_config[key] = value
    
    return json_config

def saveConfig(config: dict) -> None:
    with open(config_file_path, 'w') as f:
        for key, value in default_config.items():
            if key not in config:
                config[key] = value

        for key in list(config.keys()):
            if key not in default_config:
                del config[key]

        json.dump(config, f)
        f.flush()
    print("Config saved")