#!/bin/bash -eu

docker cp $(pwd) ruby-builder:/tmp/workspace
apt-get update
apt-get install zip unzip
zip ../pygoat_artifact.zip .*