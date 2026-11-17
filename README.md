# Smart Home Hub System (CLI)

**Course:** Ohjelmoinnin perusteet (Basics of Programming)  
**Author:** Petra Paavola  

---

## 1. Project Overview & Idea

### What is this application?
The **Smart Home Hub System** is an interactive command-line application that simulates a centralized home automation controller. Users can monitor and control smart devices across multiple rooms (such as lights, thermostats, smart locks, and security cameras), activate pre-configured scenes (e.g., *"Night Mode"* or *"Away Mode"*), and view real-time energy consumption summaries.

### Key Features
- **Room-by-Room Device Control:** Toggle smart lights, adjust thermostat temperatures, and lock or unlock doors in specific rooms.
- **Automation Scenes (Macros):** Apply global presets with one command—such as turning off all lights, lowering heating, and locking all doors when leaving home.
- **Live Status Dashboard & Energy Monitor:** Displays a formatted overview of all active devices and calculates current power usage in watts.
- **Event Log:** Keeps a chronological history of all state changes during the session (e.g., `"Living Room lights turned ON"`).
- **Input Validation & Error Handling:** Safely handles invalid menu selections, out-of-range temperatures, and typos without crashing.

### Technical Implementation
Built in **Python 3**, the program separates responsibilities into clean, modular subroutines (functions):
- **Data Structures:** Uses nested dictionaries (`dict`) to store rooms, devices, states, and wattage ratings, alongside a `list` to record the session activity log.
- **Control Flow & Logic:** Driven by a main `while` loop and `if-elif-else` branching for menu navigation, combined with `for` loops to iterate through rooms during scene activations and status reports.

---

## 2. How to Run the Program

### Prerequisites
- Python 3.8 or newer installed on your computer.
- No external third-party libraries required.

### Installation & Startup
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/petraemmii/pythonbasics]
Navigate into the project directory:

Bash
cd pythonbasics
Launch the application from the terminal (use python3 on macOS/Linux if needed):

Bash
python main.py
3. Program Logic (Flowchart)
The flowchart below illustrates the main menu loop, user input validation, device/scene control branches, and exit flow:

4. Video Demonstration
Watch a walkthrough of the Smart Home Hub in action along with a review of the source code structure:

YouTube Video Demo: [Watch the Demo Video Here]([Insert your YouTube link here])

5. Code Documentation (PyDoc - Bonus)
Every function in the codebase is documented using standard Python docstrings. The HTML documentation was generated with PyDoc and is included in the repository (docs/main.html), or can be regenerated via terminal:

Bash
python -m pydoc -w main