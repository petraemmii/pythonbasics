"""Smart Home Hub Simulator.

A console-based home automation controller that lets users monitor room
devices, calculate live energy consumption, control individual switches,
locks and thermostats, trigger automation scenes and review a session log.
"""

def activate_scene(home, event_log):
    """Apply a multi-room automation preset and record the action.

    Args:
        home (dict): Nested dictionary storing all rooms and their devices.
        event_log (list): List of strings recording actions taken during the session.
    """
    print("\n--- Automation Scenes ---")
    print("1. Night Mode (Lights OFF, Heating 18°C, Doors LOCKED)")
    print("2. Away Mode (All switches OFF, Heating 16°C, Doors LOCKED)")
    print("3. Morning Mode (Main lights ON, Heating 21°C, Door UNLOCKED)")

    scene = input("Select a scene (1-3): ").strip()

# Night Mode: turn off all switches, lower heating to 18°C and lock doors
    if scene == "1":
        for devices in home.values():
            for info in devices.values():
                if info["type"] == "switch":
                    info["state"] = False
                elif info["type"] == "thermostat":
                    info["temp"] = 18
                elif info["type"] == "lock":
                    info["locked"] = True
        message = "Scene activated: Night Mode."
        print(message)
        event_log.append(message)

# Away Mode: turn off all switches, set eco heating to 16°C and lock doors
    elif scene == "2":
        for devices in home.values():
            for info in devices.values():
                if info["type"] == "switch":
                    info["state"] = False
                elif info["type"] == "thermostat":
                    info["temp"] = 16
                elif info["type"] == "lock":
                    info["locked"] = True
        message = "Scene activated: Away Mode."
        print(message)
        event_log.append(message)

# Morning Mode: warm home to 21°C, unlock front door and turn on main lights
    elif scene == "3":
        for devices in home.values():
            for info in devices.values():
                if info["type"] == "thermostat":
                    info["temp"] = 21
                elif info["type"] == "lock":
                    info["locked"] = False
        home["living room"]["lights"]["state"] = True
        home["kitchen"]["lights"]["state"] = True
        message = "Scene activated: Morning Mode."
        print(message)
        event_log.append(message)

    else:
        print("Invalid scene choice.")

def calculate_total_watts(home):
    """Calculate total active power consumption across all rooms.

    Args:
        home (dict): Nested dictionary storing all rooms and their devices.

    Returns:
        int: Total power usage in watts (W) for currently active devices.
    """
    total = 0
    # Loop through each room and device to sum wattage of active devices
    for devices in home.values():
        for info in devices.values():
            # Switches draw power only when turned ON
            if info["type"] == "switch" and info["state"]:
                total += info["watts"]
            # Thermostats draw heating power only when set above 18°C
            elif info["type"] == "thermostat" and info["temp"] > 18:
                total += info["watts"]
            # Smart locks draw continuous standby power
            elif info["type"] == "lock":
                total += info["watts"]
    return total


def display_dashboard(home):
    """Print the current status of every room, device and total power usage.

    Args:
        home (dict): Nested dictionary storing all rooms and their devices.
    """
    print("\n===============================")
    print("   SMART HOME DASHBOARD")
    print("===============================")

    # Iterate through each room and format each device according to its type
    for room, devices in home.items():
        print(f"\n[{room.title()}]")
        for device_name, info in devices.items():
            if info["type"] == "switch":
                status = "ON" if info["state"] else "OFF"
                print(f"  - {device_name.title()}: {status} ({info['watts']}W)")
            elif info["type"] == "thermostat":
                print(f"  - {device_name.title()}: {info['temp']}°C ({info['watts']}W)")
            elif info["type"] == "lock":
                status = "LOCKED" if info["locked"] else "UNLOCKED"
                print(f"  - {device_name.title()}: {status} ({info['watts']}W)")

    # Calculate and display combined active wattage
    total_watts = calculate_total_watts(home)
    print("\n-------------------------------")
    print(f"Total Active Power: {total_watts} W")
    print("===============================")


def control_device(home, event_log):
    """Prompt the user to select a room and device, then update its state.

    Args:
        home (dict): Nested dictionary storing all rooms and their devices.
        event_log (list): List of strings recording actions taken during the session.
    """
    print("\nAvailable rooms:", ", ".join(room.title() for room in home))
    # Normalize input with .strip().lower() so matching is case-insensitive
    room_choice = input("Enter room name: ").strip().lower()

    if room_choice not in home:
        print("Room not found.")
        return

    devices = home[room_choice]
    print("Available devices:", ", ".join(dev.title() for dev in devices))
    device_choice = input("Enter device name: ").strip().lower()

    if device_choice not in devices:
        print("Device not found.")
        return

    device = devices[device_choice]

    # Toggle boolean state for standard ON/OFF switches
    if device["type"] == "switch":
        device["state"] = not device["state"]
        status = "ON" if device["state"] else "OFF"
        message = f"{room_choice.title()} {device_choice.title()} turned {status}."
        print(message)
        event_log.append(message)

    # Toggle boolean state for smart door locks
    elif device["type"] == "lock":
        device["locked"] = not device["locked"]
        status = "LOCKED" if device["locked"] else "UNLOCKED"
        message = f"{room_choice.title()} {device_choice.title()} is now {status}."
        print(message)
        event_log.append(message)

    # Validate numeric input and safe temperature range (15–28°C) for thermostats
    elif device["type"] == "thermostat":
        try:
            new_temp = int(input("Enter target temperature (15-28 °C): ").strip())
            if 15 <= new_temp <= 28:
                device["temp"] = new_temp
                message = f"{room_choice.title()} {device_choice.title()} set to {new_temp}°C."
                print(message)
                event_log.append(message)
            else:
                print("Temperature must be between 15 and 28 °C.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_event_log(event_log):
    """Display all actions recorded during the current session.

    Args:
        event_log (list): List of strings recording actions taken during the session.
    """
    print("\n===============================")
    print("\n===============================")
    print("       SESSION EVENT LOG")
    print("===============================")
    if not event_log:
        print("No actions recorded yet.")
    else:
        for entry in event_log:
            print(f" - {entry}")
    print("===============================")
def main():
    """Initialize smart home state and run the interactive main menu loop."""
    # Nested dictionary storing rooms, devices, states and power ratings (watts)
    home = {
        "living room": {
            "lights": {"type": "switch", "state": True, "watts": 45},
            "thermostat": {"type": "thermostat", "temp": 21, "watts": 1200},
        },
        "kitchen": {
            "lights": {"type": "switch", "state": False, "watts": 60},
            "coffee maker": {"type": "switch", "state": False, "watts": 900},
        },
        "hallway": {
            "lights": {"type": "switch", "state": True, "watts": 20},
            "front door lock": {"type": "lock", "locked": True, "watts": 5},
        },
    }

    # Empty list to store chronological log messages during the session
    event_log = []

    print("Welcome to the Smart Home Hub!")

    # Main menu loop repeats until the user selects option 5 to exit
    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Dashboard & Energy Usage")
        print("2. Control a Device")
        print("3. Activate Automation Scene")
        print("4. View Event Log")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            display_dashboard(home)
        elif choice == "2":
            control_device(home, event_log)
        elif choice == "3":
            activate_scene(home, event_log)
        elif choice == "4":
            display_event_log(event_log)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# Entry point: start the Smart Home Hub program
if __name__ == "__main__":
    main() 