import os
from py.utils.config_util import loadConfig, saveConfig
from py.utils.scaffolder import scaffold_service_existing_project, scaffold_service_from_repository, scaffold_service_directory, clone_repository, ProjectType

def add_gh(
    name: str,
    url: str,
    branch: str | None = None,
) -> None:
    
    if name is None or name.strip() == "":
        print("Error: Name must be provided for adding a service from GitHub.")
        return

    if url is None or url.strip() == "":
        print("Error: URL must be provided for adding a service from GitHub.")
        return
    
    config = loadConfig()
    services_location = config.get("services_location")

    if services_location is None or services_location.strip() == "":
        print("Error: 'services_location' is not set in the configuration. Please set it using the config command.")
        return
    
    if not os.path.exists(services_location):
        print(f"Error: The services location '{services_location}' does not exist.")
        return

    scaffold_service_from_repository(services_location, name, url, branch)

    print(f"Service '{name}' added successfully from GitHub repository.")