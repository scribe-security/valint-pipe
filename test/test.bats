#!/usr/bin/env bats

setup() {
  DOCKER_IMAGE=${DOCKER_IMAGE:="test/maestro-cloud-upload"}

  echo "Building image..."
  docker build -t ${DOCKER_IMAGE}:test .
}

@test "Test installation" {
    run docker run \
        -e MDEV_TEST_INSTALL="true" \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        ${DOCKER_IMAGE}:test --version

    echo "Status: $status"
    echo "Output: $output"

    [ "$status" -eq 0 ]
}

