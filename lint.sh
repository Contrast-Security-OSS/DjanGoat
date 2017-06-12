#!/usr/bin/env bash

pip install pylint
pylint app -f json
pylint pygoat -f json > pylint_pygoat.json