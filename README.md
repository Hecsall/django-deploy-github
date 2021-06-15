# Django Github Deploy
This repository is meant to create and test a fully working Github CI that will deploy a **Django app** to a **generic VPS** over SSH.

> This is a **test** project and it's still work in progress. **Do NOT** use this if you don't know what you are doing.

`master` and `develop` branches are protected.\
Every modification will be made in branches named `feature/<username>/<task-name>`.\
From those branches, a **merge request** will be opened to `develop`.


## Setup local development environment
```sh
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```