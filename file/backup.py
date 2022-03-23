#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# backup.py
#
# Created by ruibin.chow on 2019/08/01.
# Copyright (c) 2019年 Ruibin.Chow All rights reserved.
# 

import re, urllib.request, os.path, datetime, shutil
import codecs, glob, os, re, subprocess, sys
import html2text


HEADER_TEXT = """ 
<!--BEGIN_DATA
{
    "create_date": "%s", 
    "modify_date": "%s", 
    "is_top": "0", 
    "summary": "", 
    "tags": "", 
    "file_name": ""
}
END_DATA-->

#### <p>原文出处：<a href='%s' target='blank'>%s</a></p>
"""


def remove_js_css (content):
    """ remove the the javascript and the stylesheet and the comment content (<script>....</script> and <style>....</style> <!-- xxx -->) """
    r = re.compile(r'''<script.*?</script>''',re.I|re.M|re.S)
    s = r.sub ('',content)
    r = re.compile(r'''<style.*?</style>''',re.I|re.M|re.S)
    s = r.sub ('', s)
    r = re.compile(r'''<!--.*?-->''', re.I|re.M|re.S)
    s = r.sub('',s)
    r = re.compile(r'''<meta.*?>''', re.I|re.M|re.S)
    s = r.sub('',s)
    r = re.compile(r'''<ins.*?</ins>''', re.I|re.M|re.S)
    s = r.sub('',s)
    return s

def remove_empty_line (content):
    """remove multi space """
    r = re.compile(r'''^\s+$''', re.M|re.S)
    s = r.sub ('', content)
    r = re.compile(r'''\n+''',re.M|re.S)
    s = r.sub('\n',s)
    return s

def remove_any_tag (s):
    s = re.sub(r'''<[^>]+>''','',s)
    return s.strip()

def remove_any_tag_but_a (s):
    text = re.findall (r'''<a[^r][^>]*>(.*?)</a>''',s,re.I|re.S|re.S)
    text_b = remove_any_tag (s)
    return len(''.join(text)),len(text_b)

def remove_image (s,n=50):
    image = 'a' * n
    r = re.compile (r'''<img.*?>''',re.I|re.M|re.S)
    s = r.sub(image,s)
    return s

def remove_video (s,n=1000):
    video = 'a' * n
    r = re.compile (r'''<embed.*?>''',re.I|re.M|re.S)
    s = r.sub(video,s)
    return s

def sum_max (values):
    cur_max = values[0]
    glo_max = -999999
    left,right = 0,0
    for index,value in enumerate (values):
        cur_max += value
        if (cur_max > glo_max) :
            glo_max = cur_max
            right = index
        elif (cur_max < 0):
            cur_max = 0

    for i in range(right, -1, -1):
        glo_max -= values[i]
        if abs(glo_max < 0.00001):
            left = i
            break
    return left,right+1

def method_1 (content, k=1):
    if not content:
        return None,None,None,None
    tmp = content.split('\n')
    group_value = []
    for i in range(0,len(tmp),k):
        group = '\n'.join(tmp[i:i+k])
        group = remove_image (group)
        group = remove_video (group)
        text_a,text_b= remove_any_tag_but_a (group)
        temp = (text_b - text_a) - 8 
        group_value.append (temp)
    left,right = sum_max (group_value)
    return left,right, len('\n'.join(tmp[:left])), len ('\n'.join(tmp[:right]))

def extract (content):
    content = remove_empty_line(remove_js_css(content))
    left,right,x,y = method_1 (content)
    return '\n'.join(content.split('\n')[left:right])

# --------------------------------------------------------------------------

fileNameTimeStr = ""
artileDate = ""

