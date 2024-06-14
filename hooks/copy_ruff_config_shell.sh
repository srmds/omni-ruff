#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

REPO_ROOT=$(git rev-parse --show-toplevel)
HOOK_DIR=$(dirname "$0")

PARENT_DIR=${HOOK_DIR%??????}
echo "parent dir $PARENT_DIR"

# Copy the .toml file to the parent directory
cp $PARENT_DIR/ruff.toml $REPO_ROOT/ruff.toml

echo "Copied ruff.toml to $REPO_ROOT"