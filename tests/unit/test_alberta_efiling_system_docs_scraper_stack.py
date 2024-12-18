import aws_cdk as core
import aws_cdk.assertions as assertions

from alberta_efiling_system_docs_scraper.alberta_efiling_system_docs_scraper_stack import AlbertaEfilingSystemDocsScraperStack

# example tests. To run these tests, uncomment this file along with the example
# resource in alberta_efiling_system_docs_scraper/alberta_efiling_system_docs_scraper_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AlbertaEfilingSystemDocsScraperStack(app, "alberta-efiling-system-docs-scraper")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
