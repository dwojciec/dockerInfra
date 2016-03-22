#!/bin/bash
#
# Run docker-compose in a container
# as root user execute 
curl -L https://github.com/docker/compose/releases/download/1.6.2/run.sh > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
