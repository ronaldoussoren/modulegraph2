all:
	python3.7 -m tox

isort mypy flake8 black documentation py36 py37:
	python3.7 -m tox -e $@

test:
	python3.7 -m tox -e py37

dotview:
	python3.7 -m modulegraph2 > ../f.dot && dot -Tpng ../f.dot -o ../f.png && open ../f.png

.PHONY: all isort mypy flake8 black py36 py37 test dotview
