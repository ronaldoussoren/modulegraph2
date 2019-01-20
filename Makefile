all:
	python3.7 -m tox

isort mypy flake8 black py36 py37:
	python3.7 -m tox -e $@

test:
	python3.7 -m tox -e py37

.PHONY: all isort mypy flake8 black py36 py37 test
