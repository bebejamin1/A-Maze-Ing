PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip

FLAKE8 = venv/lib/python3.10/site-packages/flake8
MYPY = venv/lib/python3.10/site-packages/mypy
PYDANTIC = venv/lib/python3.10/site-packages/pydantic
NUMPY = venv/lib/python3.10/site-packages/numpy
TYPING = venv/lib/python3.10/site-packages/typing-extensions

all : run

venv/bin/activate : 
	python3 -m venv venv

$(FLAKE8) : 
	$(PIP) install -r requirement.txt

$(MYPY) : 
	$(PIP) install -r requirement.txt

$(PYDANTIC) :
	$(PIP) install -r requirement.txt

$(NUMPY) :
	$(PIP) install -r requirement.txt

$(TYPING) :
	$(PIP) install -r requirement.txt

install : venv/bin/activate  requirement.txt $(FLAKE8) $(MYPY) $(PYDANTIC) $(NUMPY) $(TYPING)


run : install
	$(PYTHON) a_maze_ing.py config.txt

debug :
	$(PYTHON) -m pdb a_maze_ing.py config.txt

lint : install
	. ./venv/bin/activate && \
	flake8 --exclude venv && \
	mypy . --exclude venv --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict : install
	. ./venv/bin/activate && \
	flake8 . --exclude venv && \
	mypy . --strict --exclude venv

clean : 
	find . -name "__pycache__" -exec rm -rf {} \+
	find . -name ".mypy_cache" -exec rm -rf {} \+
	find . -name ".vscode" -exec rm -rf {} \+

uninstall : requirement.txt
	$(PIP) uninstall -r requirement.txt

uninstall_venv :
	rm -rf venv

.PHONY: clean lint run install uninstall