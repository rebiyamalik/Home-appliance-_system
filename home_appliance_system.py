# home_system.py
# Modified by: Arfat-Anam (GitHub)
# Description: Enhanced HomeApplianceSystem with added features and improved formatting.


from appliance import Appliance

class HomeApplianceSystem:
    def __init__(self):
        # Stores appliance objects with their names as keys
        self.appliances = {}

    def add_appliance(self, appliance):
        """Add a new appliance to the system."""
        if appliance.name not in self.appliances:
            self.appliances[appliance.name] = appliance
            print(f"✅ {appliance.name} added to the system.")
        else:
            print(f"⚠️ {appliance.name} is already in the system.")
def rename_appliance(self, old_name, new_name):
    if old_name in self.appliances and new_name not in self.appliances:
        self.appliances[new_name] = self.appliances.pop(old_name)
        self.appliances[new_name].name = new_name
        print(f"🔁 Renamed '{old_name}' to '{new_name}'.")
    else:
        print("⚠️ Cannot rename: either old name doesn't exist or new name is already used.")

    def remove_appliance(self, appliance_name):
        """Remove an appliance from the system."""
        if appliance_name in self.appliances:
            del self.appliances[appliance_name]
            print(f"❌ {appliance_name} removed from the system.")
        else:
            print(f"⚠️ No appliance named '{appliance_name}' found.")

    def control_appliance(self, appliance_name, action):
        """Turn an appliance on or off."""
        appliance = self.appliances.get(appliance_name)
        if not appliance:
            print(f"❌ Appliance '{appliance_name}' not found.")
            return

        action = action.lower()
        if action == "on":
            appliance.turn_on()
        elif action == "off":
            appliance.turn_off()
        else:
            print(f"⚠️ Invalid action '{action}'. Use 'on' or 'off'.")

    def show_status(self):
        """Display the status of all appliances."""
        if not self.appliances:
            print("📭 No appliances added yet.")
        else:
            print("📋 Appliance Status:")
            for appliance in self.appliances.values():
                print(appliance.status())
