from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

from aws_cdk import aws_iam, aws_events, aws_events_targets, core, aws_sns

from aws_cdk import aws_lambda as lambda_

from lambda_b import constants, alarm_defination

import boto3


class HelloLambdaStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        
        
        role=self.create_role(constants.ROLE_NAME)

        hello_lambda=self.create_lambda(constants.HELLO_LAMBDA_ID,"handler.lambda_handler",role)
        
        web_lambda=self.create_lambda(constants.WEB_HEALTH_LAMBDA_ID,"web_health_publisher.health_web",role)
        self.scedual_lambda(constants.SCHEDULING_EVENT_NAME,web_lambda,constants.SCHEDULING_DURATION,constants.SCHEDULING_EVENT_DESCRIPTION)
        
        db_lambda=self.create_lambda(constants.SNS_NOTIFICATION_LAMBDA_ID,"lambda_database.lambda_database_function",role)
        
        #call to set alarm for Latency
        alarm_defination.create_alram(constants.LAMBDA_LATENCY_ALARM,
                         constants.URL_MONITER_NAMESPACE,
                         constants.URL_MONITER_MATRIC_NAME_LATENCY,
                         constants.LATENCY_ALARM_DESCRIPTION,
                         constants.THRESHOLD_LATENCY,
                         constants.LATENCY_UNIT,
                         constants.LATENCY_COMPARISON_OP,
                         constants.DB_FUNCTION_ARN
                        )
         #call to set alarm for Availability
        alarm_defination.create_alram(constants.LAMBDA_AVAILABILITY_ALARM,
                         constants.URL_MONITER_NAMESPACE,
                         constants.URL_MONITER_MATRIC_NAME_AVAIALABILITY,
                         constants.AVAILABILITY_ALARM_DESCRIPTION,
                         constants.THRESHOLD_AVAILABILITY,
                         constants.AVAILABILITY_UNIT,
                         constants.AVAILABILITY_COMPARISON_OP,
                         constants.DB_FUNCTION_ARN)
    
    
    def scedual_lambda(self,event_name,lambda_obj,duration,desc):
        #Construct a schedule from an interval and a time unit.
        lambda_schedule=aws_events.Schedule.rate(core.Duration.minutes(duration))
        
        #Use the LambdaFunction target to invoke a lambda function.
        event_target=aws_events_targets.LambdaFunction(handler=lambda_obj)
        #defines an EventBridge rule which monitors an event based on an event pattern(schedule) and invoke event_targets when the pattern is matched against a triggered event
        lambda_run_rule=aws_events.Rule(self,event_name,
        description=desc,
        
        schedule=lambda_schedule,
        targets=[event_target]
        )
        
    def create_role(self,role_name):
        '''
        --Description: Create a user role
    
        --Parameters:
        self: this object.
        role_name: name for role
        --Returns:iam user role
        '''
        
        #set name of role
        user_role=aws_iam.Role(self,role_name,
        assumed_by=aws_iam.CompositePrincipal(
            aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            aws_iam.ServicePrincipal("sns.amazonaws.com")
            ),
        
        
        #set policies for cloud watch and lambda services
        managed_policies=[
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambda_FullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSNSFullAccess")
            
            ])
        return user_role
        
    
    def create_lambda(self,id,handler,role):
        
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
        code=lambda_.Code.asset(constants.LAMBDA_ASSETS_DICT),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6,
        #to run lambda function for 5 minutes
        timeout = core.Duration.seconds(300),
        #set role for lambda function
        role=role)
