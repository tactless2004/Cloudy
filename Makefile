lint-win:
	python -m pylint weatherapi/*.py
	python -m pylint TUI/**/*.py
	python -m pylint UI.py

lint:
	pylint $(shell git ls-files '*.py')
