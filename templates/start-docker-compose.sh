#!/bin/bash

cd {{repo_root}} || exit 1

docker compose -p {{docker_safe_service_name}} up > ../latest.log 2>&1 &
