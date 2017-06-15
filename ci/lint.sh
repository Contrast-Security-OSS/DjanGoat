#!/bin/bash -eu

pip install pylint
pip install pylint-django
pylint app pygoat -f json > pylint_app.json || echo "lint failed continuing with build"