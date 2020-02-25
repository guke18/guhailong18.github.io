#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

appid = '20200111000374664'  # 填写你的appid
secretKey = '3lAH6nA5gUgPkKHwT2LX'  # 填写你的密钥

httpClient = None
myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

with open('yourfile.tst','r',encoding='utf-8') as file:
    lines = file.readlines()



fromLang = 'auto'   #原文语种
toLang = 'zh'   #译文语种
salt = random.randint(32768, 65536)
q = lines
sign = appid + q + str(salt) + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
salt) + '&sign=' + sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    # response是HTTPResponse对象
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)
    A = (result['trans_result'])
    trans = A[0]
    print(trans['dst'])
    # 下面的代码是将翻译后的文件保存在test.txt
#    B = trans['dst']
#    with open('test.txt','a',encoding='utf-8') as file2:
#        file2.write(B)

except Exception as e:
    print (e)
finally:
    if httpClient:
        httpClient.close()