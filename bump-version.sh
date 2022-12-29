#!/usr/bin/env bash

set -ex

previous_version=$(semversioner current-version)
v_previous_version=v$previous_version

env

if [ "$ENV" == "dev" ]
then
  previous_version=$v_previous_version
  new_version="dev-latest"
else
    new_version=$(semversioner next-version)
fi

echo "Replace version '$previous_version' to '$new_version' in Dockerfile ..."
sed -i "s/$previous_version/$new_version/g" Dockerfile
cat Dockerfile


