# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Microsoft Teams', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Cam', [Keycode.CONTROL, Keycode.SHIFT, Keycode.O]),                
        (0x004000, 'Mic', [Keycode.CONTROL, Keycode.SHIFT, Keycode.M]),
        (0x004000, 'Share', [Keycode.CONTROL, Keycode.SHIFT, Keycode.E]),      
        # 2nd row ----------
        (0x000000, '', [Keycode.F2]),
        (0x000000, '', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0xe9cd02, 'Vol +', [ConsumerControlCode.VOLUME_INCREMENT]),                     
        # 3rd row ----------
        (0x000000, '', [Keycode.CONTROL, 'r']),
        (0x000000, '', [Keycode.ALT, Keycode.HOME]),
        (0xe9cd02, 'Vol -', [ConsumerControlCode.VOLUME_DECREMENT]),
        # 4th row ----------
        (0x000000, '', [Keycode.CONTROL, Keycode.SHIFT, Keycode.R, Keycode.I]),   # Adafruit in new window
        (0x800000, 'Leave', [Keycode.CONTROL, Keycode.SHIFT, Keycode.H]),   # Digi-Key in new window
        (0x000000, '', [Keycode.F11]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
