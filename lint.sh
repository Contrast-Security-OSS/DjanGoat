#!/bin/bash -eu

pip install pylint
pylint app -f json
pylint pygoat -f json > pylint_pygoat.json