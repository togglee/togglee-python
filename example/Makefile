
help:
	@echo "clean - remove all build, test, coverage and Python artifacts"

all: default run

default: clean deps

.venv:
	if [ ! -e ".venv/bin/activate_this.py" ] ; then virtualenv --clear .venv ; fi

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

deps: .venv
	. .venv/bin/activate && pip3 install -U -r requirements.txt

run: clean
	. .venv/bin/activate && python3 main.py
