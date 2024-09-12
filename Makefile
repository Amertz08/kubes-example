.PHONY: compile
compile:
	@rm -f requirements*.txt
	@pip-compile requirements.in

.PHONY: sync
sync:
	@pip-sync requirements*.txt
