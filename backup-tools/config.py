# -*- coding: utf-8 -*-


"""
hexo 备份、更新参数

Args:
    fromPath: 源目录
    toPath: 目标目录
    ignoreDirs: fromPath 下需要跳过的目录或者子目录
    filesAndDirs: fromPath 下需要备份的文件或者目录

"""


# 备份参数
backupConfig = {
    'fromPath': '../../',
    'toPath': '../',
    'overwriteFile': True, # 遇到同名文件是否覆盖
    'ignoreDirs': [ # 需要忽略的目录，提前过滤
        '.git',
        'node_modules',
        'public',

        'hexo-git-backup',
        'history-files',
    ],
    'filesAndDirs': [ # 需要拷贝的文件夹或者文件，相对 fromPath 根目录，只有列表中的内容才会被拷贝
        'custom.yml',
        'source',
        'scaffolds',
        'themes/apollo/_config.yml',
        'themes/apollo/source/logo.png',
    ]
}


# 更新参数
updateConfig = {
    'fromPath': '../',
    'toPath': '../../',
    'overwriteFile': False, # 此时不覆盖
    'historyPath': 'history-files', # 不覆盖的情况下存储到 toPath 下面的 备份历史文件 目录
    'ignoreDirs': [
        '.git',
        'backup-tools',
    ],
    'filesAndDirs': [
        'custom.yml',
        'source',
        'scaffolds',
        'themes',
    ],
}


class Config(object):
    """用于封装配置文件，方便访问"""
    def __init__(self, config={}):
        for key, value in config.iteritems():
            if isinstance(value, dict):
                self.__dict__[key] = Config(value)
            else:
                self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__.get(key, None)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)



