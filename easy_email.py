#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lidezheng at 2016/10/30 下午12:42


from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class EasyEmail:
    """
        邮件发送类
        使用Gmail账户发送邮件
    """
    email_from = ""                     # 邮箱账号
    email_from_password = ""            # 邮箱密码
    gmail_smtp_server = "smtp.gmail.com"

    def __init__(self):
        pass

    @staticmethod
    def send(from_name, subject, content, email_to):
        """
        :param from_name: 显示的发件人姓名
        :param subject: 邮件主题
        :param content: 邮件正文，支持html文本
        :param email_to: 收件人列表 List
        :return: True 成功， False 失败
        """
        if not from_name or not subject \
                or not content or not email_to:
            return False

        try:
            e_object = MIMEText(content, 'html', 'utf-8')
            e_object['From'] = EasyEmail._format_address(from_name + "<%s>" % EasyEmail.email_from)
            e_object['To'] = ','.join(email_to).encode('utf-8')
            e_object['Subject'] = Header(subject, 'utf-8').encode()

            # 发邮件
            server = smtplib.SMTP(EasyEmail.gmail_smtp_server, 587)
            # server.set_debuglevel(1)  # 用于打印交互信息
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(EasyEmail.email_from, EasyEmail.email_from_password)
            server.sendmail(EasyEmail.email_from, email_to, e_object.as_string())
            server.quit()
            print "done"
            return True
        except Exception, e:
            print e
            return False

    @staticmethod
    def _format_address(s):
        """
        :param s: 格式化发件人姓名
        :return:
        """
        name, e_address = parseaddr(s)
        e_address = e_address.encode('utf-8') if isinstance(e_address, unicode) else e_address
        return formataddr((Header(name, 'utf-8').encode(), e_address))


if __name__ == "__main__":
    email_to = ['lidezheng@conew.com']
    EasyEmail.send("脚本", "汇报", "<h1>hello, email.</h1>", email_to)