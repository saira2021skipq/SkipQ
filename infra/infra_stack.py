from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from aws_cdk import aws_lambda as lambda_

from aws_cdk import aws_events,aws_events_targets



class InfraStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        #create a construct:lambda 
        hello_lamnda=self.create_lambda("helloLambda","./lambda","handler.lambda_handler")
        
        web_lamnda=self.create_lambda("WebhealthLambda","./lambda","web_health_publisher.health_web")
        
        #Construct a schedule from an interval and a time unit.
        lambda_schedule=aws_events.Schedule.rate(core.Duration.minutes(5))
        
        #Use the LambdaFunction target to invoke a lambda function.
        event_target=aws_events_targets.LambdaFunction(handler=web_lamnda)
        #defines an EventBridge rule which monitors an event based on an event pattern(schedule) and invoke event_targets when the pattern is matched against a triggered event
        lambda_run_rule=aws_events.Rule(self,"web_health_schedule_rule",
        description="Periodic Web Health Check",
        
        schedule=lambda_schedule,
        targets=[event_target]
        )
        
        
    
    def create_lambda(self,id,asset,handler):
        
        '''
        --Description: Create a lambda function
    
        --Parameters:
        self: this object.
        id: specific for each object
        asset: The Function method uses assets to bundle the contents of the directory and use it for the function's code.
        handler: handler is the method in your function code that processes events.
        
        --Returns:
        lambda function  
        '''
    
        return lambda_.Function(self,id,
        code=lambda_.Code.asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6)
