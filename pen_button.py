"""
pen_button.py - reads the pen switch, debounces it and toggles the
pen up/down state.
Owner: Klara Kerekes
"""


def init_button(pin):
    """
    Owner: Klara Kerekes
    Inputs:  pin (int) - GPIO number of the pen switch.
    Outputs: machine.Pin configured as input with pull-up.
    Operation: creates the Pin object for the switch.
    """
    pass


def is_pressed(button):
    """
    Owner: Klara Kerekes
    Inputs:  button (machine.Pin).
    Outputs: bool - True while the switch is held down.
    Operation: reads the pin; switch is active-low (0 = pressed).
    """
    pass


def debounce_press(button, last_state, last_time_ms, now_ms):
    """
    Owner: Klara Kerekes
    Inputs:  button (machine.Pin); last_state (bool) - previous stable state;
             last_time_ms (int) - time of last accepted change; now_ms (int).
    Outputs: (new_press, state, time_ms) - new_press is True only on a
             clean released-to-pressed edge.
    Operation: ignores changes within DEBOUNCE_MS of the last accepted one,
               so one physical press gives exactly one toggle.
    """
    pass


def toggle_pen(pen_down):
    """
    Owner: Klara Kerekes
    Inputs:  pen_down (bool) - current pen state.
    Outputs: bool - the opposite state.
    Operation: returns not pen_down.
    """
    pass
