import boto3
import constants
def put_event_data(timestamp,message):
    client = boto3.client('dynamodb')
    table=constants.TABLE_NAME
    existing_tables = client.list_tables()["TableNames"]
    
    if table not in existing_tables:
        
        response = client.create_table(
            AttributeDefinitions=[
            {
                'AttributeName': 'Timestamp',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'sns_message',
                'AttributeType': 'S'
            },
        ],
         TableName=constants.TABLE_NAME,
         KeySchema=[
            {
                'AttributeName': 'Timestamp',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'sns_message',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
         BillingMode='PAY_PER_REQUEST'
        )
        response="Table Created"
        client.put_item(
        TableName=table,
        Item={
        'Timestamp':
            {'S':timestamp},
        'sns_message':
            {'S':message}
            }
        )
        response="Data Inserted"
    else:
        client.put_item(
        TableName=table,
        Item={
        'Timestamp':
            {'S':timestamp},
        'sns_message':
            {'S':message}
            }
        )
        response="Data Inserted"
    
    return response