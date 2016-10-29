#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lidezheng at 2016/10/29 下午6:16


import logging
import logging.config
import yaml


class EasyLog:
    """
        日志类
    """
    with open('./logging.yaml') as fd:
        conf = yaml.load(fd)
    logging.config.dictConfig(conf)

    def __init__(self, log_filename):
        self.logger = logging.getLogger(log_filename)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def exception(self, message):
        self.logger.exception(message)
