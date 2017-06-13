#!/bin/bash -eu

apt-get update
apt-get install zip unzip
zip pygoat_artifact.zip *
