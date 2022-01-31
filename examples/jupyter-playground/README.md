# Steamship Jupyter Playground

This project contains a Jupyter notebook demonstrating some of Steamship's APIs.

## Initial Setup

We recommend using a python virtual environment for development. Just run the following to set it up:

First, install `venv` if you haven't already:

```bash
python3 -m pip install --user virtualenv
```

Next, create a virtualenv for this project:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m ipykernel install --user --name=jupyter-playground
```

## Developing

1. Run `jupyter notebook`
2. Select the `jupyter-playground` kernel
3. In the cell that initializes the Steamship client, put in your credentials. If you don't provide any arguments here, they will be read from `~/.steamship.json`. 