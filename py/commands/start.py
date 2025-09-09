import subprocess
import os
from py.utils.config_util import loadConfig

def start(
    name: str | list[str] = "all",
) -> None:
    config = loadConfig()
    services_location = config.get("services_location")

    if services_location is None or services_location.strip() == "":
        print("Error: 'services_location' is not set in the configuration. Please set it using the config command.")
        return
    
    if not os.path.exists(services_location):
        print(f"Error: The services location '{services_location}' does not exist.")
        return

    if isinstance(name, str):
        if name.lower() == "all":
            service_dirs = [d for d in os.listdir(services_location) if os.path.isdir(os.path.join(services_location, d))]
        else:
            service_dirs = [name]
    else:
        service_dirs = name

    for service_name in service_dirs:
        service_path = os.path.join(services_location, service_name)
        if not os.path.exists(service_path):
            print(f"Warning: Service '{service_name}' does not exist at '{service_path}'. Skipping.")
            continue

        start_script = os.path.join(service_path, "start.sh")
        if not os.path.exists(start_script):
            print(f"Warning: No start script found for service '{service_name}' at '{start_script}'. Skipping.")
            continue

        print(f"Starting service '{service_name}'...")
        subprocess.Popen(["bash", start_script], cwd=service_path)
        print(f"Service '{service_name}' started successfully.")
