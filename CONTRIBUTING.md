# Contributing to ``Multi-Language-RTVC``

Being an open source project, ``MLRTVC`` depends on developers, users and students contributing in
various ways. We try to make contributing to this project as easy and transparent as possible.  
There are multiple ways to contribute:

- Developing code (new features, fixes, enhancements)
- Writing documentation
- Raising issues (bugs, feature requests, enhancement proposals, code refacturing, etc.)
- Providing pre-trained models
- Participating in community tasks (code reviews, discussions, maintenance, etc.)

## GitHub-centered development

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.
For reasons of maintainability and simplicity, GitHub is currently the only code repository for
this project.

## Developing code

To contribute code to this repository, please follow these rules:

1. Make your changes/additions and push the code.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Make sure your code meets the quality standards.

### Quality standards

To make the code easy to read, maintainable and understandable for everyone, follow these
essential rules:

1. Keep your code as short as possible but as long as necessary.
2. Keep the code simple and clean, no links, statements or advertisement.
3. Comment your code both single-line and docstring-wise.
4. Follow the [``Module template``](templates/code_templates/module_template.py) to write a
clean and simple module/script with required head information.
5. All code is formatted using [``Black``](https://pypi.org/project/black/).

#### Black format

``Black`` is a Python code formatter replacing time-consuming hand-formatting.
It is used as this project's default style.

To install ``Black``, run

```python
pip install black
```

To format a file in Black-style, run

```python
black PATH_TO_FILE
```

To format a directory with all its files, run

```python
black PATH_TO_DIR
```

Follow these steps to push code to this repository:

1. Fork the project repository.
2. Clone your fork.
3. Navigate to your local repository.
4. Check that your fork is ghe ``origin`` remote by typing ``git remote -v``.
5. Add the project repository as the ``upstream`` remote by typing ``git remote add upstream URL_OF_PROJECT``.
6. Pull latest changes from upstream into your local repository with ``git pull upstream main``.
7. Check your current branch with ``git branch`` (initially ``main``).
8. Create a new branch with ``git checkout -b BRANCH_NAME``.
9. Check that you are in the new branch with ``git branch``.
10. Make changes in your local repository.
11. Stage your changes with ``git add -A`` or ``git add PATH_TO_FILE``.
12. Commit your changes with ``git commit -m "MESSAGE"``.
13. Push your changes to your fork with ``git push origin BRANCH_NAME``.
14. Navigate to your fork and start a pull request. Don't forget to describe your changes and to
reference related issues or authors.

Note: Contributions made will be under the ``MIT`` license.

## Bug reports

Report bugs by opening issues. Good bug reports have

- A summary and/or background
- Instructions for a minimal repoducable example
  - Code snippets
  - Sample code
  - Dummy scripts
- What you expected would happen
- What actually happened
- Notes (possibly including why you think this might have happened, or stuff you tried that didn't work)

## Feature requests

Features are requested by opening issues. Good feature requests contain

- A description of the desired feature
- The current state of the code
- The desired future state of the code
- Reasons why this can't be achieved otherwise

## Providing trained models

Providing trained models is a good way of support developers or engineers who are in need of models
that can be immediately used, without having to go through the time-consuming training process. To ensure
the uniformity of trained models in the repository, please follow these steps:

1. Navigate to the directory [``mlrtvc/saved_models``](mlrtvc/saved_models).
2. Choose the directory fitting your model language.
3. Save the model under the name ``<model_author_date_version>`` like e.g. ``model_sveneschlbeck_01012022_v1``.
4. Follow the structure given described [here](templates/saved_models_templates) to structure your model
in the following way:
```
<model_author_date_version>
  - encoder
    - encoder.pt
    - training outputs
      - [model backups]
      - [visualizations]
  - synthesizer
    - synthesizer.pt
    - training_outputs
      - [model backups]
      - [samples]
  - vocoder
    - vocoder.pt
    - training_outputs
      - [model backups]
      - [samples]
```

## Issue templates

Take a look at these [``Issue Templates``](templates/issue_templates) for issue templates to get an idea of what issues should
look like to be readable.
