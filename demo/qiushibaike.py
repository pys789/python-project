import urllib.request
import re

headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

urlstr="https://www.qiushibaike.com/text/page/{}/"
reg='<div.*?class="content">.*?<span>(.*?)</span>.*?</div>'
savefile=open("D:\\search\\qiushibaike.txt","w",encoding='utf-8')
for i in range(1,10):
    try:
        data = urllib.request.urlopen(urlstr.format(i)).read().decode("utf-8", "ignore")
        ret=re.compile(reg,re.S).findall(data)
        for j in range(0,len(ret)):
            str=ret[j].replace('<br/>', '\n')
            savefile.write(str)
            savefile.write("--------------------------------------------------------")
    except Exception as ex:
        print(ex)
savefile.close()


