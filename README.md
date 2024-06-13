# Omni ruff

A global ruff rules applier

Add the following to your `.pre-commit-config.yaml`

Bash support:

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: main
    hooks:
      - id: omni-ruff-sh
        name: Copy a global Ruff config file to project repo
        entry: hooks/copy_ruff_config_shell.sh
        language: script
```

Python support:

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: main
    hooks:
      - id: omni-ruff-py
        name: Copy a global Ruff config file to project repo
        entry: hooks/copy_ruff_config.py
        language: python
```

Then run pre-commit:

```shell
pre-commit run --all-files
```
