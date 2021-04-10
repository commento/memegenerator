# memegenerator

## Overview
This meme generator can be used a CLI or a web flask app to generate random meme or to create a meme giving the image and the quote (body and author)

## Instructions
git clone the repository and start a virtual environment with command:

```python3 -m venv venv```

access the virtual environment:

```source venv/bin/activate```

install the dependencies:

```pip install -r requirements.txt```

run the CLI command with:

```python meme.py```

with optional arguments that you can check with `--help` option.


The flask web app can be started with the command

```python app.py```

## Roles and responsability
The `MemeEngine` module contains the `MemeGenerator` that has the method `make_meme`.
The method creates the meme associating the image with the text given as input

The `QuoteEngine` module contains the Ingestors and the `QuoteModel` class.
The Ingestors takes files as input and translate them into a list of `QuoteModel` instances.