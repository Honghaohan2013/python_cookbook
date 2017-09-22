#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
使用对象的上下文管理，保证使用后释放资源
保证在需要时建立连接（惰性计算）
"""

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


class LazyConnectionFactory:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address= address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))

    conn = LazyConnectionFactory(('www.python.org', 80))
    with conn as s1:
        pass
        with conn as s2:
            pass
