#!/bin/bash

set -e

# Directories to lint
CODE_DIRS="solutions tests"

echo "Running flake8: fail on critical errors..."
flake8 $CODE_DIRS --count --select=E9,F63,F7,F82 --show-source --statistics

echo "Running flake8: report warnings and style issues..."
flake8 $CODE_DIRS --count --exit-zero --max-complexity=15 --ignore=E501 --statistics

echo "Flake8 check complete."