import urllib2

#url = "http://jkbv2-api.jkb.com/widget/dashboardinfo/list"
# url = "http://www.baidu.com"
url = "http://400.haodf.com"#/index/search?diseasename=&province=&facultyname=&hosfaculty=&hospitalname=&nowpage="
send_headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Connection':'keep-alive'
}
# response = urllib2.urlopen(url)
# print response.read()
request = urllib2.Request(url,headers=send_headers)
print request
response = urllib2.urlopen(request)
print response.read()
exit()
request = urllib2.Request(url)
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print response.read()

