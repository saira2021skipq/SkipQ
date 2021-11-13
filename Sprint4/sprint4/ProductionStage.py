from aws_cdk import core
from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines
from sprint4.hello_lambda_stack import HelloLambdaStack

class ProductionStage(core.Stage):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        service=HelloLambdaStack(self,"BetaService")