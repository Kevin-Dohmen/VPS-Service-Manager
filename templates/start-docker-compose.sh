#!/bin/bash

cd {{repo_root}} || exit 1

docker compose -p {{service_name}} up -d
