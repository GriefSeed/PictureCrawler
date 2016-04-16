#coding:utf-8
'''
Created on 2016.4.16
@author: M

用于爬取http://www.umei.cc上的美女写真
'''
import urllib.request,re
from bs4 import BeautifulSoup
import time
def allPageLink():
    pictureSum = 0      #图片总数
    filePath = "e:\\ot\\" #存储文件的路径
    linkStore = [] #用于存储页码链接的list，不需要填写
    mainPageLine = "http://www.umei.cc/p/gaoqing/rihan/" #这个是页面的主链接，加上子链接，然后遍历下一页
    
    nextPageRegex = '\d+.\d+\.htm' #这个+mainPageLine构成一个完整的链接，但这是正则表达式。
    everyPictureRegex = 'http://i7.umei.cc//img2012/2015/06/03YS/022YS638/\d+\.jpg' #这里是每一张图片的link，因为都不同，所以要填正则表达式
    firstLine = 'http://www.umei.cc/p/gaoqing/rihan/20150712182032.htm'#第一个页面
    
    linkStore.append(firstLine)
    while linkStore != [] :
        
        print(linkStore[:])
        
        html = urllib.request.urlopen( linkStore[-1], timeout=30 )
        
        #提取picture
        picUrl = re.findall(everyPictureRegex, str(html.read() ) )
        picUrl = set(picUrl)
        
        for url in picUrl :  
            print( url )
            time.sleep(2)
            sName = "{0}.jpg".format(pictureSum)#自动填充成六位的文件名  
            pictureSum += 1
            print('正在下载网页，并将其存储')   
            urllib.request.urlretrieve(url , filePath+"{0}".format(sName ))  
        #提取picture
        
        html = urllib.request.urlopen( linkStore.pop() )
        
        soup = BeautifulSoup(html, from_encoding='GBK')#这里加入beautiful进行div的搜索
        targetdiv = soup.find_all('a', text='下一页' )#这里偷懒，模拟真实用户，直接点下一页，所以就不需要存储链接啦
        print(targetdiv)
        nextPageUrl = re.findall(nextPageRegex, str(targetdiv)  )#获取下一页的链接
        print(nextPageUrl)
        linkStore.append(mainPageLine + nextPageUrl[0] )
     
allPageLink()
