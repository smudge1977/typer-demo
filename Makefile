#!make
SHELL := /bin/bash

# minus means don't fail if no .env - this is a convience for when in VScode etc.
# These variables are not yet exported for sub commands to use
-include .env
# -include ./venv/bin/activate

NAME := $(shell grep '^name = ' pyproject.toml | head -1 | cut -d \" -f2)
VENV := $(shell which python | grep '/venv/')

.DEFAULT_GOAL := help

.PHONY: help
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


##@ Fixup

.PHONY: format 
format: ## Do code formating (actually update things)
	# yapf --in-place --recursive ./$(NAME) ./tests
	isort --profile=black --lines-after-imports=2 ./tests/ ./$(NAME)
	black ./tests/ ./$(NAME) # Black is a little too opinionated for the code at the moment!


##@ Utility

.PHONY: lint
lint: ## Lint code
	isort --profile=black --lines-after-imports=2 --check-only ./tests/ ./$(NAME) # Been done in format this is relivant is we put this in a pipeline and we fail here
	black --check ./tests/ ./$(NAME) --diff # Been done in format this is relivant is we put this in a pipeline and we fail here
	flake8 ./tests/ ./$(NAME)


.PHONY: analyse
analyse: ## Type checking and code complexity
	bandit $(NAME)/*.py
# Lets keep it secure
# prospector src/fos6_eon - conflicting dependacies with flake8!
# echo "### Cyclomatic Complexity (CC)"
	radon cc $(NAME)
# echo "### Maintainability Index"
	radon mi $(NAME)
	liccheck
	mypy $(NAME)


.PHONY: test
test: ## test and analyse # lint analyse
	python3 -m doctest $(NAME)/*.py
	pytest


.PHONY: build
build: ## Uninstall package and build the dist
	# Bump minor version 0.0.x or if merging to branch ["main", "master", "release-*"] bump version
	cicd/version-bump.sh
	pip uninstall -y $(NAME)
	flit build
	pip install -e ".[dev,test]"
	@if [[ -f $(NAME)/app.py ]]; then \
		pyinstaller -y $(NAME)/app.py -n $(NAME)-$(shell uname -m) --onefile; else \
		echo "No $(NAME)/app.py not building single EXE"; fi 


.PHONY: releae
release: ## JIRA something? And put on Github release? And bump release version? Nexus publishing too? Does nexus not get fed by Github? GH is eaisier to "see" for eBin stuff
	echo "Released!"
