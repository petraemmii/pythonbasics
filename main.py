def main():
    # 1. Create the nested dictionary for our smart home
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

    # Create an empty list to record our event log later
    event_log = []

    print("Welcome to the Smart Home Hub!")

    # 2. Main menu loop (repeats until user chooses 5)
    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Dashboard & Energy Usage")
        print("2. Control a Device")
        print("3. Activate Automation Scene")
        print("4. View Event Log")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print("-> Dashboard coming in Step 2!")
        elif choice == "2":
            print("-> Device control coming in Step 3!")
        elif choice == "3":
            print("-> Scenes coming in Step 4!")
        elif choice == "4":
            print("-> Event log coming in Step 4!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# Start the program
main()