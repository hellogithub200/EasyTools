# EasyTools：简单封装，简单使用
封装的工具集合

## 1. EasyLog是对Python logging模块的简单封装，保留了logging模块最基本的功能

**使用方法：将easy_log.py, easy_log.yaml放于项目中，修改easy_log.yaml配置，添加自己需要的Logger和Handler即可。**

1. 通过修改配置文件，来定制日志的输出位置
2. 配置文件中有三种配置好的模板：基于时间切分的Handler，基于日志文件大小切分的Handler, 基于邮箱配置的Handler。
具体的参数可以参考Python官方的logging模块文档。

*注：Yaml安装：pip install pyyaml*

## 2. EasyEmail是对python email模块的简单封装，实现发送邮件的功能。

1. 支持使用Gmail服务器发送邮件
2. 支持本机SMTP服务发送邮件（查看本机服务： netstat -lntp, 查看端口25是否有smtp服务）


> **访问我的博客站点：http://www.lidezheng.net**



