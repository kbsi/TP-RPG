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

## Our CI Tool choice

We will be using **GitHub Actions** for our CI tool.

GitHub Actions is a CI/CD solution built into GitHub, perfect for automating tests and deployments directly from the repository. Its main advantages include seamless integration, customizable workflows, and free minutes for public repositories. However, limitations include high costs for heavy usage, restricted resources on GitHub-hosted runners, and limited debugging capabilities. It’s ideal for GitHub projects, but complex pipelines may benefit from more flexible CI/CD tools.

## Our CI/CD pipeline with GitHub Actions

### Git structure

We will use the following structure for our repository:

- master : this branch is the main branch and reflect the current production version
- dev : this branch is the current development branch where developers will push their commits
- failures/\* : If a commit fails during the CI/CD pipeline, it will be pushed to this branch

### Step 1: Create a new GitHub Actions workflow

- Create a new file in the `.github/workflows` directory of your repository, e.g. `rpg-actions.yml`
- This file will contain the configuration for our CI/CD pipeline.

### Step 2 : Define the pipeline

- for every commit on dev branch, run the tests
- if the tests pass, push the commit to master
- if the tests fail, push the commit to a new branch failures/[unique number] and reset the commit on dev

### Step 3 : Define the jobs and steps

- build : set up Python environment, install project dependencies, lint the code with flake8, run the tests with unittest
- merge-to-master : if build is success, push the commit to master
- handle-failure : if build fails, push the commit to a new branch failures/[unique number] and reset the commit on dev
