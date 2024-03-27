# Contributing

All configuration for the project should be put into `pyproject.toml`.

## Working locally

1. Create a virtualenv using whatever method you like (
   eg, [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/))

1. Install dependencies from requirements.txt

## Updating/adding a dependency

1. Add or update the dependency in [pyproject.toml](/pyproject.toml)

1. Update constraints file

```shell
uv pip compile --all-extras pyproject.toml --output-file constraints.txt -U
```

## Pre-commit

Basic checks (formatting, import order) is done with pre-commit and is controlled by [the yaml file](/.pre-commit-config.yaml).

After installing dependencies, Run

    # check it works
    pre-commit run --all-files
    pre-commit install

Run every so often to update the pre-commit hooks

    pre-commit autoupdate

### Fixing Python formatting issue

    ruff format tavern/ tests/
    ruff --fix tavern/ tests/

### Fix yaml formatting issues

    pre-commit run --all-files
