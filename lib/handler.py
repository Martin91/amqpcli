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
        for meta_argument in self.meta_arguments:
            if index >= len(arguments):
                self.parsed_arguments[meta_argument.name] = meta_argument.default
            else:
                self.parsed_arguments[meta_argument.name] = meta_argument.parse(arguments[index])
            index += 1

    def run(self):
        raise NotImplementedError


class QueueDeclareHandler(Handler):
    group = "queue"
    name = "declare"

    meta_arguments = (
        StringArgument("queue", "queue name"),
        BoolArgument("passive", "is passive queue", default=True),
        BoolArgument("durable", "is durable queue"),
        BoolArgument("exclusive", "is exclusive queue"),
        BoolArgument("auto_delete", "the queue could be automatically deleted"),
    )

    def run(self):
        reply = self.channel.queue_declare(**self.parsed_arguments)
        print reply
