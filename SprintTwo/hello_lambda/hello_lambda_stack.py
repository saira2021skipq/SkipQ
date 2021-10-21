from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

from aws_cdk import aws_iam, aws_events, aws_events_targets, core

from aws_cdk import aws_lambda as lambda_

from lambda_b import constants

import boto3


class HelloLambdaStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
      

        # The code that defines your stack goes here
        
        role=self.create_role("SAIRACW")

        hello_lamnda=self.create_lambda("helloLambda","./lambda_b","handler.lambda_handler",role)
        
        web_lamnda=self.create_lambda("WebhealthLambda","./lambda_b","web_health_publisher.health_web",role)
        
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
        
        #call to set alarm for Latency
        self.create_alram('latancy_alarm_saira','SairaHealthMonitering',constants.URL_MONITER_MATRIC_NAME_LATENCY,'Alarm when latency increase 0.3',constants.THRESHOLD_LATENCY,'Milliseconds')
         #call to set alarm for Availability
        self.create_alram('availability_alarm_saira','SairaHealthMonitering',constants.URL_MONITER_MATRIC_NAME_AVAIALABILITY,'Alarm when website down',constants.THRESHOLD_AVAILABILITY,'None')
        
        
    
    def create_alram(self,alarm_name,namespace,metric_name,discription,threshold,unit):
        '''
        --Description: Create a cloud watch alarm
    
        --Parameters:
        self: this object.
        alarm_name: name of alarm.
        namespace: Metrices namespace in which we want to set alarm.
        metric_name: name of the metric on which alarm is to be set
        Discription: Alarm Discription.
        Threshold: To triger alarm.
        Unit: unit for value
        --Returns:
        alarm  
        '''
        
        #create an sns client
        sns_client = boto3.client('sns')
        #Create topic for sns client
        topic_name= f'saira_sns_alert_web_health'
        topic = sns_client.create_topic(Name=topic_name)
        # Create email subscription
        response = sns_client.subscribe(TopicArn=topic['TopicArn'], Protocol="email", Endpoint="saira.s@skipq.org",ReturnSubscriptionArn=True)
        #cloudwatch client to set alarm on metrices
        cloudwatch=boto3.client("cloudwatch")
        #url array to pass in alarm dimensions
        url_array=constants.URLS_TO_MONITER
        #loop through each url in url array
        for url in url_array:
            #dimensions for alarm for each url
            dim=dim=[{
            "Name":"SAIRA_UPDATED",
            "Value":url
            }]
            #specific alarm name for each url
            alarmname=alarm_name +str(url)
            #builtin function to set alarm on metric
            alaram=cloudwatch.put_metric_alarm(
                    AlarmName=alarmname,
                    ComparisonOperator='LessThanThreshold',
                    EvaluationPeriods=1,
                    MetricName=metric_name,
                    Namespace=namespace,
                    #alarm for every 5 minutes
                    Period=300, 
                    Statistic='Average',
                    Threshold=threshold,
                    AlarmDescription=discription,
                    Dimensions=dim,
                    Unit=unit,
                    #set sns action on alamr
                    AlarmActions= [topic['TopicArn']]
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
        assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
        
        #set policies for cloud watch and lambda services
        managed_policies=[
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambda_FullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess")])
        return user_role
        
    
    def create_lambda(self,id,asset,handler,role):
        
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
        runtime=lambda_.Runtime.PYTHON_3_6,
        #to run lambda function for 5 minutes
        timeout = core.Duration.seconds(300),
        #set role for lambda function
        role=role)
