# -*- coding: utf-8 -*-

"""
@author: neo
@software: PyCharm
@file: run.py.py
@time: 2023/7/11 17:16
"""

import seldom

if __name__ == '__main__':
    seldom.main(
        path="./test_dir/test_appointment.py",
        title="Auto Test",
        browser="chrome",
        debug=False
    )