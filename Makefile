PYTHON=python3.6
all:
	$(PYTHON) -m tox

isort mypy flake8 black documentation py36 py37 py38:
	$(PYTHON) -m tox -e $@

test:
	$(PYTHON) -m tox -e py37

dotview:
	$(PYTHON) -m modulegraph2 > ../f.dot && dot -Tpng ../f.dot -o ../f.png && open ../f.png

.PHONY: all isort mypy flake8 black py36 py37 py38 test dotview
