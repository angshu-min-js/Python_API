import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key = ""
    locationString = inputString.replace(" ", "+")
    url = ()
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    print "response header: %s \n \n" % response
    return result
