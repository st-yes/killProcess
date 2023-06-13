#check before if python3.7 exist
PYTHON = python3.7

# Specify the target and dependencies
all: script

# Define the rule to execute script1
script:
	@echo "run aliasCreation.py"
	@$(PYTHON) aliasCreation.py
