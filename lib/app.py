# -*- coding: utf-8 -*-

from lib.error import UnsupportedCommandError, InvalidArgumentValueError
from lib.user_interface import UserInterface

class App(object):
    handlers = []

    @classmethod  # register single or multiple handlers to the application
    def register_handlers(cls, *handlers):
        cls.handlers = list(handlers)

    def __init__(self, broker):
        # broker: string, the url of the broker(AMQP server host)
        self.broker = broker
        self.terminated = False  # if the app has terminated its event loop
        self.connection = None
        self.channel = None

    @staticmethod
    def welcome():
        UserInterface.output("Hello World")

    def event_loop(self):
        # event_loop starts a event loop to "read - parse - handle - output"
        while not self.terminated:
            cmd = UserInterface.read()
            try:
                if len(cmd) == 0:
                    UserInterface.output("Nothing entered, please type any command")
                    continue

                if cmd.split()[0] == "exit":
                    UserInterface.output("Oops! Please don't go... /(ㄒoㄒ)/~~")
                    self.terminated = True
                    continue

                self.dispatch(cmd)
            except UnsupportedCommandError:
                UserInterface.output("Unsupported Command: {}".format(cmd))
            except InvalidArgumentValueError as e:
                UserInterface.output(e.message)

    def dispatch(self, cmd):
        # dispatch forwards the cmd and its arguments to corresponding handler
        cmd, arguments = cmd.split()[0], cmd.split()[1:]
        for handler in App.handlers:
            if cmd == handler.group + "." + handler.name:
                return handler(channel=self.channel, arguments=arguments).run()
        raise UnsupportedCommandError
