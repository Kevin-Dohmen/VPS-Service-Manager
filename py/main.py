import argparse
from py import commands

def main():
    parser = argparse.ArgumentParser(description="VPS Service Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_gh = subparsers.add_parser("add-gh", help="Add a new service from github")
    add_gh.add_argument("name", type=str, help="Name of the service")
    add_gh.add_argument("url", type=str, help="URL of the GitHub repository")
    add_gh.add_argument("--branch", type=str, default=None, help="Name of the branch to use")

    config = subparsers.add_parser("config", help="Configure VSM settings")
    config_type = config.add_mutually_exclusive_group(required=True)
    config_type.add_argument("--set", action="store_true", help="Set a configuration value")
    config_type.add_argument("--get", action="store_true", help="Get a configuration value")
    config_type.add_argument("--unset", action="store_true", help="Unset a configuration value")
    config_type.add_argument("--list", action="store_true", help="List all configuration values")
    config.add_argument("key", type=str, nargs="?", help="Configuration key")
    config.add_argument("value", type=str, nargs="?", help="Configuration value")

    start = subparsers.add_parser("start", help="Start a service")
    start.add_argument("name", type=str, nargs="*", default="all", help="Name of the service to start, 'all' if not specified")

    args = parser.parse_args()

    if args.command == "add-gh":
        commands.add_gh(
            name=args.name,
            url=args.url,
            branch=args.branch,
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
    
    if args.command == "start":
        commands.start(
            name=args.name,
        )

    args = parser.parse_args()

if __name__ == "__main__":
    main()
