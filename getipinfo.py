import io
import sys
import json
#import urllib
from urllib import request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

ip="218.4.255.255"
url="http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip="+ip
response = request.urlopen(url)
contents = response.read()
#text = contents.decode('utf8')
text = contents.decode('unicode-escape')
data=json.loads(text)
#print(data)

print(ip + " info {")
for key in data:
    print("  " + key , " => ", data[key] )
print("}")
