## :construction: Installation

### Minimum requirements

- [Python](https://www.python.org/) 3.7
- [Poetry](https://python-poetry.org/) 1.4.2
- [Docker](https://docs.docker.com/install/) 20.10.23
- [Docker Compose](https://docs.docker.com/compose/install/) 2.15.1

### Install the application locally

- Run `git clone git@github.com:your-organisation/symeo-python-template.git` or `git clone https://github.com/your-organisation/symeo-python-template.git` to clone the repository
- Run `cd symeo-python-template` to navigate to the code folder
- Run `poetry install` to install node dependencies
- Run `docker-compose up` to start the local PostGreSQL Database
- Run `cp .env.example .env.local` to copy the example dot env file
- Edit the created `.env.local` file with the relevant variable values
- Run `poetry run uvicorn src.bootstrap.main:bootstrap --port 9999 --reload` to start the application on the 9999 port with hot reload

## :wrench: Development

### Coding conventions

The coding conventions and style are enforced by the [ruff](https://beta.ruff.rs/docs/) linter and the [black](https://github.com/psf/black) formatter. The configuration can be found in the [pyproject.toml](pyproject.toml).

To check linting error in command line, run `poetry run ruff check <target_directory>`.

To fix automatically format errors, run `poetry run black <target_directory>`.

We use [swagger](https://swagger.io/) to create documentation of our API
- Launch the application with `poetry run uvicorn src.bootstrap.main:bootstrap --port 9999 --reload` and then go to your browser and type `http://localhost:9999/docs` to see the documentation of the API.
