#!/bin/bash

git push --tags
git push --tags --force --prune mirror "refs/remotes/origin/*:refs/heads/*"
