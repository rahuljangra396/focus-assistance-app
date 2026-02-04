from nicegui import ui

def toggle_timer(state):
    """Starts or pauses the focus session."""
    if not state.goal_input.value:
        ui.notify('Please set a mission goal first!', type='warning', position='top')
        return

    state.is_running = not state.is_running
    
    if state.is_running:
        # Lock the UI so the user can't change the goal during focus
        state.current_goal = state.goal_input.value
        state.goal_input.disable()
        state.duration_select.disable()
        state.start_btn.text = 'PAUSE MISSION'
        state.start_btn.props('color=orange text-color=white')
        ui.notify(f'Mission Started: {state.current_goal}', color='cyan')
    else:
        state.start_btn.text = 'RESUME MISSION'
        state.start_btn.props('color=cyan text-color=black')

def update_timer(state):
    """The heartbeat function called every second by main.py."""
    if state.is_running and state.seconds_left > 0:
        state.seconds_left -= 1
        
        # Calculate minutes and seconds
        mins, secs = divmod(state.seconds_left, 60)
        state.timer_label.text = f'{mins:02d}:{secs:02d}'
        
        # When time runs out
        if state.seconds_left == 0:
            state.is_running = False
            finish_session(state)

def finish_session(state):
    """Triggers when the timer hits zero."""
    ui.notify('MISSION ACCOMPLISHED!', type='positive', sticky=True, position='center')
    state.start_btn.text = 'START NEW MISSION'
    state.start_btn.props('color=green')
    # Re-enable inputs for the next round
    state.goal_input.enable()
    state.duration_select.enable()
    import ending

def finish_session(state):
    state.is_running = False
    # Call our new ending screen!
    ending.show_summary(state)