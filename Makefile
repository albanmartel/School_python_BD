# Ce Makefile a été généré avec l'aide d'une IA.

PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
PYTHON_VENV := $(VENV)/bin/python

.PHONY: venv install run clean

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r ecole/requirements.txt

run: venv
	$(PYTHON_VENV) ecole/main.py

clean:
	python -c "import shutil; shutil.rmtree('$(VENV)', ignore_errors=True)"
