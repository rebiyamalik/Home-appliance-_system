class Appliance:
    def init(self, name):
if not isinstance(name, str) or not name.strip():
raise ValueError("Appliance name must be a non-empty string.")
self.name = name.strip()
self.state = False # Appliance is off by default
    def turn_on(self):
        if not self.state:
            self.state = True
            print(f"{self.name} is now ON.")
        else:
            print(f"{self.name} is already ON.")

    def turn_off(self):
        if self.state:
            self.state = False
            print(f"{self.name} is now OFF.")
        else:
            print(f"{self.name} is already OFF.")

    def status(self):
        return f"{self.name} is {'ON' if self.state else 'OFF'}."
