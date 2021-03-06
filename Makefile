PYTHON = python3
PIP = pip3
VENV_DIRECTORY = venv
PROJECT_DIRECTORY = python_connector_template

.DEFAULT_GOAL = help

help:
	@echo "make venv_init - set up and activate venv for the project"
	@echo "make setup - set up the project locally"
	@echo "make test - run the tests for the project"
	@echo "make cover - check test coverage for the project"
	@echo "make lint - run linter against the project"
	@echo "make clean - remove venv directory from the project"

venv_init:
	${PYTHON} -m venv ${VENV_DIRECTORY}

setup:
	${VENV_DIRECTORY}/bin/${PIP} install -r requirements.txt
	${VENV_DIRECTORY}/bin/${PIP} install -r tests/requirements.txt

install_locally:
	${VENV_DIRECTORY}/bin/${PIP} install .

test:
	${VENV_DIRECTORY}/bin/${PYTHON} -m pytest

cover:
	${VENV_DIRECTORY}/bin/pytest --cov ${PROJECT_DIRECTORY} --cov-fail-under=80 tests

lint:
	flake8 ${PROJECT_DIRECTORY}

clean:
	rm -rf venv
	rm -rf build
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm .coverage
