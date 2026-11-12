"""
knob_reader.py - reads the X and Y potentiometers and turns them into
a target pen position (x, y) in mm on the paper.
Owner: Klara Kerekes
"""


def init_knobs(x_pin, y_pin):
    """
    Owner: Klara Kerekes
    Inputs:  x_pin, y_pin (int) - GPIO numbers of the two pots.
    Outputs: (x_adc, y_adc) tuple of machine.ADC objects.
    Operation: creates one ADC object per pin so the knobs can be read.
    """
    pass


def read_raw(adc):
    """
    Owner: Klara Kerekes
    Inputs:  adc (machine.ADC) - one knob.
    Outputs: int 0 to 65535 - raw knob reading.
    Operation: calls adc.read_u16() and returns the value.
    """
    pass


def smooth_reading(history, new_value, size):
    """
    Owner: Klara Kerekes
    Inputs:  history (list of int) - recent readings, modified in place;
             new_value (int) - newest reading; size (int) - max samples kept.
    Outputs: int - average of the readings in history.
    Operation: appends new_value, drops the oldest if longer than size,
               returns the average to remove knob jitter.
    """
    pass


def map_range(value, in_min, in_max, out_min, out_max):
    """
    Owner: Klara Kerekes
    Inputs:  value (number) and the input/output ranges (numbers).
    Outputs: float - value scaled linearly into [out_min, out_max].
    Operation: linear interpolation, clamped to the output range.
    """
    pass


def read_target_xy(x_adc, y_adc, x_hist, y_hist):
    """
    Owner: Klara Kerekes
    Inputs:  x_adc, y_adc (machine.ADC); x_hist, y_hist (list) - smoothing buffers.
    Outputs: (x_mm, y_mm) tuple of floats - target pen position on the paper.
    Operation: read_raw -> smooth_reading -> map_range from 0..65535
               to the X_MIN..X_MAX / Y_MIN..Y_MAX drawing area.
    """
    pass
