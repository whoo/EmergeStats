#!/usr/bin/env python

from gi.repository import Gtk,GObject
import re
import emerge


class MainWin(Gtk.Window):
    """
    GTK Windows definition.
    """
    def __init__(self):
        Gtk.Window.__init__(self,title="windows Update")
        self.set_border_width(10)
        self.set_default_size(200, 100)
        self.set_icon_name(Gtk.STOCK_EXECUTE)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Emerge Stats"
        self.set_titlebar(hb)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.button = Gtk.Button(stock=Gtk.STOCK_QUIT,use_stock=True)
        self.button.connect("clicked",self.on_button_clicked)

        self.label = Gtk.Label("Package")
        self.label.set_justify(Gtk.Justification.LEFT)

        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(True)
        self.scrolledwindow.set_vexpand(True)
        self.text= Gtk.TextView()
        self.text.set_wrap_mode(3)
        self.scrolledwindow.add(self.text)
        self.textbuffer = self.text.get_buffer()


        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)
        vbox.pack_start(self.label,True,True,0)
        vbox.pack_start(self.scrolledwindow,True,True,0)
        vbox.pack_start(self.button,True,True,0)

        self.timeout_id = GObject.timeout_add(500, self.on_timeout, None)

        self.stat=emerge.emerge()

        self.on_timeout(None)

    def on_button_clicked(self,widget):
        Gtk.main_quit()

    def on_timeout(self,data):
        if (self.stat.read()):
            self.textbuffer.insert_at_cursor(self.stat.lastline)
            self.stat.dump()
            adj=self.scrolledwindow.get_vadjustment()
            adj.set_value(adj.get_upper()+1)
        cur=self.stat.cur
        tot=self.stat.tot
        pkg=self.stat.pkg
        action=self.stat.action
        
        self.progressbar.set_fraction(cur/tot)
        self.progressbar.set_text("%d / %d"%(cur,tot))
        self.progressbar.set_show_text(True)
        self.label.set_text("%s %s"%(action,pkg))


        return True

if (__name__== "__main__"):
    win = MainWin()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
