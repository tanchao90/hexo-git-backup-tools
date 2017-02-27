# -*- coding: utf-8 -*-

from datetime import datetime
import os
import shutil


def _createDir(fromPath, toPath, currPath):
    """计算目标目录，并创建对应的目录"""
    destPath = os.path.join(toPath, currPath[len(fromPath)+1:]) # +1 to skip first directory separator

     # create new folder if the new folder destPath does not exist
    if not os.path.isdir(destPath): # Return True if path is an existing directory
        os.mkdir(destPath)

    # if os.listdir(destPath) == []: # delete empty directory
    #    os.rmdir(destPath)

    return destPath


def _backupFile(config, dest, destHistoryPath, fileName):
    """备份旧文件，如果不需要备份，则直接返回"""
    if config.overwriteFile:
        return
    if not os.path.isfile(dest):
        return

    destHistory = os.path.join(destHistoryPath, fileName)

    filenameSplit = os.path.splitext(destHistory) # filename and extensionname (extension in [1])
    filenameZero, fileExt = filenameSplit
    newDestHistory = '%s%s%s' % (filenameZero, config.datetimeStr, fileExt)
    shutil.copy(dest, newDestHistory)


def _doCopyFiles(config, srcPath, fileNames):
    """
    Args:
    Returns:
    """
    destPath = _createDir(config.fromPath, config.toPath, srcPath)
    if not config.overwriteFile:
        destHistoryPath = _createDir(config.fromPath, config.historyPath, srcPath)
    else:
        destHistoryPath = None

    for fn in fileNames:
        src = os.path.join(srcPath, fn)
        dest = os.path.join(destPath, fn)
        needCopy = False
        for each in config.filesAndDirs:
            if src.startswith(each):
                needCopy = True
                break
        if not needCopy:
            continue

        _backupFile(config, dest, destHistoryPath, fn)

        shutil.copy(src, dest)


def _preprocessConfig(config):
    """预处理配置文件"""
    # format path
    # D:\my_project\test -> D:\my_project\test
    # D:\my_project\test\ -> D:\my_project\test
    # test -> D:\my_project\test
    config.fromPath = os.path.abspath(config.fromPath)
    config.toPath = os.path.abspath(config.toPath)

    # build full path
    for index, path in enumerate(config.filesAndDirs):
        config.filesAndDirs[index] = os.path.abspath(os.path.join(config.fromPath, path))
    # print 'filesAndDirs', config.filesAndDirs

    if not config.overwriteFile:
        config.historyPath = os.path.abspath(os.path.join(config.toPath, config.historyPath))

    date = datetime.now()
    dateFmt = '-%Y%m%d_%H%M%S'
    config.datetimeStr = date.strftime(dateFmt)


def copyFiles(config):
    """
    Args:
        config: 拷贝参数，参考 config.py
    Returns:
    """
    _preprocessConfig(config)

    # Iterate over existing folders
    for dirPath, dirNames, fileNames in os.walk(config.fromPath):
        # dirPath current directory
        # dirNames sub directory's name
        # fileNames file's name in current directory
        # print dirPath, dirNames, fileNames

        # filter directory
        ignoreFlag = False
        for eachDir in config.ignoreDirs:
            if dirPath.find(eachDir) >= 0:
                ignoreFlag = True
                break
        if ignoreFlag:
            continue

        _doCopyFiles(config, dirPath, fileNames)







