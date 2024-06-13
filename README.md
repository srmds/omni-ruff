# Omni ruff

A global ruff rules applier

Add the following to your `.pre-commit-config.yaml`

🖥️ Bash flavour:

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: 0.1.0
    hooks:
      - id: omni-ruff-sh
        name: Copy a global Ruff config file to project repo
```

𓆙 Python flavour:

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: 0.1.0
    hooks:
      - id: omni-ruff-py
        name: Copy a global Ruff config file to project repo
```

Then run pre-commit:

```shell
$ pre-commit run --all-files
```

Output example:

```shell
Copy a global Ruff config file to project repo...........................Passed
```

In the root of your project there is an updated (or new) `ruff.toml` file containing the global ruff rules:

```shell

.
...
├── .ruff_cache
├── ruff.toml
...
```
