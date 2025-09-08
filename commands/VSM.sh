
OLD_PWD="$PWD"

VSM_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$VSM_ROOT" || exit 1

python3 -m py.main "$@"
