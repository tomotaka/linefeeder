==========
linefeeder
==========

Installation
============


::

    $ pip install linefeeder



Basic Usage
===========

::

    from linefeeder import LineFeeder
    f = LineFeeder(encoding='utf-8', newline='\n')
    f.feed('aaa\nbbb\nccc\n')
    line1 = f.readline()  # => 'aaa\n'
    line2 = f.readline()  # => 'bbb\n'
    line3 = f.readline()  # => 'ccc\n'
    empty = f.readline()  # => Mone

    f.feed('ddd\neee\n')
    line4 = f.readline()  # => 'ddd\n'
    line5 = f.readline()  # => 'eee\n'

    # You can use LineFeeder as iterator.
    f2 = LineFeeder()
    f2.feed('aaa\nbbb\nccc\n')
    for line in f2:
        print line
    f2.feed('111\n222\n333\n')
    print list(f2)

    # LineFeeder doesn't buffer for next line break
    f3 = LineFeeder()  # encoding=utf-8, newline=\n
    f3.feed('Hello\nWOR')
    f3.readline()  # => 'Hello\n'
    f3.readline()  # => 'WOR'
    f3.readline()  # => None

    # If you want line buffering, use StrictLineFeeder.
    slf = StrictLineFeeder()
    slf.feed('Hello\nWOR')
    slf.readline()  # => 'Hello\n'
    slf.readline()  # => None
    slf.feed('LD\n')
    slf.finish()
    slf.readline()  # => 'WORLD\n'
    slf.readline()  # => None
    slf.feed('something')  # => AssertionError





