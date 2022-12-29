#!/usr/bin/env bash

# Bump versions using semversioner

set -ex

previous_version=$(semversioner current-version)
v_previous_version=v$previous_version
# semversioner release

env

if [ "$ENV" == "dev" ]
then
  previous_version=$v_previous_version
  new_version="dev-latest"
else
    new_version=$(semversioner next-version)
fi

# echo "Generating CHANGELOG.md file..."
# semversioner changelog > CHANGELOG.md

# # Use new version in the README.md examples
# echo "Replace version '$previous_version' to '$new_version' in README.md ..."
# sed -i "s/$previous_version/$new_version/g" README.md

# # Use new version in the pipe.yml metadata file
# echo "Replace version '$previous_version' to '$new_version' in pipe.yml ..."
# sed -i "s/$previous_version/$new_version/g" setup.py

echo "Replace version '$previous_version' to '$new_version' in Dockerfile ..."
sed -i "s/$previous_version/$new_version/g" Dockerfile
cat Dockerfile


