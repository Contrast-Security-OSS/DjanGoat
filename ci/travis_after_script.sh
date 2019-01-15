#!/bin/bash -eu

# send coverage report to Codacy
pip install codacy-coverage
python-codacy-coverage -r coverage.xml

# send coverage report to CodeClimate
./cc-test-reporter after-build --exit-code $TRAVIS_TEST_RESULT
