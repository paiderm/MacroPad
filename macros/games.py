# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Game', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'M1', [Keycode.ONE]),                
        (0x004000, 'M2', [Keycode.TWO]),
        (0x004000, 'M3', [Keycode.THREE]),      
        # 2nd row ----------
        (0x000040, 'Q', [Keycode.Q]),
        (0x400000, 'W', [Keycode.W]),
        (0x000040, 'E', [Keycode.E]),                     
        # 3rd row ----------
        (0x400000, 'A', [Keycode.A]),
        (0x400000, 'S', [Keycode.S]),
        (0x400000, 'D', [Keycode.D]),
        # 4th row ----------
        (0x000040, 'Shift', [Keycode.SHIFT]),   # Adafruit in new window
        (0x000040, 'C', [Keycode.C]),   # Digi-Key in new window
        (0x000040, 'R', [Keycode.R]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
