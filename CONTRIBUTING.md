# Contributing to this project

## Local development setup

First, a python intepreter is required. Python3.8 or later. It is then highly recommended to use a virtual environment to manage dependencies. This can be done by running the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r dev_requirements.txt
```

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
