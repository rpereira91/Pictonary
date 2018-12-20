from phue import Bridge

class HueControl:
    
    def __init__(self,IP):
        self.b = Bridge(IP)
        # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
        # self.b.connect()
        self.b.register_app()
        # Get the bridge state (This returns the full dictionary that you can explore)
        self.b.get_api()

    def flash_blubs(self):
        self.b.set_light(3,'on',False)
        self.b.set_light(3,'on',True)
        self.b.set_light(3,'on',False)
        self.b.set_light(3,'on',True)