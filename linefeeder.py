#!/usr/bin/python
# -*- coding: utf-8 -*-


class LineFeeder(object):

    def __init__(self, encoding='utf-8', newline='\n'):
        self._encoding = encoding
        self._newline = newline
        self._newline_len = len(newline)
        self._buffer = ''

    def feed(self, chunk):
        self._buffer += chunk

    def readline(self):
        if self._buffer == '':
            return None

        idx = self._buffer.find(self._newline)
        if idx == -1:
            rest = self._buffer
            self._buffer = ''
            return rest

        line = self._buffer[0:idx+self._newline_len]
        rest = self._buffer[idx + self._newline_len:]
        self._buffer = rest
        return line.decode(self._encoding)

    def next(self):
        line = self.readline()
        if not line:
            raise StopIteration()
        return line

    def __iter__(self):
        return self


class StrictLineFeeder(LineFeeder):

    def __init__(self, encoding='utf-8', newline='\n'):
        super(StrictLineFeeder, self).__init__(encoding, newline)
        self._is_finished = False

    def feed(self, chunk):
        assert not self._is_finished
        super(StrictLineFeeder, self).feed(chunk)

    def readline(self):
        if self._buffer == '':
            return None

        idx = self._buffer.find(self._newline)
        if idx == -1:
            if not self._is_finished:
                return None
            else:
                rest = self._buffer
                self._buffer = ''
                return rest

        line = self._buffer[0:idx + self._newline_len]
        rest = self._buffer[idx + self._newline_len:]
        self._buffer = rest
        return line.decode(self._encoding)

    def finish(self):
        self._is_finished = True
