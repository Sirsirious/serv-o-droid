.PHONY: init \
init-npm \
init-venv \
create-venv \
update-venv \
clean \
clean-npm \
clean-venv \
clean-pyc \
clean-sls \
clean-test \
test \
docker-up \
deploy \
local

# Default goal
.DEFAULT_GOAL := help

# Python requirements
VENV ?= venv
REQUIREMENTS ?= requirements.txt
BE_PORT = 8000
FE_PORT = 3003


help:
	@echo "Usage: make [TARGET]"

init: clean init-npm init-venv

init-npm:
	@( \
		cd frontend; \
		npm install; \
		echo "PORT="$(FE_PORT) > .env; \
	)


init-venv: clean-venv create-venv update-venv

create-venv:
	@echo "Creating venv: $(VENV)..."
	@python3 -m venv $(VENV)

update-venv:
	@echo "Updating venv: $(VENV)..."
	@( \
		. $(VENV)/bin/activate; \
		pip install --upgrade pip; \
		pip install -r $(REQUIREMENTS); \
		pre-commit install; \
	)

clean: clean-npm clean-venv

clean-npm:
	@echo "Cleaning npm..."
	@( \
		cd frontend; \
		@rm -rf node_modules; \
	)

clean-venv:
	@echo "Cleaning venv: $(VENV)..."
	@rm -rf $(VENV)

local-frontend: init-npm
	@echo "Running local frontend..."
	@( \
		cd frontend; \
		npm start & \
		export FE_PID=(echo $!); \
	)
	@echo "Started local frontend on port $(FE_PORT)"

local-backend: init-venv
	@echo "Running local backend..."
	@( \
		. $(VENV)/bin/activate; \
		uvicorn app.main:app --reload --port $(BE_PORT) & \
		export BE_PID=(echo $!); \
	)
	@echo "Started local backend on port $(BE_PORT)"

local: local-backend local-frontend