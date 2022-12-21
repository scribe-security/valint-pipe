#!/bin/bash

git push --tags --force --prune mirror "refs/remotes/origin/*:refs/heads/*"
