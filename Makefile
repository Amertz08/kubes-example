.PHONY: compile
compile:
	@rm -f requirements*.txt
	@pip-compile requirements.in
	@pip-compile requirements-dev.in

.PHONY: sync
sync:
	@pip-sync requirements*.txt

.PHONY: run
run:
	@fastapi dev src/main.py

.PHONY: build-image
build-image:
	@docker build -t kubes-example .

.PHONY: run-container
run-container:
	@docker run -d -p 8000:8000 kubes-example
