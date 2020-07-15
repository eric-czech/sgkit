# sgkit
Statistical genetics toolkit

## Developer documentation

### Build and test

From a Python virtual environment run:

```bash
pip install -r requirements.txt -r requirements-dev.txt
pytest
```

To check code coverage and get a coverage report, run

```bash
pytest --cov=sgkit --cov-report term-missing
```

### Code standards

Run the following to enforce (or check) the source code adheres to our coding standards.

```bash
isort -rc .
black .
flake8
mypy --strict .
```

You can use [pre-commit](https://pre-commit.com/) to check or enforce the coding standards when you commit your code. Install the git hook using:

```bash
pre-commit install
```

Note that pre-commit does not run the `mypy` check, so you will need to run that manually before submitting a pull request.
