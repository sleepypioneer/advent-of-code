# Advent of Code 2023


Following along challenges here https://adventofcode.com/2023

## Running

### Install dependencies

```bash
poetry install
```

### Run individual days

example for day 1

```bash
poetry run python -m 2023.day_1.main
```

### Run tests

```bash
poetry run pytest
```

## Workflows

There are multiple workflows setup to run tests and linting on push requests via GitHub Actions. You can also run these locally with [act](https://github.com/nektos/act) using the command:

```bash
# list all workflows
act list --container-architecture linux/amd64 # optional only for mac os

# run a specific workflow
act -j python-lint --container-architecture linux/amd64

act -j python-tests --container-architecture linux/amd64
```
