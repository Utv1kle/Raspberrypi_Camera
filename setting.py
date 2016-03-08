#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os,sys

def First():
	f = open("setting.txt", 'w')
	f.close()
	#win.fullscreen()

class Button(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Button Demo")
		self.set_border_width(100)

		hbox = Gtk.Box(spacing=6)
		self.add(hbox)

		button = Gtk.Button.new_with_label("Save")
		button.connect("clicked", self.Save)
		button.props.valign = Gtk.move
		hbox.pack_start(button, True, True, 0)
		
		button = Gtk.Button.new_with_mnemonic("Cancel")
		button.connect("clicked", self.Cancel)
		button.PositionType.BOTTOM()
		hbox.pack_start(button, True, True, 0)

	def Save(self, button):
		print("\"Click me\" button was clicked")
	
	def Cancel(self, button):
		print("CanCel")
		Gtk.main_quit()
First()
win = Button()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
