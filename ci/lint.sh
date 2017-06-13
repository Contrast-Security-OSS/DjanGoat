#!/bin/bash -eu

pip install pylint
pylint app -f json > pylint_app.json && pylint pygoat -f json > pylint_pygoat.json || echo "lint failed continuing with build"