from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines
from sprint4.ProductionStage import ProductionStage

class Sprint4Stack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = pipelines.CdkPipeline(self, 'SairaPipelineTest1',
        cloud_assembly_artifact=cloud_assembly_artifact,
        

        source_action=cpactions.GitHubSourceAction(
        action_name='GitHub_Source',
        output=source_artifact,
        oauth_token=core.SecretValue.secrets_manager('saira_pipeline_token', json_field='saira_pipeline_token'),
        owner='saira2021skipq',
        repo='pipeline_web_services',
        branch= 'master',
        trigger=cpactions.GitHubTrigger.POLL),

        synth_action=pipelines.SimpleSynthAction(
        source_artifact=source_artifact,
        cloud_assembly_artifact=cloud_assembly_artifact,
        install_command='npm install -g aws-cdk && pip install -r requirements.txt',
        synth_command='cdk synth'))
        
        pipeline.add_application_stage(ProductionStage(self,'prepod',env={
            'account':'315997497220',
            'region':'us-east-2'
        }))

