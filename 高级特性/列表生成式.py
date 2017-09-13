# -*- coding:utf-8 -*-

d = {'v': 'E', 'w': 'D', 'x': 'A', 'y': 'B', 'z': 'C'}

for k, v in d.iteritems():
    print k, '=', v

for k in d.iteritems():
    print k
