# Nginx Commands

## 基本命令

```bash
# 启动 nginx
nginx

# 停止 nginx (快速关闭)
nginx -s stop

# 优雅停止 nginx
nginx -s quit

# 重新加载配置
nginx -s reload

# 重新打开日志
nginx -s reopen

# 测试配置文件是否正确
nginx -t

# 查看 nginx 版本
nginx -v

# 查看完整版本信息和编译参数
nginx -V
```

## macOS 上的 Nginx

```bash
# 通过 brew services 管理
brew services start nginx
brew services stop nginx
brew services restart nginx
brew services list

# 配置文件位置 (通过 brew 安装)
# /opt/homebrew/etc/nginx/nginx.conf
```

## 常用目录

```bash
# Linux 默认配置目录
/etc/nginx/

# Linux 默认日志
/var/log/nginx/

# 默认网站根目录
/usr/share/nginx/html/
```

## 测试配置

```bash
# 检查语法和配置
nginx -t -c /path/to/nginx.conf
```
