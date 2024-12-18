import os
from pathlib import Path

from aws_cdk import BundlingOptions, CfnOutput, Duration, Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as _alambda
from aws_cdk import aws_sqs as sqs
from constructs import Construct

from alberta_efiling_system_docs_scraper.utils import (
    get_all_lambda_handlers,
    get_excluded_files,
    get_lambda_runtime,
)


class AlbertaEfilingSystemDocsScraperStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        proceeding_requests_queue = sqs.Queue(
            self,
            "ProceedingRequestsQueue",
            queue_name="proceeding_requests_queue",
            visibility_timeout=Duration.seconds(300),
        )

        lambda_entry_path = "lambda"
        lambda_runtime = get_lambda_runtime()
        all_lambda_handlers = get_all_lambda_handlers(entry=lambda_entry_path)

        check_lambda_handler = _alambda.PythonFunction(
            self,
            "CheckLambdaFunction",
            function_name="check_lambda_function",
            runtime=lambda_runtime,
            entry=lambda_entry_path,
            index="check.py",
            handler="handler",
            timeout=Duration.seconds(30),
            bundling={
                "asset_excludes": get_excluded_files(all_lambda_handlers, ["check.py"])
            },
        )

        CfnOutput(
            self,
            "CheckLambdaARN",
            value=check_lambda_handler.function_arn,
            description="ARN for check lambda function",
        )

        CfnOutput(
            self,
            "ProceedingRequestsQueueURL",
            value=proceeding_requests_queue.queue_url,
            description="Link of the SQS queue for processing proceeding requests",
        )
