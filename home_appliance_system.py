from appliance import Appliance

class HomeApplianceSystem:
    def __init__(self):
        self.appliances = {}

    def add_appliance(self, appliance):
        """Adds an appliance to the system."""
        if appliance.name not in self.appliances:
            self.appliances[appliance.name] = appliance
            print(f"{appliance.name} has been added to the system.")
        else:
            print(f"{appliance.name} is already in the system.")

    def control_appliance(self, appliance_name, action):
        """Controls an appliance (turn on/off)."""
        appliance = self.appliances.get(appliance_name)
        if appliance:
            if action == "on":
                appliance.turn_on()
            elif action == "off":
                appliance.turn_off()
            else:
                print(f"Invalid action '{action}' for {appliance_name}. Please use 'on' or 'off'.")
        else:
            print(f"Appliance {appliance_name} not found in the system.")

    def show_status(self):
        """Shows the status of all appliances."""
        if not self.appliances:
            print("No appliances are added to the system.")
        for appliance in self.appliances.values():
            print(appliance.status())

