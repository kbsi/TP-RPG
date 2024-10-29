# RPG project for Continues Integration course

## Prerequies

Before you begin, make sure you have the following installed on your environment:

- Python (version 3.x recommended)
- Pip (package manager for Python)
- Pipenv (tool for managing virtual environments and dependencies)

### Installing Pipenv

If Pipenv is not already installed, you can install it using pip:

```bash
pip install pipenv
```

### Loading the Project Packages

```bash
pipenv install
```

### Activating the Virtual Environment

```bash
pipenv shell
```

Once activated, you should see the name of the virtual environment in your command prompt.

## To run all tests in the virtual environment :

```python
pipenv run python3 -m unittest discover -s test
```
