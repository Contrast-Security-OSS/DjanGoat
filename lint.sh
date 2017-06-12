#!/bin/bash -eu

pip install pylint
pylint app -f json || exit 0