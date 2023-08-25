# -*- coding: utf-8 -*-

"""
@author: neo
@software: PyCharm
@file: test_appointment.py
@time: 2023/7/11 17:24
"""
import time

import seldom
from seldom import file_data


class AppointmentTest(seldom.TestCase):
    @file_data("test_data.yaml", key="login")
    def test_create_appointment(self, username, password):
        """create appointment test"""
        self.open("https://go.t2.moego.pet/")
        self.type(id_="email", text=username)
        self.type(id_="password", text=password)
        self.click(tag="button")
        time.sleep(3)
