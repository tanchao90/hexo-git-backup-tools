# README #

Back-up the source files of my blog.

[coneycode/hexo-git-backup](https://github.com/coneycode/hexo-git-backup) is more popular, you also can try it.


## env
- git
- Python 2.7: Tested.
- Python 3.x: Not tested.


## clone repo to local
- Go to the root directory of hexo blog.
- `git clone https://github.com/tanchao90/hexo-git-backup.git`


## modify remote `origin` to your repo
- `git remote set-url origin https://github.com/username/repo.git`


## backup `source files` to Git
- `cd hexo-git-backup`
- `config.py`: check and modify.
- `backup-win.bat` or `sh backup-mac.sh`: copy `source files` to git repo
- git ops: add, commit, and push files to Github or Bitbucket.


## update `source files` from Git
- `cd hexo-git-backup`
- `config.py`: check and modify.
- `update-win.bat` or `sh update-mac.sh`: pull `source files` and copy it to the root directory of hexo blog.
- `history-files` is used to store the history files that has been overwrited by the same file in git repo.


## Reference
- [os — Miscellaneous operating system interfaces](https://docs.python.org/2/library/os.html?highlight=os#module-os)
- [os.path — Common pathname manipulations](https://docs.python.org/2/library/os.path.html)
- [shutil — High-level file operations](https://docs.python.org/2.7/library/shutil.html?highlight=shutil)
- [python copy folder structure under another directory](http://stackoverflow.com/questions/40828450/python-copy-folder-structure-under-another-directory)
- [Changing a remote's URL](https://help.github.com/articles/changing-a-remote-s-url/)
