# PokeBerries Stats API

## Requirements

### Python

The API was developed on Python 3.12.

It will probably work with Python versions starting from 3.8, but it has not been tested on any other version than 3.12, so the recommended version is 3.12.

### Redis

You will need Redis installed for the berries caching feature. If you do not have it installed you can follow the instructions from [here](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/) to install it on your operating system.

You may also use Docker to install and manage it.

As for the version, the recommended one is 7.2.5, but the application will (probably) work with any version >=5.0.

## Installation

### Environment variables configuration

After the cloning the repository you should copy the environment file example.

Example (for Unix based systems):
```sh
cp .env.example .env
```

Then, edit it with your preferred text/code editor.

### Virtual environment (optional, but recommended)

You may also want to create a virtual Python environment for the application. The easiest way to achieve this is using the `venv` module from Python. (make sure you have it installed as on some distros it is not auto-installed with Python)

Example:
```sh
python -m venv .venv --prompt pokeberries-stats
```

and then activate it (this command might differ depending on your OS, please check the official Python guide regarding virtual environments by clicking [here](https://docs.python.org/3/tutorial/venv.html)):

```sh
source .venv/bin/activate
```

### Install requirements

Use pip to install the requirements:

```sh
pip install -r requirements.txt
```

## Usage


### Running the development server

To run the development server use:

```sh
flask run
```

If you want the webserver to reload on code changes, you may use instead:

```sh
flask run --reload
```

### Running tests

You can run the tests using:

```sh
python run_tests.py
```

### Running the production server

To run the production server you may use `waitress`:
```sh
waitress-serve app:app
```

### Docker Compose

Another way of running the application is by using Docker Compose.

You will need to change directory to the `compose` folder and then copy the environment file (the same as above).

Then you can start the application (and redis server) using:

```sh
docker compose up
```

**Note that this command will actually pull the latest Docker image of the application from the Docker hub and will run it.**

**If you would like to run your own code instead, just edit the docker-compose.yml file to build the container. (Comment the `image:` line and uncomment the `build: ` line from the api service).**