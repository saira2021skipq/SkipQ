ROLE_NAME="SAIRACW"
#LAMBDA IDS
HELLO_LAMBDA_ID="helloLambda"
WEB_HEALTH_LAMBDA_ID="WebhealthLambda"
SNS_NOTIFICATION_LAMBDA_ID="DbLambda"
#LAMBDA ASSET
LAMBDA_ASSETS_DICT="./lambda_b"
#ALARM NAMES
LAMBDA_LATENCY_ALARM='latancy_alarm_saira_lambda'
LAMBDA_AVAILABILITY_ALARM='availability_alarm_saira_lambda'
#ALARM DESCRIPTION
AVAILABILITY_ALARM_DESCRIPTION='Alarm when website down'
SCHEDULING_EVENT_DESCRIPTION="Periodic Web Health Check"
DB_FUNCTION_ARN= "arn:aws:lambda:us-east-2:315997497220:function:SAIRALambdaStack-DbLambdaE33031A4-PKky1KDMoldW"
LATENCY_ALARM_DESCRIPTION='Alarm when latency increase 0.3'
ALARM_TOPIC=f'saira_sns_lambda_alert_web_health'
SNS_LAMBDA_PROTOCOL="lambda"
ALARM_PERIOD=600

URLS_TO_MONITER=["https://www.skipq.org/","https://www.amazon.com/","https://www.youtube.com/","https://www.wikipedia.org/"]
#SCEDULING
SCHEDULING_DURATION=5
SCHEDULING_EVENT_NAME="web_health_schedule_rule"
SCHEDULING_RULE_NAME="web_health_schedule_rule"

URL_MONITER_NAMESPACE="SairaHealthMonitering"
LATENCY_COMPARISON_OP="GreaterThanThreshold"
AVAILABILITY_COMPARISON_OP='LessThanThreshold'
URL_MONITER_MATRIC_NAME_AVAIALABILITY="is_url_down"
URL_MONITER_MATRIC_NAME_LATENCY="url_latency_in_seconds"
THRESHOLD_LATENCY=0.3
THRESHOLD_AVAILABILITY=1
#UNIT FOR LATENCY METRIC
LATENCY_UNIT='Milliseconds'
#UNIT FOR AVAILABILITY METRIC
AVAILABILITY_UNIT='None'
#MATRIC DIMENSIONS
METRIC_DIMENSION_NAME="SAIRA_UPDATED"
TABLE_NAME="Saira_web_health_alarm_table"