import os
import json
from ..utils.config_util import loadConfig, saveConfig

def setConfig(key: str, value: str) -> None:
    if key is None or key.strip() == "":
        print("Error: Key must be provided for setting a configuration value.")
        return
    if value is None or value.strip() == "":
        print("Error: Value must be provided for setting a configuration value.")
        return

    config = loadConfig()

    if key not in config.keys():
        print(f"Error: '{key}' is not a valid configuration key.")
        return
    
    if value.lower() == "none" or value.lower() == "null":
        value = None
    
    config[key] = value
    saveConfig(config)

def getConfig(key: str) -> None:
    if key is None or key.strip() == "":
        print("Error: Key must be provided for getting a configuration value.")
        return
    
    config = loadConfig()

    if key not in config.keys():
        print(f"Error: '{key}' is not a valid configuration key.")
        return
    
    print(f"{key}: {config.get(key)}")

def unsetConfig(key: str) -> None:
    if key is None or key.strip() == "":
        print("Error: Key must be provided for unsetting a configuration value.")
        return

    config = loadConfig()

    if key in config:
        del config[key]
        saveConfig(config)
        print(f"Config '{key}' has been unset")
    else:
        print(f"Config '{key}' is not set")

def listConfig() -> None:
    config = loadConfig()
    print("Listing all config values:")
    for key, value in config.items():
        print(f"{key}: {value}")

def config(
    set: bool,
    get: bool,
    unset: bool,
    list: bool,
    key: str | None = None,
    value: str | None = None
) -> None:
    if set:
        setConfig(key, value)
    elif get:
        getConfig(key)
    elif unset:
        unsetConfig(key)
    elif list:
        listConfig()