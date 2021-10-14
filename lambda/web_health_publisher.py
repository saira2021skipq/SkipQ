import datetime
import urllib3
import constants

'''
    We create a PoolManager to generate a request. It handles all of the details of connection pooling and thread safety.
'''
http = urllib3.PoolManager()
url_array=constants.URLS_TO_MONITER

def health_web(event,context):
  
    results=[] #array to store url monitering results
    for url in url_array:
        results.append(moniter(url))
    return results
    
    
def moniter(url):   
        try: 
            start = datetime.datetime.now()
            #With the request() method, we make a GET request to the specified URL.
            response = http.request('HEAD', url)
            server=response.headers['Server']
            end = datetime.datetime.now()
            delta = end - start #take time difference
            elapsed_seconds = round(delta.microseconds * .000001, 6) 
                
            return{
                    "url":url,
                    "Latency": elapsed_seconds,
                    "availability":"Available"
                }
            
            
        except urllib3.exceptions.HTTPError as e:
            return{
                 "url":url,
                 "error":"Error 404 : URL not found"
                 }
 