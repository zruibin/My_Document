#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# gitUpdate.py
#
# Created by Ruibin.Chow on 2017/05/22.
# Copyright (c) 2017年 Ruibin.Chow All rights reserved.
# 

"""

"""

import os, re
import subprocess
import datetime

logList = []

def log(string="", newline=True):
    if newline:
        logList.append(str(string) + "\n")
        print(string, end="\n")
    else:
        logList.append(str(string))
        print(string, end="")
    pass

def gitOperator(gitString, newline=True):
    log(gitString)
    output = os.popen(gitString)
    # operatorString = output.read()
    for line in output.readlines():
        log(line, newline)

def gitOperatorCMD(parameterList):
    # res = subprocess.call(parameterList)
    gitString = " ".join(parameterList)
    gitOperator(gitString)
    pass

def getBranchs():
    configPath = ".git/config"
    content = ""
    with open(configPath, "r") as fp:
        content = fp.read()
    branchs = []
    tmpList = re.findall('\[branch .*?\]', content)
    for tmp in tmpList:
        if tmp == '[core]' or tmp == '[remote "origin"]':
            continue
        branch = tmp.replace('[branch "', '').replace('"]', '')
        branchs.append(branch)
        pass
    return branchs

def fetchAndUpdate(path):
    os.chdir(path)
    branchs = getBranchs()
    log(branchs)

    gitString = "git checkout -f "
    gitOperator(gitString)

    gitString = "git fetch --all"
    gitOperator(gitString)

    for branch in branchs:
        gitOperatorCMD(["git", "checkout", branch])

        gitString = "git pull"
        gitOperator(gitString, False)

        """
        tempName = "temp"
        gitString = "git fetch origin " + branch + ":" + tempName
        gitOperator(gitString)

        gitString = "git merge " + tempName
        gitOperator(gitString)

        gitString = "git branch -d " + tempName
        gitOperator(gitString)
        """
        pass

    os.chdir("../")
    pass

def dirWalk(DIR):
    dirList = os.listdir(DIR)
    dirList = sorted(dirList)
    log("总共项目个数：" + str(len(dirList)))
    for directory in dirList:
        # print directory
        if os.path.isdir(directory):
            gitDirectory = directory + "/.git"
            if os.path.exists(gitDirectory):
                log("-" * 80)
                log(gitDirectory)
                fetchAndUpdate(directory)
    pass


if __name__ == '__main__':
    begin = datetime.datetime.now()
    log("更新时间：" + str(begin))
    dirWalk(".")
    end = datetime.datetime.now()
    log("-" * 80)
    log(('花费时间: %.3f 秒' % (end - begin).seconds))

    # print(logList)
    with open('gitUpdate.log', 'w') as fileHandle:
        for logStr in logList:
            fileHandle.write(str(logStr))

    # os.chdir("./antlr4")
    # os.system("git fetch origin master:temp")
    # output = os.popen("git fetch origin master:temp")
    # operatorString = output.read()
    # print operatorString
    pass





