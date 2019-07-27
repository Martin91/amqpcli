# -*- coding: utf-8 -*-

from lib.argument import StringArgument, BoolArgument

class Handler(object):
    group = None
    name = None

    def __init__(self, channel, arguments):
        self.channel = channel
        self.parsed_arguments = {}
        self.parse_arguments(arguments)

    def parse_arguments(self, arguments):
        if len(arguments) == 0:
            return

        index = 0
        for argument in arguments:
            meta_argument = self.__class__.meta_arguments[index]
            self.parsed_arguments[meta_argument.name] = meta_argument.parse(argument)
            index += 1

    def run(self):
        raise NotImplementedError


class QueueDeclareHandler(Handler):
    group = "queue"
    name = "declare"

    meta_arguments = (
        StringArgument("queue", "queue name"),
        BoolArgument("passive", "is passive queue"),
        BoolArgument("durable", "is durable queue"),
        BoolArgument("exclusive", "is exclusive queue"),
        BoolArgument("auto_delete", "the queue could be automatically deleted"),
    )

    def run(self):
        print "hello"
