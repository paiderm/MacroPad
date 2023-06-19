# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Visual Studio', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'BrkPnt', [Keycode.F9]),                
        (0x004000, 'Cmt', [Keycode.CONTROL, Keycode.K, Keycode.FORWARD_SLASH]),
        (0x400000, 'Stop', [Keycode.SHIFT, Keycode.F5]),      
        # 2nd row ----------
        (0x000040, 'Rename', [Keycode.F2]),
        (0x202000, '', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x004000, 'Cont.', [Keycode.F5]),                     
        # 3rd row ----------
        (0x000040, '', [Keycode.CONTROL, 'r']),
        (0x000040, '', [Keycode.ALT, Keycode.HOME]),
        (0xe9cd02, 'S Over', [Keycode.F10]),
        # 4th row ----------
        (0xe900e9, 'RI', [Keycode.CONTROL, Keycode.SHIFT, Keycode.R, Keycode.I]),   # Adafruit in new window
        (0x800000, '', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0xe9cd02, 'S Into', [Keycode.F11]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
