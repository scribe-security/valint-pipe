#!/usr/bin/env bats

setup() {
  DOCKER_IMAGE=${DOCKER_IMAGE:="scribe-security/valint-pipe"}

  echo "Building image..."
  docker build -t ${DOCKER_IMAGE}:test .
}

@test "Test installation" {
    run docker run \
        -e COMMAND_NAME=bom \
        -e TARGET=dir:. \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        ${DOCKER_IMAGE}:test

    echo "Status: $status"
    echo "Output: $output"

    [ "$status" -eq 0 ]
}

