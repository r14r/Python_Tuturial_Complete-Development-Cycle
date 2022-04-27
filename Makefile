default:
	cat Makefile

run:
	@python src/main.py


clean:
	@echo cleanup __pycache__ folders
	@find src test -name __pycache__ -exec rm -rf {} \;

.PHONY: test
test: clean
	@echo run test
	@pytest -v


style:
	@isort .
	@black .