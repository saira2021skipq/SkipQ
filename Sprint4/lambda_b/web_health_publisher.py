import datetime
import urllib3
import constants
from cloudWatch_defination import cloudWatchMetrics
'''
  We create a PoolManager to generate a request. 
  It handles all of the details of connection pooling and thread safety.
'''


#Constants is a file that define URL array to moniter

http = urllib3.PoolManager()
def health_web(event,context):
    
    '''
    --Description: moniter url.
    --Parameters:
    event : A JSON-formatted document that contains data for a Lambda function to process.
    The event object contains information from the invoking service.
    
    Context: A context object is passed to your function by Lambda at runtime. 
    This object provides methods and properties that provide information about the invocation, function, and runtime environment.
    --Returns:
    List of dictionary/URL having information about latency and availability.  
    '''
   
    url_array=constants.URLS_TO_MONITER
    results=[] #array to store url monitering results
    
    for url in url_array:
        #run a loop for each url from url array for monitering
        
        #store result in status:<dict type>for each url
        status=moniter(url)
        #get latency from status:dictionary for each url
        latency=status["Latency"]
        #get availability from status:dictionary for each url
        availability=status["availability"]
        #create a cloudwatch_defination object to call create metrics function
        temp_obj=cloudWatchMetrics()
        
        #set up dimension for specific url
        dim=[{
            "Name":constants.METRIC_DIMENSION_NAME,
            "Value":url
            
        }]
        #call for metric creation for latency
        response_latency=temp_obj.create_metrics(constants.URL_MONITER_MATRIC_NAME_LATENCY,
                                                 constants.URL_MONITER_NAMESPACE,
                                                 dim,latency,
                                                 constants.LATENCY_UNIT)
        #call for metric creation for availability
        response_availability=temp_obj.create_metrics(constants.URL_MONITER_MATRIC_NAME_AVAIALABILITY,
                                                      constants.URL_MONITER_NAMESPACE,
                                                      dim,availability,
                                                      constants.AVAILABILITY_UNIT)
        
        #result for status of each url
        results.append(moniter(url)) 
    
    #return list  
    return results
    
    
def moniter(url):
        '''
        --Description: hit url by GET request to check status.
    
        --Parameters:
        url: url to moniter.
        
        --Returns:
        Dictionary with url as key and url status.  
        '''
    
        try: 
            #this try block is to catch HTTP exception

            start = datetime.datetime.now() # start time before hiting website
            #With the request() method, we make a GET request to the specified URL.
            response = http.request('GET', url)
            end = datetime.datetime.now() # check time after hiting website
            
            delta = end - start #take time difference
            elapsed_seconds = round(delta.microseconds * .000001, 6) 
               
            #return dictionary of url status 
            return{
                    "url":url,
                    "Latency": elapsed_seconds,
                    "availability":1
                }
            
            
        except urllib3.exceptions.HTTPError as e:
            #except HTTP exception if url not found
            
            #return dict with url status
            return{
                 "url":url,
                 "error":"Error 404 : URL not found",
                 "Latency": 0,
                 "availability":0
                 }