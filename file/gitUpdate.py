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

import os, re, json, sys
import subprocess
import datetime

logList = []
projects = []

def logRecord():
    with open('gitUpdate.log', 'w') as fileHandle:
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

def gitOperator(gitString, newline=True):
    log(gitString)
    output = os.popen(gitString)
    for line in output.readlines():
        log(line, newline)

def gitOperatorCMD(parameterList, newline=True):
    # res = subprocess.call(parameterList)
    gitString = " ".join(parameterList)
    gitOperator(gitString, newline)
    pass

def getGitUrl():
    configPath = ".git/config"
    content = ""
    with open(configPath, "r") as fp:
        content = fp.read()
    urls = re.findall('url = (.+)', content)
    if len(urls) > 0:
        return urls[0]
    return None

def getBranchs():
    configPath = ".git/config"
    content = ""
    with open(configPath, "r") as fp:
        content = fp.read()
    branchs = []
    tmpList = re.findall(r'\[branch .*?\]', content)
    for tmp in tmpList:
        if tmp == '[core]' or tmp == '[remote "origin"]':
            continue
        branch = tmp.replace('[branch "', '').replace('"]', '')
        branchs.append(branch)
        pass
    return branchs

def convert_http_to_ssh(url):
    if url.startswith('http'):
        parts = url.split('/')
        domain = parts[2]
        path = '/'.join(parts[3:])
        ssh_url = f'git@{domain}:{path}'
        return ssh_url
    return url

def getRemote():
    configPath = ".git/config"
    content = ""
    with open(configPath, "r") as fp:
        content = fp.read()
    pattern = r'\[remote "([^"]+)"\]\s+url = (\S+)'
    matches = re.findall(pattern, content)
    urls = {remote_name: url for remote_name, url in matches}
    url = urls['origin']
    if 'github' in url:
        return convert_http_to_ssh(url)
    else:
        return url

def fetchAndUpdate(path):
    os.chdir(path)
    branchs = getBranchs()
    log(branchs)

    gitString = "git checkout -f "
    gitOperator(gitString)

    gitString = "git fetch --all"
    gitOperator(gitString)

    url = getRemote()
    log(url)

    for branch in branchs:
        gitOperatorCMD(["git", "checkout", branch])

        if url.startswith('http'):
            gitString = "git pull"
            gitOperator(gitString, False)
        else:
            gitOperatorCMD(["git", "pull", url, branch], False)

        """
        git pull git@github.com:yourusername/your-repo.git main

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

def dirWalk(DIR, actionFunction):
    dirList = os.listdir(DIR)
    dirList = sorted(dirList)
    count = 0
    for directory in dirList:
        if os.path.isdir(directory):
            gitDirectory = directory + "/.git"
            if os.path.exists(gitDirectory):
                count = count + 1
                log("-" * 80)
                log(gitDirectory)
                actionFunction(directory)
    return count

def updateProject():
    begin = datetime.datetime.now()
    log("更新时间：" + str(begin))
    count = dirWalk(".", fetchAndUpdate)
    end = datetime.datetime.now()
    log("-" * 80)
    log("总共项目个数：" + str(count))
    log(('花费时间: %.3f 秒' % (end - begin).seconds))

    logRecord()
    pass

# ------------------------------------------------------------------------------

def backupForJson(directory):
    os.chdir(directory)
    branchs = getBranchs()
    projectName = str(directory)
    log("Project Name:" + projectName)
    log("Project Branchs:" + ",".join(branchs))
    url = getGitUrl()
    log("Project Url: " + str(url))

    project = {
        "name":projectName,
        "url":str(url),
        "branchs":branchs
    }
    projects.append(project)
    os.chdir("../")
    pass

def backupProject():
    dirWalk(".", backupForJson)
    with open('projects.json', 'w', encoding='utf-8') as fileHandle:
        jsonStr = json.dumps(projects, indent=4)
        fileHandle.write(str(jsonStr))
    pass

def cloneProject():
    with open('projects.json', 'r', encoding='utf-8') as fileHandle:
        jsonStr = fileHandle.read()
        projects = json.loads(jsonStr)
        # log(projects)
    begin = datetime.datetime.now()
    for project in projects:
        log("-" * 80)
        projectName = project["name"]
        projectUrl = project["url"]
        branchs = project["branchs"]
        log("project name: " + projectName)
        log("project url: " + projectUrl)
        log("project branchs: " + ",".join(branchs))
        gitOperatorCMD(["git", "clone", projectUrl, projectName])
        os.chdir(projectName)
        for branch in branchs:
            gitOperatorCMD(["git", "checkout", "-b", branch, "--track", "origin/"+str(branch)])
        os.chdir("../")
    log("-" * 80)
    end = datetime.datetime.now()
    log(('clone花费时间: %.3f 秒' % (end - begin).seconds))
    logRecord()
    pass

def help():
    helpStr = """
Command:
    update  更新仓库
    clone   根据projects.json文件来克隆仓库
    backup  将现有的仓库信息备份到projects.json
    help    说明
Default:
    update
    """
    print(helpStr)
    pass


# ------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        updateProject()
    if len(sys.argv) > 1:
        if sys.argv[1] == "clone":
            cloneProject()
        elif sys.argv[1] == "backup":
            backupProject()
        elif sys.argv[1] == "help" or sys.argv[1] == "-h":
            help()
        elif sys.argv[1] == "update":
            updateProject()
    pass





