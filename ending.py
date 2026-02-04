from nicegui import ui
import styles

def show_summary(state):
    """Replaces the timer with a 'Mission Accomplished' report."""
    # Clear the timer area
    state.timer_container.clear()
    
    with state.timer_container:
        with ui.card().classes(f'{styles.CARD_DARK} {styles.ACCENT_BORDER} border w-full p-8 items-center animate-fade-in'):
            ui.icon('check_circle', color='cyan').classes('text-6xl mb-4')
            ui.label('MISSION ACCOMPLISHED').classes('text-white text-2xl font-black tracking-widest')
            
            ui.separator().classes('my-4 opacity-20')
            
            with ui.column().classes('items-center'):
                ui.label('OBJECTIVE COMPLETED:').classes('text-gray-400 text-xs')
                ui.label(state.current_goal.upper()).classes(f'{styles.ACCENT_CYAN} text-xl font-bold mt-1')
            
            ui.label('Thank you for your focus. Your brain deserves a break!').classes('text-gray-500 mt-6 italic')
            
            # Button to go back and start a new one
            ui.button('NEW MISSION', on_click=lambda: ui.navigate.to('/'))\
                .props('unelevated color=cyan-5 text-color=black').classes('mt-8 px-10')