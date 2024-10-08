fmt:
	poetry run ruff format .
.PHONY: fmt

lint: fmt
	poetry run ruff check . --fix
.PHONY: lint

dev-server-start: fmt
	poetry run uvicorn --log-level=debug thing_payloads_service.service:server --reload --port 8001
.PHONY: dev-server-start

server-start: fmt
	poetry run uvicorn thing_payloads_service.service:server --port 8001 &
.PHONY: server-start

test-unit: fmt
	poetry run pytest tests/unit/
.PHONY: test-unit

test-integration: fmt
	poetry run pytest tests/integration/
.PHONY: test-integration

test: fmt
	poetry run pytest tests/
.PHONY: test
