#!/bin/bash -eu

# send coverage report to CodeClimate
./cc-test-reporter after-build --exit-code $TRAVIS_TEST_RESULT
