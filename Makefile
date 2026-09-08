# Ce Makefile a été généré avec l'aide d'une IA.

PYTHON := python
VENV := ecole/.venv
PIP := $(VENV)/Scripts/pip.exe
PYTHON_VENV := $(VENV)/Scripts/python.exe

.PHONY: venv install run clean

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r ecole/requirements.txt

run: venv
	$(PYTHON_VENV) ecole/main.py

clean:
	$(PYTHON) -c "import shutil; shutil.rmtree('$(VENV)', ignore_errors=True)"

