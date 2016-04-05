#!/bin/bash
#
# Run awscli as a container
#
# 
#


set -e

VERSION="latest"
IMAGE="relocaio/awscli:$VERSION"

#export AWS_ACCESS_KEY_ID=
#export AWS_SECRET_ACCESS_KEY=

# Setup options for connecting to docker host
if [ -z "$DOCKER_HOST" ]; then
    DOCKER_HOST="/var/run/docker.sock"
fi
if [ -S "$DOCKER_HOST" ]; then
    DOCKER_ADDR="-v $DOCKER_HOST:$DOCKER_HOST -e DOCKER_HOST"
else
    DOCKER_ADDR="-e DOCKER_HOST -e DOCKER_TLS_VERIFY -e DOCKER_CERT_PATH"
fi

# Only allocate tty if we detect one
if [ -t 1 ]; then
    DOCKER_RUN_OPTIONS="-t"
fi
if [ -t 0 ]; then
    DOCKER_RUN_OPTIONS="$DOCKER_RUN_OPTIONS -i"
fi


exec docker run --env AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --env AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY --rm $DOCKER_RUN_OPTIONS $DOCKER_ADDR -w "$(pwd)" $IMAGE "$@"

