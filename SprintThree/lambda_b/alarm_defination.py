import boto3
from lambda_b import constants

def create_alram(alarm_name,namespace,metric_name,discription,threshold,unit,Comparison_operator,lambda_ARN):
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
        # Create email subscription
        
             #Create topic for sns client
        topic_name= constants.ALARM_TOPIC
        topic = sns_client.create_topic(Name=topic_name)
        response = sns_client.subscribe(TopicArn=topic['TopicArn'], 
                                        Protocol=constants.SNS_LAMBDA_PROTOCOL,
                                        Endpoint=lambda_ARN,
                                        ReturnSubscriptionArn=True)
       
        #cloudwatch client to set alarm on metrices
        cloudwatch=boto3.client("cloudwatch")
        #url array to pass in alarm dimensions
        url_array=constants.URLS_TO_MONITER
        #loop through each url in url array
        for url in url_array:
            #dimensions for alarm for each url
            dim=dim=[{
            "Name":constants.METRIC_DIMENSION_NAME,
            "Value":url
            }]
            #specific alarm name for each url
            alarmname=alarm_name +str(url)
            #builtin function to set alarm on metric
            alaram=cloudwatch.put_metric_alarm(
                    AlarmName=alarmname,
                    ComparisonOperator=Comparison_operator,
                    EvaluationPeriods=1,
                    MetricName=metric_name,
                    Namespace=namespace,
                    #alarm for every 5 minutes
                    Period=constants.ALARM_PERIOD, 
                    Statistic='Average',
                    Threshold=threshold,
                    AlarmDescription=discription,
                    Dimensions=dim,
                    Unit=unit,
                    #set sns action on alarm
                    AlarmActions= [topic['TopicArn']]
                    )
