import datetime
import urllib3
import constants

'''
  We create a PoolManager to generate a request. 
  It handles all of the details of connection pooling and thread safety.
'''
http = urllib3.PoolManager()

#Constants is a file that define URL array to moniter
url_array=constants.URLS_TO_MONITER

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
  
    results=[] #array to store url monitering results
    
    for url in url_array:
        #run a loop for each url from url array for monitering
        
        #append monter results in list
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
                    "availability":"Available"
                }
            
            
        except urllib3.exceptions.HTTPError as e:
            #except HTTP exception if url not found
            
            #return dict with url status
            return{
                 "url":url,
                 "error":"Error 404 : URL not found"
                 }
 