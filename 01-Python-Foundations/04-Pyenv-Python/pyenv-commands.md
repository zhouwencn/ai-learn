# Pyenv 与 Python 命令

## Pyenv 基础命令

### 版本管理

```bash
# 列出所有可安装的 Python 版本
pyenv install --list

# 安装指定版本的 Python
pyenv install 3.11.0
pyenv install 3.11.0 -v    # 显示详细安装过程

# 卸载指定版本
pyenv uninstall 3.11.0

# 列出已安装的 Python 版本
pyenv versions

# 查看当前激活的版本
pyenv version

# 查看所有已激活的版本 (全局+本地)
pyenv version-name
```

### 全局与本地版本

```bash
# 设置全局 Python 版本 (影响所有未指定目录)
pyenv global 3.11.0

# 设置当前目录的 Python 版本 (创建 .python-version 文件)
pyenv local 3.11.0

# 取消本地版本设置
pyenv local --unset

# 查看全局版本设置
pyenv global
```

### Shell 与插件

```bash
# 查看 pyenv 完整路径
which pyenv

# 启用 pyenv (某些 shell 需要手动加载)
eval "$(pyenv init -)"

# 仅初始化 pyenv-virtualenv 插件
eval "$(pyenv virtualenv-init -)"

# 升级 pyenv
cd $(pyenv root)/ && git pull
```

---

## Python 基础命令

### 解释器

```bash
# 进入 Python 交互式解释器
python

# 进入 Python 解释器 (明确指定版本)
python3.11
pyenv run python3.11

# 执行 Python 脚本
python script.py
python3 script.py

# 执行单行代码
python -c "print('Hello')"

# 执行模块
python -m module_name

# 显示 Python 版本
python --version
python -V
python3 --version
```

### pip 包管理

```bash
# 安装包
pip install <package>
pip install package==1.0.0       # 指定版本
pip install "package>=1.0.0"      # 最低版本
pip install -U package             # 升级到最新版本

# 安装 requirements.txt 中的包
pip install -r requirements.txt

# 批量升级
pip install --upgrade pip setuptools wheel

# 卸载包
pip uninstall <package>
pip uninstall -y <package>        # 自动确认

# 查看已安装的包
pip list
pip list --outdated               # 显示可升级的包

# 查看包信息
pip show <package>

# 搜索包
pip search <package>              # 需要 pip-search 插件

# 导出依赖
pip freeze > requirements.txt

# 使用国内镜像安装
pip install <package> -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 常用 pip 选项

```bash
# 清华大学镜像
-i https://pypi.tuna.tsinghua.edu.cn/simple

# 阿里云镜像
-i https://mirrors.aliyun.com/pypi/simple/

# 豆瓣镜像
-i https://pypi.douban.com/simple/

# 指定用户安装 (不污染全局)
pip install --user <package>

# 以编辑模式安装 (用于开发)
pip install -e .

# 忽略已安装的包 (强制重新安装)
pip install --force-reinstall <package>
```

---

## 虚拟环境 (venv)

### 创建与管理

```bash
# 创建虚拟环境
python -m venv venv

# 创建指定 Python 版本的虚拟环境
python3.11 -m venv venv

# 激活虚拟环境 (Linux/macOS)
source venv/bin/activate

# 激活虚拟环境 (Windows)
.\venv\Scripts\activate

# 退出虚拟环境
deactivate
```

### 虚拟环境常用操作

```bash
# 在虚拟环境中运行命令
venv/bin/python --version

# 查看虚拟环境中的包
venv/bin/pip list

# 导出依赖
venv/bin/pip freeze > requirements.txt
```

---

## Conda 命令 (备选)

```bash
# 创建环境
conda create --name myenv python=3.11

# 激活环境
conda activate myenv

# 退出环境
conda deactivate

# 查看环境列表
conda env list

# 删除环境
conda env remove --name myenv

# 安装包
conda install numpy

# 导出环境
conda env export > environment.yml
```

---

## pyenv-virtualenv 插件

```bash
# 创建虚拟环境
pyenv virtualenv 3.11.0 myproject

# 列出所有虚拟环境
pyenv virtualenvs

# 激活虚拟环境
pyenv activate myproject

# 退出虚拟环境
pyenv deactivate

# 删除虚拟环境
pyenv virtualenv-delete myproject
```

---

## 常用场景

### 1. 安装特定 Python 版本并创建项目

```bash
# 1. 查看可用版本
pyenv install --list | grep "3.11"

# 2. 安装
pyenv install 3.11.0

# 3. 设置项目本地版本
cd myproject
pyenv local 3.11.0

# 4. 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 5. 安装依赖
pip install -r requirements.txt
```

### 2. 切换不同项目

```bash
# 项目 A
cd project-a
pyenv local 3.10.0

# 项目 B (独立设置)
cd project-b
pyenv local 3.11.0

# 无需手动激活，pyenv 会自动切换
```

### 3. 解决 macOS 系统 Python 问题

```bash
# macOS 系统自带 Python 2.7，不要修改它
# 使用 pyenv 安装独立版本

# 1. 安装依赖 (Homebrew)
brew install pyenv pyenv-virtualenv

# 2. 添加到 shell 配置 (~/.zshrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv-virtualenv-init -)"' >> ~/.zshrc

# 3. 重启 shell
exec "$SHELL"
```

---

## 故障排除

```bash
# 检查 pyenv 是否正确安装
pyenv doctor

# 排查版本未切换问题
# 1. 检查是否正确初始化
echo $PYENV_VERSION

# 2. 检查 .python-version 文件
cat .python-version

# 3. 检查 shims 是否最新
pyenv rehash

# 4. 手动指定版本测试
PYENV_VERSION=3.11.0 python --version
```
