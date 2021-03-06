#! /usr/bin/python3
# A truly disgusting PyGTK button conglomeration, will try and clean this
# up sometime

from gi.repository import Gtk

class HelloWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Button Demo")
        self.set_size_request(250, 250)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        self.normal_buttons_label = Gtk.Label(label="Normal Buttons Label")
        vbox.pack_start(self.normal_buttons_label, True, True, 5)

        hbox = Gtk.Box()
        vbox.add(hbox)

        self.click_button = Gtk.Button(label="Click Me")
        self.click_button.connect("clicked", self.click_button_clicked)
        hbox.pack_start(self.click_button, True, True, 4)

        self.open_button = Gtk.Button(label="Open")
        self.open_button.connect("clicked", self.open_button_clicked)
        hbox.pack_start(self.open_button, True, True, 4)

        self.close_button = Gtk.Button(label="Close")
        self.close_button.connect("clicked", self.close_button_clicked)
        hbox.pack_start(self.close_button, True, True, 4)

        label = Gtk.Label(label="Toggle Buttons Label")
        vbox.pack_start(label, True, True, 5)

        hbox = Gtk.Box(spacing=5)
        vbox.pack_start(hbox, True, True, 0)

        self.toggle_button1 = Gtk.ToggleButton(label="Button 1")
        self.toggle_button1.set_active(is_active=True)
        self.toggle_button1.connect("toggled", self.toggle_button1_state)
        hbox.pack_start(self.toggle_button1, True, True, 4)

        self.toggle_button2 = Gtk.ToggleButton(label="Button 2")
        self.toggle_button2.set_active(is_active=False)
        self.toggle_button2.connect("toggled", self.toggle_button2_state)
        hbox.pack_start(self.toggle_button2, True, True, 4)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 10)

        label = Gtk.Label(label="Enable the check box?")
        hbox.pack_start(label, True, True, 5)

        self.check_button = Gtk.CheckButton()
        self.check_button.connect("toggled", self.check_button_toggle)
        hbox.pack_start(self.check_button, True, True, 0)

        label = Gtk.Label(label="Select your choice of radio buttons:")
        vbox.pack_start(label, True, True, 0)


        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 0)

        self.radio_button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Button One")
        self.radio_button1.connect("toggled", self.radio_button_toggle, "1")    
        hbox.pack_start(self.radio_button1, False, False, 0)

        self.radio_button2 = Gtk.RadioButton.new_with_label_from_widget(self.radio_button1, "Button Two")
        self.radio_button2.connect("toggled", self.radio_button_toggle, "2")
        hbox.pack_start(self.radio_button2, False, False, 0)

        self.radio_button3 = Gtk.RadioButton.new_with_label_from_widget(self.radio_button1, "Button Three")
        self.radio_button3.connect("toggled", self.radio_button_toggle, "3")
        hbox.pack_start(self.radio_button3, False, False, 0)

        link = Gtk.LinkButton("https://github.com/JamesWrigley", "Bad Code Example")
        vbox.pack_start(link, False, False, 0)

        label = Gtk.Label(label="SpinButton Demonstration")
        vbox.pack_start(label, True, True, 15)

        hbox = Gtk.Box(spacing=20)
        vbox.pack_start(hbox, True, True, 0)

        self.adjustment = Gtk.Adjustment(4, 0, 100, 2, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(self.adjustment)
        self.spinbutton.set_digits(2)
        hbox.pack_start(self.spinbutton, True, True, 20)

        self.check_numeric = Gtk.CheckButton("Numeric")
        self.check_numeric.connect("toggled", self.on_numeric_toggled)
        hbox.pack_start(self.check_numeric, True, True, 0)

        label = Gtk.Label(label="A switch button example")
        vbox.pack_start(label, True, True, 15)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 0)

        self.switch_button1_text = Gtk.Label(label="Switch One")
        hbox.pack_start(self.switch_button1_text, True, True, 10)

        self.switch_button1 = Gtk.Switch()
        self.switch_button1.set_active(True)
        self.switch_button1.connect("notify::active", self.on_switched, self.switch_button1_text.get_text())
        hbox.pack_start(self.switch_button1, True, True, 0)

        self.switch_button2_text = Gtk.Label(label="Switch Two")
        hbox.pack_start(self.switch_button2_text, True, True, 10)

        self.switch_button2 = Gtk.Switch()
        self.switch_button2.set_active(False)
        self.switch_button2.connect("notify::active", self.on_switched, self.switch_button2_text.get_text())
        hbox.pack_start(self.switch_button2, True, True, 0)

        label = Gtk.Label(label="Some spinning action")
        vbox.pack_start(label, True, True, 15)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 0)

        vbox_spinner1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox_spinner1, True, True, 0)

        # Have to declare this here and pack later, so spinner1.switch sees it
        self.spinner1 = Gtk.Spinner()

        self.spinner1_switch = Gtk.Switch()
        self.spinner1_switch.connect("notify::active", self.spinner_toggle, self.spinner1)
        vbox_spinner1.pack_start(self.spinner1_switch, True, True, 0)

        # Pack the spinner
        vbox_spinner1.pack_start(self.spinner1, True, True, 20)

        vbox_spinner2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox_spinner2, True, True, 0)

        # Declare second spinner here
        self.spinner2 = Gtk.Spinner()

        self.spinner2_switch = Gtk.Switch()
        self.spinner2_switch.connect("notify::active", self.spinner_toggle, self.spinner2)
        vbox_spinner2.pack_start(self.spinner2_switch, True, True, 0)

        # And pack second spinner
        vbox_spinner2.pack_start(self.spinner2, True, True, 20)

    def click_button_clicked(self, button):
        print("\"Click Me\" button was clicked")
        
    def open_button_clicked(self, button):
        print("\"Open\" button was clicked")
        
    def close_button_clicked(self, button):
        print("\"Close\" button was clicked")

    def toggle_button1_state(self, button):
        print("Button 1 is set to " + str(button.get_active()))

    def toggle_button2_state(self, button):
        print("Button 2 is set to " + str(button.get_active()))

    def check_button_toggle(self, button):
        print("Check button is set to" + str(button.get_active()))

    def radio_button_toggle(self, button, name):
        if button.get_active() == True:
            print("Button " + name + " is now active")

    def on_numeric_toggled(self, button):
        self.spinbutton.set_numeric(button.get_active())

    def on_switched(self, button, gparam, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print(str(name) + " is set " + state)

    def spinner_toggle(self, button, gparam, name):
        if button.get_active():
            name.start()
        else:
            name.stop()


win = HelloWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
