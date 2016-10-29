#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lidezheng at 2016/10/29 下午9:32


import time
from easy_log import EasyLog

if __name__ == "__main__":

    logger = EasyLog("my_module")

    for i in xrange(1, 16):
        logger.critical("critical message %s" % i)
        time.sleep(1)