setup:
	pip install -e .
	noqa
test:
	pytest
	noqa
lint:
	noqa
	noqa
doc:
	noqa
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache