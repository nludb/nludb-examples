# Steamship COrpus Importer Plugin

This project implements a basic Steamship Corpus Importer that you can customize and deploy for your own use.

In Steamship, **Corpus Importers** are responsible for importing data into the Steamship platform -- a corpus at a time! 
A corpus importer's job is to return the list of File Importer requests that will assemble the corpus.

This sample project simply imports two files from a pre-loaded test importer hard-coded into the Steamship Engine. But it provides a base that you can extend to:

* Import an entire RSS feed of podcasts
* Import an entire Notion site
* Import an entire HelpScout knowledge base

Once a Corpus Importer has returned a list of FileImport requests to Steamship, Steamship will immediately begin running them to import your data.

## First Time Setup

We recommend using Python virtual environments for development.
To set one up, run the following command from this directory:

```bash
python3 -m venv .venv
```

Activate your virtual environment by running:

```bash
source .venv/bin/activate
```

Your first time, install the required dependencies with:

```bash
python -m pip install -r requirements.dev.txt
python -m pip install -r requirements.txt
```

## Developing

All the code for this plugin is located in the `src/api.py` file:

* The CorpusImporterPlugin class
* The `/import_corpus` endpoint

## Testing

Tests are located in the `test/test_api.py` file. You can run them with:

```bash
pytest
```

## Deploying

Deploy your converter to Steamship by running:

```bash
ship deploy
```

That will deploy your app to Steamship and register it as a plugin for use.

**This will also provide a plugin handle. Make sure to copy this down! You will need this to call your plugin.**

## Using

Once deployed, your Corpus Importer Plugin can be referenced by the handle in your `steamship.json` file.

```python
from steamship import Corpus, Steamship, CorpusImportRequest

MY_PLUGIN_HANDLE = ".. fill this out .."

client = Steamship()
request = CorpusImportRequest() # Provide the appropriate parameters
file = client.create_file(importer=MY_PLUGIN_HANDLE, request=request)
```

### Using in a Jupyter Notebook

To use the plugin in a notebook, first install Jupyter

```bash
python3 -m pip install jupyter
jupyter notebook
```

Create a new notebook, and then copy and paste the following

## Sharing

Please share what you've built with hello@steamship.com! 

We would love take a look, hear your suggestions, help where we can, and share what you've made with the community.