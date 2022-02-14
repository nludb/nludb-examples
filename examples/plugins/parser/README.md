# Steamship Parser Plugin

This project implements a basic Steamship Parser that you can customize and deploy for your own use.

In Steamship, **Parsers** are responsible for text into sentences, tokens, and tags upon those tokens using the **Steamship Block Format**.

This sample project transform (assumed) paragraphs into sentences and tokens using simple whitespace, but the implementation you create might:

* Use SpaCy to parse text
* Use some custom-trained parser based on your domain to parse text

Once a Parser has returned data to Steamship as **Block Format**, that data is ready for use by the rest of the ecosystem. 
For example, you could perform a query over the sentences or embed each sentence.

## Cloning from the CLI

This example can be created using the Steamship CLI. For example

```
$ ship create name-of-your-plugin-goes-here

What kind of project would you like to create?
( ) App - A full-stack, natural language microservice.
(x) Plugin - Extend Steamship with your own model.
( ) Project - A project which uses Steamship.

What kind of plugin?
( ) Corpus Importer - Import a corpus from another service.
( ) File Importer - Import a file from another service.
( ) Converter - Convert a data type into Steamship's Block Format.
(x) Parser - Parse natural language text into tokens and tags.
( ) Embedder - Embed natural language text into vectors of meaning.

$ cd name-of-your-plugin-goes-here
```

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

* The ParserPlugin class
* The `/parse` endpoint

## Testing

Tests are located in the `test/test_api.py` file. You can run them with:

```bash
pytest
```

We have provided sample data in the `test_data/` folder.

## Deploying

Deploy your converter to Steamship by running:

```bash
ship deploy
```

That will deploy your app to Steamship and register it as a plugin for use.

**This will also provide a plugin handle. Make sure to copy this down! You will need this to call your plugin**

## Using

Once deployed, your Convert Plugin can be referenced by the handle in your `steamship.json` file.

```python
from steamship.plugin.parser import ParseRequest
from steamship.plugin.service import PluginRequest
from steamship import Steamship

steamship = Steamship()

TEST_REQ = ParseRequest(
    docs=["Hi there.\nI just made my first Steamship Plugin.\nTime to make some cool plugins."]
)
res = steamship.parse(docs=TEST_REQ.docs, plugin="YOUR PLUGIN HANDLE COPIED ABOVE")
res.wait()
res.data.blocks
```

### Using in a Jupyter Notebook

To use the plugin in a notebook, first install Jupyter

```bash
python3 -m pip install jupyter
jupyter notebook
```

Create a new notebook, and then copy and paste the following

```python
from steamship.plugin.parser import ParseRequest
from steamship.plugin.service import PluginRequest
from steamship import Steamship

steamship = Steamship()

TEST_REQ = ParseRequest(
    docs=["Hi there.\nI just made my first Steamship Plugin.\nTime to make some cool plugins."]
)
res = steamship.parse(docs=TEST_REQ.docs, plugin="YOUR PLUGIN HANDLE COPIED ABOVE")
res.wait()
res.data.blocks
```

## Sharing

Please share what you've built with hello@steamship.com! 

We would love take a look, hear your suggestions, help where we can, and share what you've made with the community.