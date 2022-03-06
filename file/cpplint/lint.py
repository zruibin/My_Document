#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# cppcheck.py
#
# Created by Ruibin.Chow on 2022/03/04.
# Copyright (c) 2022年 Ruibin.Chow All rights reserved.
# 

"""

"""

import os, os.path, shutil
import subprocess
import datetime
import codecs, sys
from cpplint import *

rootDir = "src" # 工程源码根目录
lintDir = "lint" # lint脚本目录
gitDir = ".git"

logList = []
includeSuffixs = ["c", "cc", "cpp", "h", "hpp"]
excludeDirs = [gitDir, lintDir]



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

def ignoreDirectory(path, ignoreDirs):
    ignore = False
    for ignoreDir in ignoreDirs:
        if ignoreDir in path:
            ignore = True
    return ignore


def dirWalk(DIR, excludeDirs=[]):
    """返回指定目录下所有文件的集合，exIncludeDirs的目录不包含"""
    array = []
    for root, dirs, files in os.walk(DIR):
        for file in files:
            fullFile = os.path.join(root, file)
            path = os.path.dirname(fullFile)
            # ignore = ignoreDirectory(path, excludeDirs)
            # if ignore:
            #     continue
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


def lintCMD(file):
    cmd = [
            "--filter=-whitespace/line_length,-build/include", 
            "--output=emacs", 
            "--headers="+(",".join(includeSuffixs)),
        ]
    if len(rootDir) > 0:
        cmd.append("--root=" + rootDir)
    for directory in excludeDirs:
        cmd.append("--exclude=" + directory)
    cmd.append(file)
    return cmd


class SysErr():
    def write(self, arg):
        log(arg, False)
  
# class SysOut():
#     def write(self, format_string, *args, **kwargs):
#         log(format_string, False)
#         pass

def lint(argvList, backStd=True):
    filenames = ParseArguments(argvList)
    if backStd:
        backup_err = sys.stderr
        sys.stderr = SysErr()
    try:
        # Change stderr to write with replacement characters so we don't die
        # if we try to print something containing non-ASCII characters.
        sys.stderr = codecs.StreamReader(sys.stderr, 'replace')
        get_cpplint_state().ResetErrorCounts()
        for filename in filenames:
            ProcessFile(filename, get_cpplint_state().verbose_level)
        # If --quiet is passed, suppress printing error count unless there are errors.
        if not get_cpplint_state().quiet or get_cpplint_state().error_count > 0:
            get_cpplint_state().PrintErrorCounts()

        if get_cpplint_state().output_format == 'junit':
            sys.stderr.write(get_cpplint_state().FormatJUnitXML())

    finally:
        if backStd:
            sys.stderr = backup_err
    pass



def containOCAttribute(content):
    hasOCAttribute = False
    attributeList = [
        "#import", "@protocol"
        "@interface", "@property", 
    ]
    for attribute in attributeList:
        if attribute in content:
            hasOCAttribute = True
            break
    return hasOCAttribute


def isOCHeader(filePath):
    """通过文件内容判断是否为OC头文件"""
    suffix = os.path.splitext(filePath)[-1]
    if len(suffix) == 0 or suffix != ".h":
        return False
    content = ""
    with open(filePath, "r") as fileHandle:
        content = fileHandle.read()
    if containOCAttribute(content):
        return True
    else:
        return False



def default():
    # begin = datetime.datetime.now()
    # log("更新时间：" + str(begin))
    directory = rootDir
    fileList = dirWalk(directory, excludeDirs)
    fileList = filtingFileSuffix(fileList, includeSuffixs)

    for file in fileList:
        if isOCHeader(file):
            continue
        lint(lintCMD(file))
        log(" ")

    # end = datetime.datetime.now()
    # log(('花费时间: %.3f 秒' % (end - begin).seconds))
    logRecord()
    pass

def lintFile(file):
    if isOCHeader(file):
        return
    # if ignoreDirectory(file, excludeDirs):
    #     return
    suffix = file.split(".")[-1]
    if suffix not in includeSuffixs:
        return
    lint(lintCMD(file), False)
    sys.exit(get_cpplint_state().error_count > 0)


def checkGitPreCommit():
    """检查并创建提交检查软链接"""
    hooksName = "hooks"

    # 必须是绝对路径
    absSrcDir = os.path.abspath(os.path.join(lintDir, hooksName))
    absDstDir = os.path.abspath(os.path.join(gitDir, hooksName))
    if os.path.islink(absDstDir):
        log("is exists hooks link!")
        return
    if os.path.exists(absDstDir):
        shutil.move(absDstDir, 
            os.path.abspath(os.path.join(gitDir, "hooks_bak")))

    log(absSrcDir)
    log(absDstDir)
    os.symlink(absSrcDir, absDstDir)
    pass



if __name__ == '__main__':
    if len(sys.argv) == 1:
        default()
    else:
        if sys.argv[1] == "--check":
            checkGitPreCommit()
        else:
            lintFile(sys.argv[1])
    pass












