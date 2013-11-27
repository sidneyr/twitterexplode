#! /usr/bin/python3
from gi.repository import Gtk

class HelloWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PyGrypt")

        self.button = Gtk.Button(label="Exit")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
        
    def on_button_clicked(self, widget):
        print("Ain't implemented yet")

win = HelloWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()