from nicegui import ui
import styles

def build_interface(state):
    """
    Builds the main UI layout based on a Bento Grid design.
    Accepts the 'state' object to link UI elements to the app logic.
    """
    
    # Set the global background color to the Deep Navy from styles
    ui.query('body').classes(styles.BG_DARK)
    
    # Smooth transition for theme switching
    ui.query('body').classes('transition-all duration-500')

    with ui.column().classes('w-full items-center p-8 min-h-screen'):
        
        # --- 1. HEADER SECTION ---
        with ui.row().classes('w-full max-w-5xl justify-between items-center mb-10'):
            with ui.row().classes('items-center gap-3'):
                # Logo Icon
                ui.label('GS').classes('text-white font-black text-2xl bg-blue-600 px-3 py-1 rounded-lg shadow-lg')
                ui.label('FOCUS ASSISTANT').classes('text-white text-xl font-light tracking-[0.2em]')
            
            # Theme Toggle Slider
            with ui.row().classes('items-center gap-3 bg-black/20 p-2 rounded-full px-4'):
                ui.icon('light_mode', color='white').classes('text-sm')
                ui.switch(on_change=ui.dark_mode().toggle).props('color=cyan')
                ui.icon('dark_mode', color='white').classes('text-sm')

        # --- 2. MAIN BENTO GRID ---
        with ui.row().classes('w-full max-w-5xl gap-6 items-stretch'):
            
            # LEFT SIDE: INTAKE ZONE (The Control Panel)
            with ui.card().classes(f'{styles.CARD_DARK} {styles.ACCENT_BORDER} border w-full md:w-1/3 p-8 rounded-2xl shadow-xl'):
                ui.label('SESSION GOAL').classes(f'{styles.ACCENT_CYAN} text-xs font-bold tracking-widest mb-4')
                
                state.goal_input = ui.input(placeholder='What are we achieving?') \
                    .props('dark standout color=cyan').classes('w-full')
                
                ui.label('SELECT DURATION').classes('text-gray-400 text-xs mt-8 mb-2 font-medium')
                state.duration_select = ui.select(
                    options={25: '25 Minutes', 45: '45 Minutes', 60: '60 Minutes'}, 
                    value=25
                ).props('dark flat color=cyan').classes('w-full bg-black/10 rounded-lg')

                ui.label('STATUS').classes('text-gray-400 text-xs mt-8 mb-2 font-medium')
                ui.label('READY TO START').classes('text-gray-500 text-sm italic')

            # RIGHT SIDE: ZEN TIMER (The central focus element)
            # We wrap this in a container assigned to state.timer_container for ending.py to use
            with ui.card().classes(f'{styles.CARD_DARK} {styles.ACCENT_BORDER} border flex-grow p-12 items-center justify-center rounded-2xl shadow-xl') as timer_container:
                state.timer_container = timer_container
                
                with ui.column().classes('items-center gap-8 w-full'):
                    # The Countdown Visualization
                    with ui.element('div').classes('relative flex items-center justify-center'):
                        # Subtle glowing background ring
                        ui.circular_progress(value=1.0, show_value=False) \
                            .props('size=320px thickness=0.04 color=cyan-4') \
                            .classes('absolute opacity-10 blur-sm')
                        
                        # Main Timer Label
                        state.timer_label = ui.label('25:00').classes('text-white text-9xl font-thin tracking-tighter')

                    # Action Button
                    state.start_btn = ui.button('START MISSION', icon='rocket_launch') \
                        .props('unelevated color=cyan-5 text-color=black size=lg') \
                        .classes('mt-6 px-12 py-3 font-bold rounded-xl hover:scale-105 transition-transform')

        # --- 3. FOOTER ---
        ui.label('STAY FOCUSED • WORK HARD • REST WELL').classes('text-gray-600 text-[10px] mt-12 tracking-[0.5em]')