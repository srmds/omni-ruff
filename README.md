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

☁️ Azure private hosted repo flavour:

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: 0.1.0
    hooks:
      - id: omni-ruff-az
        name: Copy a global Ruff from a private Azure Repo to project repo
        args: [--config=global-ruff.toml] # provide path to global ruff config file in source repo
```

Then export needed env vars:

```shell
$ export ORG=<VALUE> && \
 export PROJECT=<VALUE> && \
 export REPO=<VALUE> && \
 export PAT=<VALUE> 
```

or via `.env` export:

```shell
$ cp template.env .env
# After copy, add the needed values to the variables inside the .env file

# Then export all the variables at once:
$ set +o && source .env && set -0
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