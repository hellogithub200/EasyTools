# EasyTools
封装的工具集合

EasyLog是对Python logging模块的简单封装，保留了logging模块最基本的功能

**使用方法：将easy_log.py, easy_log.yaml放于项目中使用即可**

1. 通过修改配置文件，来定制日志的输出文件
2. 配置文件中有两种配置好的模板：基于时间切分的Handler，基于日志文件大小切分的Handler。具体的参数可以参考Python官方的logging模块文档。

*注：Yaml安装：pip install pyyaml*


EasyEmail简单封装了用python emai模块发送邮件的功能：适用于发件人是Gmail的账户。使用起来十分简单

