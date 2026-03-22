# Docker Commands

## 基础命令

```bash
# 查看 Docker 版本
docker --version

# 查看容器列表 (运行中的)
docker ps

# 查看所有容器 (包括停止的)
docker ps -a

# 列出镜像
docker images

# 拉取镜像
docker pull <image>

# 运行容器
docker run <image>

# 交互式运行
docker run -it <image> /bin/bash

# 后台运行
docker run -d <image>

# 指定端口映射
docker run -p 8080:80 <image>
```

## 容器管理

```bash
# 启动容器
docker start <container>

# 停止容器
docker stop <container>

# 重启容器
docker restart <container>

# 删除容器
docker rm <container>

# 强制删除运行中的容器
docker rm -f <container>

# 查看容器日志
docker logs <container>

# 实时跟踪日志
docker logs -f <container>

# 进入容器
docker exec -it <container> /bin/bash

# 查看容器信息
docker inspect <container>
```

## 镜像管理

```bash
# 构建镜像
docker build -t myapp:latest .

# 删除镜像
docker rmi <image>

# 强制删除
docker rmi -f <image>

# 清理未使用的镜像
docker image prune

# 清理所有未使用的资源
docker system prune
```

## Docker Compose

```bash
# 启动服务
docker-compose up

# 后台启动
docker-compose up -d

# 停止服务
docker-compose down

# 重新构建并启动
docker-compose up --build

# 查看日志
docker-compose logs -f

# 查看服务状态
docker-compose ps
```

## 网络

```bash
# 列出网络
docker network ls

# 创建网络
docker network create <network>

# 查看网络信息
docker network inspect <network>
```

## 清理

```bash
# 删除已停止的容器
docker container prune

# 删除无用镜像
docker image prune -a

# 删除无用卷
docker volume prune

# 删除所有未使用的 Docker 资源
docker system prune -a
```
