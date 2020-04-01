import requests


contextId= input('[*] ContextID: ')

token = input('[*] Token: ')

#cookie = input('[*] Cookie: ')

print ("Check your cookie and type here, carefully!")

_ga = input('[*] Cookie _ga: ')

__zlcmid = input('[*] Cookie __zlcmid: ')

MoodleSession = input('[*] Cookie MoodleSession: ')

_gid = input('[*] Cookie _gid: ')

_gat = input('[*] Cookie _gat: ')

url = "http://e-learning.hcmut.edu.vn/mod/hvp/ajax.php?contextId=1010672&token=5c0156c3b9be2&action=set_finished&contentId=437&data_type=state&sub_content_id=0&score=0&maxScore=0&opened=1585754436&finished=1585755546"

print("---------------Start brute force--------------")
headers={
    "Accept":"*/*",
    "Accept-Language":"en-US,en;q=0.5",
    "Accept-Encoding":"gzip, deflate",
    "X-Requested-With":"XMLHttpRequest",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Connection":"close",
    "Cookie":"_ga={}; __zlcmid={}; MoodleSession={}; _gid={}; _gat={}".format(_ga,__zlcmid,MoodleSession,_gid,_gat)
}

i=0

while i < 20000:
    url = "http://e-learning.hcmut.edu.vn/mod/hvp/ajax.php?contextId={}&token={}&action=set_finished&contentId={}&data_type=state&sub_content_id=0&score=0&maxScore=0&opened=1585754436&finished=1585755546".format(contextId,token,i)
    res=requests.get(url, headers=headers)
    if res.text.find('true') != -1:
        print ("[*] Video bypass watching, ID=" + str(i))
    i+=1

