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

## Running the development server

To run the development server use:

```sh
flask run
```

If you want the webserver to reload on code changes, you may use instead:

```sh
flask run --reload
```
