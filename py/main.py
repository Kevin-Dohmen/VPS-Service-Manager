import argparse
from py import commands

def main():
    parser = argparse.ArgumentParser(description="VPS Service Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add subparser for 'add-service' command
    add_gh = subparsers.add_parser("add-gh", help="Add a new service from github")
    add_gh.add_argument("url", type=str, help="URL of the GitHub repository")
    add_gh.add_argument("--branch", type=str, default=None, help="Name of the branch to use")
    add_gh.add_argument("--use-docker-compose", action="store_true", help="Use docker-compose template")

    config = subparsers.add_parser("config", help="Configure VSM settings")
    group = config.add_mutually_exclusive_group(required=True)
    group.add_argument("--set", action="store_true", help="Set a configuration value")
    group.add_argument("--get", action="store_true", help="Get a configuration value")
    group.add_argument("--unset", action="store_true", help="Unset a configuration value")
    group.add_argument("--list", action="store_true", help="List all configuration values")
    config.add_argument("key", type=str, nargs="?", help="Configuration key")
    config.add_argument("value", type=str, nargs="?", help="Configuration value")


    args = parser.parse_args()

    if args.command == "add-gh":
        commands.add_gh(
            url=args.url,
            branch=args.branch,
            use_docker_compose=args.use_docker_compose
        )

    if args.command == "config":
        commands.config(
            set=args.set,
            get=args.get,
            unset=args.unset,
            list=args.list,
            key=args.key,
            value=args.value
        )

    args = parser.parse_args()

if __name__ == "__main__":
    main()