def downloadIMG(content, urlPath):
    """下载图片"""
    print("下载图片")

    content = convert_character(content, '?wx_fmt=png', '')
    content = convert_character(content, '?wx_fmt=jpeg', '')
    content = convert_character(content, 'data-src=', 'src=')
    # content = convert_character(content, 'png alt></p>', 'png"></p>')
    # content = convert_character(content, '<p><img src=', '<p><img src="')

    rex = r'<img[^>]*src[=\"\']+([^\"\']*)[\"\'][^>]*>'
    lists = re.findall(rex, content)

    backupDir = './image/'
    if os.path.exists(backupDir) == False:
        os.mkdir(backupDir) 
    
    print("照片时间：" + fileNameTimeStr)
    index = 0
    for img in lists:
        ignore = img.find('?')
        imgIgnore = img
        if ignore != -1:
            imgIgnore = img[0:ignore]
            # content = convert_character(content, img, imgIgnore)
      
        fileName = ""
        
        imageFormat = [".bmp", ".jpg", ".jpeg", ".png", ".gif", 
                        ".tif", ".pcx", ".tga", ".webp", ".raw",
                        ".svg", ".psd"
                    ]
        formatName = ""
        for format in imageFormat:
            if format in imgIgnore.lower():
                formatName = format
                break

        if len(formatName) > 1:
            fileName = fileNameTimeStr + "-" + str(index) + formatName
        else:
            fileName = fileNameTimeStr + "-" + str(index) + ".png"

        index = index + 1
        fileName = backupDir + fileName
        content = convert_character(content, imgIgnore, fileName)
        path = fileName
        try:
            print('图片开始下载: ' + str(imgIgnore))
            print('图片下载位置: ' + path)
            # # print('文件下载中......')
            # urllib.urlretrieve(imgIgnore, path, callbackfunc)
            if imgIgnore.startswith("./"):
                shutil.copyfile(imgIgnore, path)
            else:
                if imgIgnore.startswith("//"):
                    imgIgnore = "https:" + imgIgnore
                if imgIgnore.startswith("/"):
                    imgIgnore =  urlPath + imgIgnore
                print('图片最终下载地址: ' + str(imgIgnore))
                imageFile = urllib.request.urlopen(imgIgnore) 
                with open(path, "wb") as code:
                    code.write(imageFile.read())
        except Exception as e:
            print('文件下载错误: ' + str(imgIgnore) + ' 原因:' + str(e))
        finally:
            print('文件下载结束: '+str(imgIgnore))

    return content

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    # print("文件下载:%.2f%%"% percent)

def convert_character(string, origin_string, replace_string):
    """用指定的字符替换文本中指定的字符"""
    string = string.replace(origin_string, replace_string)
    return string


def responseData(url):
    """请求数据"""
    print("请求数据")
    html = ''
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30 "}
        request = urllib.request.Request(url, headers = headers)
        response = urllib.request.urlopen(request)
        html = response.read()
    except urllib.request.HTTPError as e:
        print(e.code)
        print("请求数据error: " + e)
    except Exception as e:
        print(e)
    finally:
        pass
        html = html.decode("UTF-8")
    print("请求数据完成")
    return html

def writeContentToFile(fileName, content, mode='w'):
    """以特定的方式向文件写内容"""
    fp = open(fileName, mode)
    fp.write(content)
    fp.close()
    pass

def getTheFileContent(fileName):
    """获得文件的内容"""
    fp = open(fileName, 'r') 
    allText = fp.read()
    fp.close()
    return allText

def getAllFileInDirBeyoundTheDir(DIR, beyoundDir=''):
    """返回指定目录下所有文件的集合，beyoundDir的目录不包含"""
    array = []
    print(DIR+beyoundDir)
    for root, dirs, files in os.walk(DIR):
        if len(beyoundDir) != 0 and os.path.exists(DIR+beyoundDir):
            if beyoundDir not in dirs:
                continue
        for name in files:
            path = os.path.join(root,name)
            array.append(path)
    return array

def convertHtmlToMarkdown(path):
    content = getTheFileContent(path)
    content = html2text.html2text(content)
    writeContentToFile(path, content)
    pass

def convertFiles(DIR):
    array = getAllFileInDirBeyoundTheDir(DIR)
    for path in array:
        convertHtmlToMarkdown(path)
    pass

def Main(url):
    url = url.lstrip().rstrip()
    html = responseData(url)
    # html = getTheFileContent("./data.html")
    
    title = re.findall(r"<title>.*</title>", html)
    if len(title) > 0:
        title = title[0]
        title = convert_character(title, '<title>', '')
        title = convert_character(title, '</title>', '')
        print("标题: " + title)

    content = extract(html)
    content = downloadIMG(content, url)
    print("#" * 100)
    # print(content)

    print("开始转为markdown")
    content = html2text.html2text(content)

    content = convert_character(content, '# ', '## ')
    content = convert_character(content, ' ', ' ')

    header = HEADER_TEXT % (artileDate, artileDate, url, title)
    content = header + '\n' + content
    writeContentToFile('temp.md', content)
    print("转换完成！")

    pass

if __name__ == '__main__':
    artileDate = "2022-01-28 22:22"
    fileNameTimeStr = "20220128-222200"
    # artileDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M');
    # fileNameTimeStr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S");
    url = """
https://mp.weixin.qq.com/s/Q3ILLSKj2kLIcDgEoIE71g
"""
    Main(url)
    pass

"""
45.63.107.3
fF.2[tj9XQX=7U{=
42.194.251.114
"""





