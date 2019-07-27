# -*- coding: utf-8 -*-
import amqp

from lib.argument import StringArgument, BoolArgument
from lib.user_interface import UserInterface

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
        try:
            queue, msg_count, consumer_count = self.channel.queue_declare(**self.parsed_arguments)
        except amqp.exceptions.NotFound:
            UserInterface.output("Queue `{}` not found".format(self.parsed_arguments['queue']))
            return
        UserInterface.output("Queue: {}, msg_count: {}, consumer_count: {}".format(queue, msg_count, consumer_count))

class QueueDeleteHandler(Handler):
    group = 'queue'
    name = 'delete'

    meta_arguments = (
        StringArgument('queue', 'queue name'),
        BoolArgument('if_unused', 'delete only if unused'),
        BoolArgument('if_empty', 'delete only if empty'),
    )

    def run(self):
        msg_count = self.channel.queue_delete(**self.parsed_arguments)
        UserInterface.output("{} messages deleted".format(msg_count))

class QueueBindHandler(Handler):
    group = 'queue'
    name = 'bind'

    meta_arguments = (
        StringArgument('queue', 'queue name'),
        StringArgument('exchange', 'The name of the exchange to bind to'),
        StringArgument('routing_key', 'message routing key'),
    )

    def run(self):
        try:
            self.channel.queue_bind(**self.parsed_arguments)
            UserInterface.output('success')
        except BaseException as e:
            UserInterface.output(e.message)

class QueueUnbindHandler(Handler):
    group = 'queue'
    name = 'unbind'

    meta_arguments = (
        StringArgument('queue', 'queue name'),
        StringArgument('exchange', 'The name of the exchange to bind to'),
        StringArgument('routing_key', 'message routing key'),
    )

    def run(self):
        try:
            self.channel.queue_unbind(**self.parsed_arguments)
            UserInterface.output('success')
        except BaseException as e:
            UserInterface.output(e.message)
