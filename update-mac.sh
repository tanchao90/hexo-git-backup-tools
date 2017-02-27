
# 从git更新文件
# 还原到本地hexo目录

echo "update backup..."

cd backup-tools
git pull origin master

echo "wait 3s"
sleep 3s

python main.py update

echo "success."
