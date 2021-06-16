[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Django Deploy Github
This repository is meant to create and test a fully working Github CI that will deploy a **Django app** to a **generic VPS** over SSH.

> This is a **test** project and it's still work in progress. **Do NOT** use this if you don't know what you are doing.

`master` and `develop` branches are protected.\
Every modification will be made in branches named `feature/<username>/<task-name>`.\
From those branches, a **merge request** will be opened to `develop`.

The Python linter for this project will be **Flake8**. The auto-formatter for python files will be **Black** with format on save enabled. 


## Setup Github Secrets
To work, this project relies on some Github Secrets, here's the list:

- **PROJECT_NAME**: Name used for the main project folder creation on the remote VPS, and used to name configuration files related to this project. Use a lowercase name without spaces (like `my_project_name`).
- **DJANGO_APP_NAME**: Name of the main django app (folder containing the `settings.py` file), used to locate the main django folder.
- **VPS_APPS_BASE_PATH**: Base path where you store your webapps inside your VPS (like `/home/username/web`) **WITHOUT trailing `/`**.
- **VPS_HOST**:
- **VPS_PORT**:
- **VPS_SSH_KEY**:
- **VPS_USERNAME**:
- **SETTINGS_DB_HOST**:
- **SETTINGS_DB_NAME**:
- **SETTINGS_DB_PORT**:
- **SETTINGS_DB_USER**:
- **SETTINGS_DEBUG**:
- **SETTINGS_SECRET_KEY**:


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
