lint-win:
	python -m pylint weatherapi/*.py
	python -m pylint TUI/**/*.py
	python -m pylint UI.py
	pyright

lint:
	if [ -d .venv ]; then \
		.venv/bin/python -m pylint $(shell git ls-files '*.py'); \
		.venv/bin/python -m pyright; \
	elif [ -d venv ]; then \
		venv/bin/python -m pylint $(shell git ls-files '*.py'); \
		venv/bin/python -m pyright; \
	else \
		pylint $(shell git ls-files '*.py'); \
		pyright; \
	fi

docker:
	docker buildx build -t cloudy .
	docker run -it cloudy
