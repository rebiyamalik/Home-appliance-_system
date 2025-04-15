from home_appliance_system import HomeApplianceSystem
from appliance import Appliance

def main():
    # Create appliances
    light = Appliance("Light")
    fan = Appliance("Fan")
    heater = Appliance("Heater")

    # Create home appliance system
    home_system = HomeApplianceSystem()

    # Add appliances to the system
    home_system.add_appliance(light)
    home_system.add_appliance(fan)
    home_system.add_appliance(heater)

    # Control appliances
    home_system.control_appliance("Light", "on")
    home_system.control_appliance("Fan", "off")
    home_system.control_appliance("Heater", "on")

    # Show the status of all appliances
    home_system.show_status()

if __name__ == "__main__":
    main()