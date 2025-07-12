lint-win:
	python -m pylint weatherapi/*.py
	python -m pylint TUI/**/*.py
	python -m pylint UI.py
	pyright

lint:
	pylint $(shell git ls-files '*.py')
	pyright
