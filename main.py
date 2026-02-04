from nicegui import ui
from state import AppState
import ui_components
import functions

# 1. Initialize the shared state
# This object will be passed around to all other files
state = AppState()

# 2. Build the UI
# We call the function from ui_components.py and pass our state
ui_components.build_interface(state)

# 3. Connect the Logic
# We tell the 'Start' button what to do when clicked
state.start_btn.on_click(lambda: functions.toggle_timer(state))

# 4. Set up the Background Heartbeat
# This runs every 1 second to update the numbers on the screen
ui.timer(1.0, lambda: functions.update_timer(state))

# 5. Launch the App
# native=True makes it look like a real desktop app
# port=8080 is standard for Docker deployment
ui.run(
    title='Focus Assistant',
    port=8080,
    dark=True,  # Start in dark mode by default
    reload=False # Set to True during development, False for Docker
)