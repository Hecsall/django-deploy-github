[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Django Github Deploy
This repository is meant to create and test a fully working Github CI that will deploy a **Django app** to a **generic VPS** over SSH.

> This is a **test** project and it's still work in progress. **Do NOT** use this if you don't know what you are doing.

`master` and `develop` branches are protected.\
Every modification will be made in branches named `feature/<username>/<task-name>`.\
From those branches, a **merge request** will be opened to `develop`.

The Python linter for this project will be **Flake8**. The auto-formatter for python files will be **Black** with format on save enabled. 

## Setup local development environment
Setup Python Virtual Environment, and install dependencies
```sh
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Run `black` formatter from your terminal to auto fix all "auto-fixable" issues inside python files.
```sh
black --exclude=venv/ .
```

Test python files before pushing (if there are errors, the CI will fail and won't deploy anything).\
*Note: we use `pflake8` because that will read flake8 configurations from the `pyproject.toml` file.*
```sh
# From the root folder of the project
pflake8 --exclude=venv/ --count .
```
