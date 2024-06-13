#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

REPO_ROOT=$(git rev-parse --show-toplevel)

ls -la
echo "*************" 
ls -la $REPO_ROOT
# Copy the .toml file to the parent directory
cp ./ruff.toml $REPO_ROOT/ruff-config.toml

echo "Copied ruff.toml to $REPO_ROOT"