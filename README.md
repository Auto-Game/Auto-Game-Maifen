# 出发吧，麦芬！

## 简介
### 亮点功能

- [ ] 待添加

## 更新日志
Todo

## 使用说明
### 基本说明
Todo
### 常见问题
Todo
### 环境要求
- Python 3.7+
#### 开源库
| 库名 | 描述 | 应用场景 |
| --- | --- | --- |
| [aricv](https://github.com/NetEaseGame/aircv) | 图片处理功能库 | 用于图片识别 |

### 开发环境部署/安装
#### 创建并激活Conda环境
```shell
conda create --name wgjx python=3.7 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda activate wgjx
```

#### 配置Conda和Pip使用清华大学镜像源
```shell
conda config --add channels https://pypi.tuna.tsinghua.edu.cn/simple
conda config --set show_channel_urls yes
```

#### 使用Pip安装Python库
```shell
pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install aircv -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paddlepaddle==2.3.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paddleocr==2.6.0.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### Docker 方式部署
Todo
