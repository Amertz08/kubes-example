.PHONY: compile
compile:
	@rm -f requirements*.txt
	@pip-compile requirements.in
	@pip-compile requirements-dev.in

.PHONY: sync
sync:
	@pip-sync requirements*.txt
