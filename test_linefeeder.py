#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from nose.tools import eq_, raises


from linefeeder import LineFeeder, StrictLineFeeder


class LineFeederTestCase(TestCase):
    def test_readline1(self):
        f = LineFeeder()
        f.feed('hello\nHELLO\nBye')
        eq_(f.readline(), 'hello\n')
        eq_(f.readline(), 'HELLO\n')
        eq_(f.readline(), 'Bye')

        eq_(f.readline(), None)
        eq_(f.readline(), None)

    def test_readline2(self):
        f = LineFeeder()
        f.feed('')
        eq_(f.readline(), None)

    def test_readline3(self):
        f = LineFeeder(newline='\r\n')
        f.feed('hoge\r\nmoge\r\nfuga\r\n')
        eq_(f.readline(), 'hoge\r\n')
        eq_(f.readline(), 'moge\r\n')
        eq_(f.readline(), 'fuga\r\n')
        eq_(f.readline(), None)

    def test_iter1(self):
        f = LineFeeder()
        f.feed('hello\nHELLO\nBye')
        eq_(list(f), ['hello\n', 'HELLO\n', 'Bye'])

        f2 = LineFeeder()
        f.feed('')
        eq_(list(f), [])


class StrictLineFeederTestCase(TestCase):

    def test_readline1(self):
        f = StrictLineFeeder()
        f.feed('hello\nHE')
        eq_(f.readline(), 'hello\n')
        eq_(f.readline(), None)
        f.feed('LLO\n')
        eq_(f.readline(), 'HELLO\n')
        eq_(f.readline(), None)
        eq_(f.readline(), None)
        f.feed('hoge\n')
        eq_(f.readline(), 'hoge\n')
        eq_(f.readline(), None)
        eq_(f.readline(), None)

    def test_readline2(self):
        f = StrictLineFeeder()

        f.feed('hello\nHE')
        eq_(f.readline(), 'hello\n')
        eq_(f.readline(), None)
        f.feed('LLO\n')
        eq_(f.readline(), 'HELLO\n')
        eq_(f.readline(), None)
        eq_(f.readline(), None)
        f.feed('hoge\naiueo')
        f.finish()
        eq_(f.readline(), 'hoge\n')
        eq_(f.readline(), 'aiueo')
        eq_(f.readline(), None)
        eq_(f.readline(), None)

    @raises(AssertionError)
    def test_finish_and_feed(self):
        f = StrictLineFeeder()
        f.feed('hello\n')
        f.finish()
        f.feed('something')
