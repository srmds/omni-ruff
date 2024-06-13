#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

REPO_ROOT=$(git rev-parse --show-toplevel)

# Copy the .toml file to the parent directory
cp ruff.toml $REPO_ROOT/ruff-config.toml

echo "Copied ruff.toml to $REPO_ROOT"