#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Time    : 2024/10/25 14:46
Author  : ren
"""

import sanic

from src.sanic_nacos import NacosExt

app = sanic.Sanic(__name__)

from sanic_ext import Extend

Extend.register(NacosExt)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9001)
