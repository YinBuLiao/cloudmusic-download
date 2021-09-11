import re
import os
import time
import requests
import html5lib
from bs4 import BeautifulSoup

#设置标题名称
os.system("title 网易云歌曲一键下载 By:YinBuLiao")

print("注意！VIP歌曲无法进行下载！")

url = input("请输入歌曲链接:")

#获取前半段关键词
w1 = 'id='
#获取后半段关键词
w2 = '&userid'

#提取关键字
pat = re.compile(w1 + '(.*?)' + w2, re.S)
#输出列表
songid = pat.findall(url)
#提取数字
str_songid = re.sub("\D","",str(songid))

#模拟chrome进行请求
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
}

#下载歌曲
def songdownload():
    url = r'https://music.163.com/song/media/outer/url?id='
    send_url = url + str_songid + '.mp3'
    result = requests.get(send_url,headers=headers)
    with open(str_songid + '.mp3', 'wb') as f:
        f.write(result.content)
    print('下载完成，等待重命名')

#重命名歌曲
def autorename():
    res = requests.get(url)
    res.encoding = 'uft-8'
    soup = BeautifulSoup(res.text,"html5lib")
    a = soup.find_all('em',class_="f-ff2")
    for i in a:
        srcFile = str_songid + '.mp3'
        dstFile = i.text.strip() + '.mp3'
        try:
            os.rename(srcFile, dstFile)
        except Exception as e:
            print('歌曲重命名失败')
        else:
            print('歌曲重命名成功')
    ##print(a)

if __name__ == '__main__':
    songdownload()
    time.sleep(1)
    autorename()
    os.system('pause')
