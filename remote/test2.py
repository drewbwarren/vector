#!/usr/bin/env python

from multiprocessing import Process,Queue,Pipe
from test1 import f

import sys
sys.path.append('../../joystick/d452dc49c57e935db199f636058b7665/')
from js_linux import jsLoop

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "Hello"


    k = Process(target=jsLoop, args=(child_conn,))
    k.start()
    print(parent_conn.recv())
