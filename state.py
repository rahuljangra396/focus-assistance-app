from nicegui import ui

class AppState:
    def __init__(self):
        # UI Element References (Filled by ui_components.py)
        self.timer_label = None
        self.goal_input = None
        self.duration_select = None
        self.start_btn = None
        
        # Data Logic
        self.is_running = False
        self.seconds_left = 25 * 60
        self.current_goal = ""
        # Add this to your AppState class in state.py
        self.timer_container = None