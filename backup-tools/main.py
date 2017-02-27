# -*- coding: utf-8 -*-

import sys

import config
import file_utils


def backup():
	file_utils.copyFiles(config.Config(config.backupConfig))


def update():
	file_utils.copyFiles(config.Config(config.updateConfig))


cmds = {
	'backup': backup,
	'update': update
}

if __name__ == '__main__':
	print 'sys.argv', sys.argv

	cmdName = sys.argv[1]
	func = cmds.get(cmdName, None)
	if func:
		func()
	else:
		print('Argv(%s) is invalid.'%(cmdName,))




