# Homebrew Commands

## 基础命令

```bash
# 更新 brew 本身
brew update

# 升级所有已安装的包
brew upgrade

# 升级单个包
brew upgrade <package>

# 搜索包
brew search <package>

# 安装包
brew install <package>

# 卸载包
brew uninstall <package>

# 查看已安装的包
brew list

# 查看包信息
brew info <package>
```

## 清理与维护

```bash
# 清理旧版本的缓存包
brew cleanup

# 诊断问题
brew doctor

# 查看过时的包
brew outdated
```

## Cask (macOS 应用)

```bash
# 安装 GUI 应用
brew install --cask <app>

# 卸载 GUI 应用
brew uninstall --cask <app>

# 列出已安装的 cask
brew list --cask
```

## 服务管理

```bash
# 启动服务
brew services start <service>

# 停止服务
brew services stop <service>

# 查看服务状态
brew services list

# 重启服务
brew services restart <service>
```
