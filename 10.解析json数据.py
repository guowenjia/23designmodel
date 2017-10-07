import json
from urllib.request import urlopen
def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)#这里的关键,load之后然后获取
    print(responseJson)
    return responseJson.get('country_code')
print(getCountry('50.78.253.58'))