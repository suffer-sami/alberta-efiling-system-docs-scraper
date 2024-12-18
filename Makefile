LAMBDA_DIR=lambda
REQUIREMENTS_TXT=$(LAMBDA_DIR)/requirements.txt

install:
	@echo "Installing Python dependencies..."
	uv sync

bootstrap:
	@echo "Bootstrapping stack in your aws account"
	uv run --env-file .env cdk bootstrap
	
export-dependencies:
	@echo "Exporting Lambda dependencies..."
	uv export --only-group lambda-dependencies --no-header --no-editable --no-hashes > $(REQUIREMENTS_TXT)

deploy: export-dependencies
	@echo "Deploying CDK stack..."
	uv run --env-file .env cdk deploy

deploy-hotswap: export-dependencies
	@echo "Performing CDK hotswap deployment..."
	uv run --env-file .env cdk deploy --hotswap

clean: 
	@echo "Cleaning up..."
	uv run --env-file .env cdk destroy