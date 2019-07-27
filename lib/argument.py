# -*- coding: utf-8 -*-

from lib.error import InvalidArgumentValueError

class Argument(object):
    default = None

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc  # reserved design
        self._value = self.__class__.default

    def __str__(self):
        return "{}:{}".format(self.name, self.__class__.default)

    def parse(self, value):
        raise NotImplementedError("Not implemented")


class BoolArgument(Argument):
    default = False

    def parse(self, value):
        if value.lower() == "true":
            self._value = True
            return
        if value.lower() == "false":
            self._value = False
            return
        raise InvalidArgumentValueError("Not recognized value {} for {}".format(value, self.name))

class StringArgument(Argument):
    default = ""

    def parse(self, value):
        self._value = value
