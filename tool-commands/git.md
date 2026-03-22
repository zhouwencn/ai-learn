# Git Commands

## 基础配置

```bash
# 设置用户名和邮箱
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 查看配置
git config --list

# 设置默认分支名
git config --global init.defaultBranch main
```

## 基础操作

```bash
# 初始化仓库
git init

# 克隆仓库
git clone <url>

# 查看状态
git status

# 添加文件到暂存区
git add <file>
git add .

# 提交
git commit -m "message"

# 查看提交历史
git log

# 查看未暂存的修改
git diff

# 查看已暂存的修改
git diff --staged
```

## 分支

```bash
# 查看分支
git branch

# 创建分支
git branch <branch>

# 切换分支
git checkout <branch>
git switch <branch>

# 创建并切换
git checkout -b <branch>
git switch -c <branch>

# 删除分支
git branch -d <branch>

# 强制删除
git branch -D <branch>

# 重命名分支
git branch -m <old> <new>
```

## 远程操作

```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add origin <url>

# 推送
git push origin <branch>
git push -u origin <branch>

# 拉取
git pull origin <branch>

# 获取 (不合并)
git fetch origin

# 删除远程分支
git push origin --delete <branch>
```

## 合并与变基

```bash
# 合并分支
git merge <branch>

# 变基
git rebase <branch>

# 继续变基 (解决冲突后)
git rebase --continue

# 取消变基
git rebase --abort
```

## 暂存

```bash
# 暂存工作区
git stash

# 暂存并添加消息
git stash save "message"

# 查看暂存列表
git stash list

# 应用最近一次暂存
git stash apply

# 应用最近一次暂存并删除
git stash pop

# 清空暂存
git stash clear
```

## 其他常用

```bash
# 重置到某个提交
git reset --soft <commit>
git reset --hard <commit>

# 查看某文件的历史
git log -p <file>

# 撤销对文件的修改
git checkout -- <file>

# 取消暂存
git reset HEAD <file>

# 创建标签
git tag <tagname>

# 查看修改某行的提交
git blame <file>
```

## 忽略文件

创建 `.gitignore` 文件:

```
node_modules/
.env
*.log
.DS_Store
dist/
```
