
rem 备份hexo文件
rem 并上传到git

echo "start backup..."

cd backup-tools
python main.py backup

echo "success."
pause