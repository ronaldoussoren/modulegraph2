all:
	python3.7 -m tox


mypy flake8 black py36 py37:
	python3.7 -m tox -e $@

test:
	python3.7 -m tox -e py37
