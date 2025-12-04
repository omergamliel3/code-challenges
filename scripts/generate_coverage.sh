#!/bin/bash

set -e
coverage run -m unittest discover
coverage report -m
coverage html
open htmlcov/index.html