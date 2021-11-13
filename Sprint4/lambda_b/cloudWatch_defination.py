import os
import boto3
import constants

class cloudWatchMetrics:
    def __init__(self):
        #constructor to create cloudwatch client
        self.client=boto3.client("cloudwatch")
        
    def create_metrics(self,metric_name,namespace,dim,value,unit):
        '''
        --Description: create metric on cloud watch.
    
        --Parameters:
        metric_name: specific name
        namespace: spefic name to contain all metrices
        dim:dimensions for each metric
        value: value to be pass for each metric
        unit:unit for value
        
        --Returns:
        create metric object  
        '''
        response = self.client.put_metric_data(
        MetricData =[
                    {
                        'MetricName':metric_name,
                        'Dimensions':dim,
                        'Unit': unit,
                        'Value': value
                        #we need deafult timestamp so no need to define timestamp
                    },
                ],
                Namespace=namespace
            )
        return response