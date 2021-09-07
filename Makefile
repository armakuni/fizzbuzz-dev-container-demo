.PHONY: build
# builds fizzbuzz app image
build:
	docker build -t fizzbuzz:latest .

.PHONY: install
# installs requirements.txt
install:
	pip install -r requirements.txt

.PHONY: test
# runs unit tests
test:
	python -m pytest -m "not integration"

.PHONY: integration
# runs integration tests against running service
integration:
	python -m pytest -m "integration"

.PHONY: all
# runs unit and integration tests
all: test integration
