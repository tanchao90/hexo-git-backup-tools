
rem 从git更新文件
rem 还原到本地hexo目录

echo "update backup..."

cd backup-tools
git pull origin master

echo "wait 3s"
timeout /t 3

python main.py update

echo "success."
pause