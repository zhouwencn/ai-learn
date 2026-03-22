# Shell Commands

## 文件与目录

```bash
# 列出文件
ls -la

# 进入目录
cd <dir>

# 当前目录
pwd

# 创建目录
mkdir <dir>

# 创建多级目录
mkdir -p path/to/dir

# 删除空目录
rmdir <dir>

# 删除文件
rm <file>

# 强制删除
rm -f <file>

# 递归删除目录
rm -rf <dir>

# 复制文件
cp source dest

# 复制目录
cp -r source dest

# 移动/重命名
mv source dest

# 查看文件内容
cat <file>

# 分页查看文件
less <file>

# 查看文件前几行
head -n 20 <file>

# 查看文件末尾
tail -n 20 <file>

# 跟踪日志 (实时)
tail -f <file>
```

## 搜索

```bash
# 查找文件
find . -name "*.txt"
find . -type d -name "node_modules"

# 搜索文件内容
grep "pattern" <file>
grep -r "pattern" <dir>

# 搜索并高亮显示
grep -rn "pattern" .

# 忽略大小写搜索
grep -i "pattern" <file>
```

## 权限

```bash
# 修改权限
chmod 755 <file>
chmod +x <script.sh>

# 修改所有者
chown user:group <file>

# 递归修改目录
chown -R user:group <dir>
```

## 系统

```bash
# 查看进程
ps aux

# 实时查看进程
top

# 终止进程
kill <pid>
kill -9 <pid>

# 后台运行
nohup <command> &

# 查看端口占用
lsof -i :8080
netstat -tlnp | grep 8080

# 查看磁盘使用
df -h

# 查看内存使用
free -h

# 查看用户
whoami
```

## 网络

```bash
# ping 测试
ping <host>

# 查看 IP 地址
ifconfig
ip addr
curl ifconfig.me

# 下载文件
curl -O <url>
wget <url>

# SSH 连接
ssh user@host
scp file user@host:/path
```

## 其他

```bash
# 管道 (将前一个命令的输出传给后一个)
cat file | grep pattern

# 重定向
command > output.txt
command 2>&1

# 别名
alias ll='ls -la'

# 环境变量
export PATH=$PATH:/new/path
echo $HOME
```
