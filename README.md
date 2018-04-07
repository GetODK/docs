# ODK Docs

![Platform](https://img.shields.io/badge/platform-Sphinx-blue.svg) [![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/) [![Build status](https://circleci.com/gh/opendatakit/docs.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/opendatakit/docs/) [![Slack status](http://slack.opendatakit.org/badge.svg)](http://slack.opendatakit.org/)

This repo is the source for ODK documentation.

## Current Status — Live! (But still new)

Our documentation website is live at https://docs.opendatakit.org

If you can't find what you are looking for, try the [old docs on the ODK website](https://opendatakit.org/). Also, please [file an issue](https://github.com/opendatakit/docs/issues) so that we know to add the information you are looking for.

## Building and viewing documentation locally

> See the [Contributor Guide](http://docs.opendatakit.org/contributing) for detailed steps --- no prior experience needed!

Firstly, make sure you have installed [python 3.x](https://www.python.org/downloads/), we recommend you to use a virtual environment like [virtualenv](https://virtualenv.pypa.io/en/stable/) or a Python version management like [pyenv](https://github.com/pyenv/pyenv). You can take a look at your python and pip version using a  `--version` parameter.

After that, you need to clone this repo and make sure all the requirements are installed:
```bash
$ git clone https://github.com/opendatakit/docs.git
$ cd docs/
$ pip install -r requirements.txt
```
Once your environment is set up, build and run the doc site with:
```bash
$ make odk1
$ cd odk1-build
$ python -m http.server 8000
```

And we also have several `make` options you can choose.
For both ODK 1 and ODK 2:

|          |    Build     |     Clean     |     Check     |
| -------- | :---------: | :-----------: | :-----------------: |
| **Options** | build-all |  clean |  check-all |

For a specific ODK version:

|          |    Copy     |     LaTeX     |     Style Check     |    Spell Check     |    Check All   |
| -------- | :---------: | :-----------: | :-----------------: | :----------------: | :----------------: |
| **Options** | odk1_copy |  odk1-latex |  odk1-style-check | odk1-spell-check |    odk1-check     |

To build ODK 2 docs, just replace `odk1` with `odk2`. 


## How to contribute?

We are open for new issues and pull requests.

 - Please read the [Contributors Guide](http://docs.opendatakit.org/contributing) before working on the documentation.
 - Find issues to work on.
    - First time contributors are encouraged to complete a [line edit](https://github.com/opendatakit/docs/issues/96) as a way to get familiar with our contribution process.
	- Issues labelled [easy](https://github.com/opendatakit/docs/labels/easy) do not require much specific technical knowledge.
	- Issues labelled [contributor friendly](https://github.com/opendatakit/docs/labels/contributor%20friendly) are usually self-contained and don't require extensive knowledge of the ODK ecosystem as a whole.
	
You can also...

 - [Discuss the documentation from a user perspective in our forum](https://forum.opendatakit.org/c/development/documentation).
 - [Discuss the documentation from a contributor perspective in our developer Slack](slack.opendatakit.org). (Use the #docs-code channel.)
 - [File an issue](https://github.com/opendatakit/docs/issues) for any needed improvements.
 - [Watch](https://github.com/opendatakit/docs/subscription) and star this repo, to keep up with what we're doing.

## Troubleshooting
- If you get an extension error or a configuration error:
  - Make sure your virtual environment is activated.
  - type `python --version` to set their current python version (it should be 3.x).
  - run `pip install -r requirements.txt`.


