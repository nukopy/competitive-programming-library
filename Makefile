.PHONY: test
test: ## Test all python modules with pytest
	@echo "Testing all python modules"
	@pytest -v
