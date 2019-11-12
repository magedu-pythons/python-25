~~还没学到 `pyenv` & `jupyter` 相关内容，没有搭建。~~

搭建 `pyenv` 环境：  
1. CentOS 6 x64 虚拟机  
2. 执行 `pyenv-installer` 安装 pyenv  
3. `pyenv install 3.6.9` 编译安装 `v3.6.9`  

global & local & shell：  
1. global 设置某用户全局 python 版本，基于版本文件 `~/.pyenv/version`  
2. local 设置某目录的递归 python 版本，基于版本文件 `.python-version`  
3. shell 设置当前终端会话的 python 版本，基于环境变量 `PYENV_VERSION`  

可查看帮助：  
`pyenv help <global|local|shell>`  

部署jupyter：  
pip install jupyter  
jupyter notebook password YOURPW  
jupyter notebook --ip=0.0.0.0 --no-browser  
