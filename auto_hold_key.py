import keyboard


def auto_hold_key(hotkey, key):
    keyboard.wait(hotkey)
    keyboard.press(key)
    keyboard.wait(hotkey)
    keyboard.release(key)


while True:
    hotkey = "F9"
    key = "W"
    auto_hold_key(hotkey, key)
