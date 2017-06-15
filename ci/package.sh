#!/bin/bash -eu

apt-get update
apt-get install zip unzip
zip -r pygoat_artifact.zip *
