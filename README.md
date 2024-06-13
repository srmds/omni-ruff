# Omni ruff

A global ruff rules applier

Add the following to your `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: master
    hooks:
      - id: omni-ruff
        name: Copy a global Ruff config file to project repo
        entry: hooks/copy_ruff_config.sh
        language: script
```

Then run pre-commit:

```shell
$ pre-commit run --all-files
```

