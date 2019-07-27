# -*- coding: utf-8 -*-

class AMQPClientError(StandardError):
    pass

class InvalidArgumentValueError(AMQPClientError):
    pass

class UnsupportedCommandError(AMQPClientError):
    pass
