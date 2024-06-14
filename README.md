# Omni ruff

A global ruff rules applier

Add the following to your `.pre-commit-config.yaml`

🖥️ Bash flavour (toy functionality):

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: 0.6.12
    hooks:
      - id: omni-ruff-sh
        name: Copy a global Ruff config file to project repo
```

𓆙 Python flavour (toy functionality):

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: 0.6.12
    hooks:
      - id: omni-ruff-py
        name: Copy a global Ruff config file to project repo
```

☁️ Azure private hosted repo flavour:

```yaml
repos:
  - repo: https://github.com/srmds/omni-ruff
    rev: 0.6.12
    hooks:
      - id: omni-ruff-az
        name: Copy a global Ruff from a private Azure Repo to project repo
        args: [--config=global-ruff.toml] # provide path to global ruff config file in source repo
```

---

Then export needed env vars:

_only needed when using azure - private repo flavour_

```shell
$ export ORG=<VALUE> && \
 export PROJECT=<VALUE> && \
 export REPO=<VALUE> && \
 export PAT=<VALUE> 
```

or via `.env` export:

```shell
$ touch .env
```

After copy/pasting below, add the needed values to the variables inside the .env file

```text
ORG=<VALUE>
PROJECT=<VALUE>
REPO=<VALUE>
PAT=<VALUE>
```

Then export all the variables at once:

```shell
$ set +o && source .env && set -0
```

---

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
