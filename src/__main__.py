#!/usr/bin/env python

import MainWin
from gi.repository import Gtk,GObject


if (__name__== "__main__"):
    win = MainWin.MainWin()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
