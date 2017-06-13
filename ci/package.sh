#!/bin/bash -eu

docker cp $(pwd) pygoat:/tmp/workspace
apt-get update
apt-get install zip unzip
zip ../pygoat_artifact.zip .*