"""
jig_settings.py - constants for the PicoSketch brachiograph.
Owner: Samith Fernando
No functions: pin numbers, servo calibration and arm geometry only.
Values marked TODO are measured on the jig during calibration (test 3).
"""

# Input pins (accessory board)
X_POT_PIN = 26          # ADC0, horizontal knob
Y_POT_PIN = 27          # ADC1, vertical knob
PEN_SWITCH_PIN = 22     # TODO: confirm on accessory board

# Servo PWM pins
SHOULDER_PIN = 0        # TODO: confirm on jig
ELBOW_PIN = 1
PEN_PIN = 2
SERVO_FREQ_HZ = 50

# Servo calibration: duty_u16 at 0 and 180 degrees (TODO: measure)
SERVO_CAL = {
    "shoulder": {"duty_0": 1638, "duty_180": 8192},
    "elbow":    {"duty_0": 1638, "duty_180": 8192},
    "pen":      {"duty_0": 1638, "duty_180": 8192},
}
PEN_UP_ANGLE = 30       # TODO: tune
PEN_DOWN_ANGLE = 0

# Arm geometry (mm)
UPPER_ARM_MM = 155.0
FOREARM_MM = 155.0
SHOULDER_XY = (-50.0, 139.5)

# Drawing area on the paper (mm)
X_MIN, X_MAX = 0.0, 215.0
Y_MIN, Y_MAX = 0.0, 279.0

# Knob smoothing and loop timing
SMOOTH_SAMPLES = 8
DEBOUNCE_MS = 50
LOOP_DELAY_MS = 20
