import os
from enum import Enum, auto
from typing import Optional
import subprocess
from py.utils.stringvalidators import formatValidFolderName, formatValidDockerName

def ensure_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def scaffold_service_directory(base_path: str, service_name: str) -> str:
    service_path = os.path.join(base_path, service_name)
    ensure_directory(service_path)
    return service_path


def clone_repository(repo_url: str, repo_location: str, branch: Optional[str] = None) -> None:
    ensure_directory(repo_location)
    print(f"Cloning repository {repo_url} into {repo_location}")

    cmd = ["git", "clone"]
    if branch:
        cmd.extend(["-b", branch])
    cmd.extend([repo_url, repo_location])

    subprocess.run(cmd, check=True)

    print(f"Repository cloned into {repo_location}")


def detect_project_type(service_path: str) -> 'ProjectType':
    if os.path.exists(os.path.join(service_path, "docker-compose.yml")):
        return ProjectType.DOCKERCOMPOSE
    return ProjectType.UNDETECTABLE


def copy_file(src: str, dest: str) -> None:
    cmd = ["cp", "-r", src, dest]
    subprocess.run(cmd, check=True)


def place_start_scripts(service_path: str, service_type: 'ProjectType', repo_path: str, service_name: str) -> None:
    template_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'templates')

    match service_type:
        case ProjectType.DOCKERCOMPOSE:
            templateFileDir = os.path.join(template_dir, 'start-docker-compose.sh')
        case _:
            templateFileDir = os.path.join(template_dir, 'start-base.sh')

    start_script_path = os.path.join(service_path, 'start.sh')
    
    with open(templateFileDir, 'r') as file:
        content = file.read()

    repo_root_relative = os.path.relpath(repo_path, start=os.path.dirname(start_script_path))

    content = content.replace("{{repo_root}}", repo_root_relative)
    content = content.replace("{{service_name}}", service_name)
    content = content.replace("{{docker_safe_service_name}}", formatValidDockerName(service_name))

    start_script_path = os.path.join(service_path, 'start.sh')
    with open(start_script_path, 'w') as file:
        file.write(content)

def scaffold_service_existing_project(
    services_base_path: str,
    service_path: str,
    project_path: str,
    service_name: str,
    project_type: Optional['ProjectType'] = None
) -> str:
    if project_type is None:
        project_type = detect_project_type(project_path)

    place_start_scripts(service_path, project_type, project_path, service_name)

    print(f"Service '{service_name}' scaffolded at '{service_path}' with project type: {project_type.name}")
    if project_type == ProjectType.UNDETECTABLE:
        print(f"Could not detect the project type automatically, modify start.sh script manually.")
    elif project_type == ProjectType.DOCKERCOMPOSE:
        print(f"Detected Docker Compose in repo. start.sh uses 'docker compose up' to start the service.")
    
    print(f"You might have to check the start.sh script and modify it to fit your needs.")

    return service_path


def scaffold_service_from_repository(
    services_base_path: str,
    service_name: str,
    repo_url: str,
    branch: str | None = None
) -> None:

    service_path = scaffold_service_directory(services_base_path, formatValidFolderName(service_name))
    repo_name = os.path.basename(repo_url).replace(".git", "")

    repo_location = os.path.join(service_path, formatValidFolderName(repo_name))

    clone_repository(repo_url, repo_location, branch)

    scaffold_service_existing_project(services_base_path, service_path, repo_location, service_name)


class ProjectType(Enum):
    UNDETECTABLE = 0
    DOCKERCOMPOSE = 1