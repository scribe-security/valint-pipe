#!/usr/bin/env bash

set -ex

previous_version=$(semversioner current-version)
v_previous_version=v$previous_version

if [ "$ENV" == "dev" ]; then
  previous_version=$v_previous_version
  new_version="dev-latest"
else
  new_version=$(semversioner next-version)
fi

# Replace any version in the FROM line with the new version
echo "Replace version in Dockerfile with '$new_version'..."
sed -i "s|FROM scribesecuriy.jfrog.io/scribe-docker-public-local/valint:v[^\ ]*|FROM scribesecuriy.jfrog.io/scribe-docker-public-local/valint:$new_version|g" Dockerfile

cat Dockerfile
