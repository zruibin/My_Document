#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# cppcheck.py
#
# Created by Ruibin.Chow on 2022/03/04.
# Copyright (c) 2022年 Ruibin.Chow All rights reserved.
# 

"""
$cpplint --filter=$filters --headers=$headers --exclude=no $file
"""

import os, os.path
import subprocess
import datetime

logList = []


def logRecord():
    with open('cpplint.log', 'w') as fileHandle:
        for logStr in logList:
            fileHandle.write(str(logStr))
    pass

def log(string="", newline=True):
    if newline:
        logList.append(str(string) + "\n")
        print(string, end="\n")
    else:
        logList.append(str(string))
        print(string, end="")
    pass

def operator(string, newline=True):
    log(string)
    output = os.popen(string)
    for line in output.readlines():
        log(line, newline)

def operatorCMD(parameterList):
    string = " ".join(parameterList)
    operator(string, False)
    pass



def dirWalk(DIR, exIncludeDirs=[]):
    """返回指定目录下所有文件的集合，exIncludeDirs的目录不包含"""
    array = []
    for root, dirs, files in os.walk(DIR):
        for file in files:
            fullFile = os.path.join(root, file)
            path = os.path.dirname(fullFile)

            isPass = False
            for exIncludeDir in exIncludeDirs:
                if exIncludeDir in path:
                    isPass = True

            if not isPass:
                # log(path)
                # log(file)
                # log(fullFile)
                array.append(fullFile)
    return array

def filtingFileSuffix(fileList, suffixList=[]):
    if len(suffixList) == 0:
        return fileList
    array = []
    for file in fileList:
        suffix = os.path.splitext(file)[-1]
        if len(suffix) == 0:
            continue
        suffix = suffix.split(".")[-1]
        if suffix in suffixList:
            array.append(file)
    return array

def main():
    begin = datetime.datetime.now()
    log("更新时间：" + str(begin))

    fileList = dirWalk('./', [".git"]) # , "a/bb", "no"
    includeSuffixs = ["c", "cc", "cpp", "h", "hpp"]
    fileList = filtingFileSuffix(fileList, includeSuffixs)

    for file in fileList:
        cmd = ["python3", "cpplint.py", "--filter=-whitespace/line_length,-build/include --output=emacs", file]
        operatorCMD(cmd)
        log(" ")

    end = datetime.datetime.now()
    log(('花费时间: %.3f 秒' % (end - begin).seconds))

    logRecord()
    pass


if __name__ == '__main__':
    main()
    pass












