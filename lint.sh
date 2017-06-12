#!/bin/bash -eu

pip install pylint
pylint app -f json && pylint pygoat -f json || echo "lint failed continuing with build"