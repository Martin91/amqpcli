# -*- coding: utf-8 -*-

import six

class UserInterface(object):
    @staticmethod  # return the user's input in string
    def read():
        if six.PY2:
            return raw_input()
        else:
            return input()

    @staticmethod  # print the result
    def output(result):
        print(result)
