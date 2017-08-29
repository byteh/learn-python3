#!/usr/bin/python
#coding:utf-8

def lagou(p):
    import requests #if No module named requests  need 'sudo pip install requests
    import numpy as np
    import pandas as pd
    import json
    import time
    from bs4 import BeautifulSoup
    import jieba as jb
    import jieba.analyse
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Connection':'close',
    'Referer':'https://www.jd.com/'
    }
    cookie={'TrackID':'1_VWwvLYiy1FUr7wSr6HHmHhadG8d1-Qv-TVaw8JwcFG4EksqyLyx1SO7O06_Y_XUCyQMksp3RVb2ezA',
    '__jda':'122270672.1507607632.1423495705.1479785414.1479794553.92',
    '__jdb':'122270672.1.1507607632|92.1479794553',
    '__jdc':'122270672',
    '__jdu':'1507607632',
    '__jdv':'122270672|direct|-|none|-|1478747025001',
    'areaId':'1',
    'cn':'0',
    'ipLoc-djd':'1-72-2799-0',
    'ipLocation':'%u5317%u4EAC',
    'mx':'0_X',
    'rkv':'V0800',
    'user-key':'216123d5-4ed3-47b0-9289-12345',
    'xtest':'4657.553.d9798cdf31c02d86b8b81cc119d94836.b7a782741f667201b54880c925faec4b'}
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    positionName=[]
    workYear=[]
    education=[]
    district=[]
    jobNature=[]
    salary=[]
    city=[]
    businessZones=[]
    companyLabelList=[]
    companySize=[]
    financeStage=[]
    industryField=[]
    secondType=[]
    positionId=[]
    for x in range(1,31):
        para = {'first': 'true','pn': x, 'kd': p}
        r=requests.get(url=url,headers=headers,cookies=cookie,params=para)
        html=r.content
        print r,html
        break
        html = html.decode()
        html_json=json.loads(html)
        content=html_json.get('content')
        positionResult=content.get('positionResult')
        result=positionResult.get('result')
        for i in result:
            positionName.append(i.get('positionName'))
            workYear.append(i.get('workYear'))
            education.append(i.get('education'))
            district.append(i.get('district'))
            jobNature.append(i.get('jobNature'))
            salary.append(i.get('salary'))
            city.append(i.get('city'))
            businessZones.append(i.get('businessZones'))
            companyLabelList.append(i.get('companyLabelList'))
            companySize.append(i.get('companySize'))
            financeStage.append(i.get('financeStage'))
            industryField.append(i.get('industryField'))
            secondType.append(i.get('secondType'))
            positionId.append(i.get('positionId'))
    exit()
    url1='https://www.lagou.com/jobs/'
    url2='.html'
    job_detail=[]
    for d in positionId:
        d=str(d)
        url3=(url1 + d + url2)
        r=requests.get(url=url3,headers=headers,cookies=cookie)
        detail=r.content
        lagou_detail=BeautifulSoup(detail)
        gwzz=lagou_detail.find_all('dd',attrs={'class':'job_bt'})   
        for j in gwzz:
            gwzz_text=j.get_text()
            job_detail.append(gwzz_text)
    date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    columns = ['date','positionName', 'workYear','education','jobNature','businessZones','salary','city','companyLabelList','companySize','financeStage','industryField','district','secondType','positionId','job_detail']
    table=pd.DataFrame({'date':date,
                        'positionName':positionName,
                        'workYear':workYear,
                        'education':education,
                        'jobNature':jobNature,
                        'businessZones':businessZones,
                        'salary':salary,
                        'city':city,
                        'companyLabelList':companyLabelList,
                        'companySize':companySize,
                        'financeStage':financeStage,
                        'industryField':industryField,
                        'district':district,
                        'secondType':secondType,
                        'positionId':positionId,
                        'job_detail':job_detail},
                        columns=columns)
    table.to_csv('lagou_' + p + date + '.csv')
 
lagou("数据分析")
