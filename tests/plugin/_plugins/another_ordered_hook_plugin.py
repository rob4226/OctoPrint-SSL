# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

def callback(*args, **kwargs):
	pass

__plugin_hooks__ = {
	"some.ordered.callback": (callback, 100)
}
