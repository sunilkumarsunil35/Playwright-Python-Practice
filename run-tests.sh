#!/usr/bin/env sh
# Runs every test against the worked solutions in src/solutions.
# Add --mine to test your own code in src/exercises instead. Other options go straight to pytest:
#   sh run-tests.sh --mine -k locators        only the locator exercises
#   sh run-tests.sh --mine --headed --slowmo 500   watch the browser work
set -e
cd "$(dirname "$0")"
python3 -m pytest "$@"
