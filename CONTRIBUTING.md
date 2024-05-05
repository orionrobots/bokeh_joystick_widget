# Contributing to this project

## Local development setup

First, a python interpreter is required. Python3.9 or later. Install poetry, then install the development app and dependencies with:

```bash
poetry install
```

You can then enter the virtual environment with:

```bash
poetry shell
```

## Running linters

This project requires PR's to pass pre-commit checks. To set up the hooks:

```bash
pre-commit install-hooks
```

You can then run pre-commit from a command line with:

```bash
pre-commit run --all-files
```

You can also have this run before committing by setting up a git hook:

```bash
pre-commit install
```
