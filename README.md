# Tavern flask plugin

## YAML configuration

The test definition looks like this:

```yaml
---
test_name: Test example
flask:
  app:
    location: flask_module
stages:
  - name: Test example
    request:
      url: "http://localhost:5000/example"
      method: GET
    response:
      status_code: 200
```

This assumes that: `flask_module` is a python module that implements the function [create_app()](https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/#basic-factories).

## Using `poetry`

1. Add the tavern plugin as a dev dependency;

```shell
$ poetry add --group dev git+https://github.com/jeremad/tavern-flask.git
```

2. Use this plugin as the HTTP entrypoint.

* In `pyproject.toml`:

```toml
[tool.poetry.plugins."tavern_http"]
"flask" = "tavern_flask.tavernhook"
```

* In the `pytest` command line:

```shell
$ poetry run pytest --tavern-http-backend=flask
```
