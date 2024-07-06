# typewriter_sounds.py - A typewriter sounds emulator

from __future__ import print_function
import sys
import os
import signal

# Suppress the pygame startup message
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
from pynput import keyboard


class TypeWriterSounds:
    def __init__(self):
        pygame.mixer.init(buffer=512)
        self.keysounds = {
            "load": pygame.mixer.Sound("samples/manual_load_long.wav"),
            "shift": pygame.mixer.Sound("samples/manual_shift.wav"),
            "delete": pygame.mixer.Sound("samples/manual_backspace.wav"),
            "space": pygame.mixer.Sound("samples/manual_space.wav"),
            "key": pygame.mixer.Sound("samples/manual_key.wav"),
            "enter": pygame.mixer.Sound("samples/manual_return.wav"),
            "bell": pygame.mixer.Sound("samples/manual_bell.wav"),
        }
        print("Typewriter Sounds Emulator")
        print("Type now and enjoy the vintage experience! Press Ctrl-C to exit.")
        self.keysounds["bell"].play()  # Play bell sound on startup

    def play_sound(self, keyname, mode):
        if keyname == "enter":
            self.keysounds["enter"].play()
        elif keyname == "space":
            self.keysounds["space"].play()
        elif keyname == "backspace":
            self.keysounds["delete"].play()
        elif keyname in ("esc", "up", "down", "left", "right") or (
            mode == "normal" and keyname in ("i", "a")
        ):
            self.keysounds["shift"].play()
        elif mode in ("normal", "visual", "operator_pending"):
            if keyname in (
                "h",
                "j",
                "k",
                "l",
                "W",
                "w",
                "e",
                "E",
                "b",
                "B",
                "0",
                "$",
                "gg",
                "G",
                "H",
                "M",
                "L",
                "zz",
                "zb",
                "zt",
                "ge",
                "gE",
                "/",
                "?",
                "n",
                "N",
                "*",
                "#",
                "aw",
                "iw",
                "as",
                "is",
                "ap",
                "ip",
                "a[",
                "i[",
                "%",
            ):
                self.keysounds["shift"].play()
            else:
                self.play_default_sound(keyname)
        elif mode == "insert":
            self.play_default_sound(keyname)

    def play_default_sound(self, keyname):
        if keyname in ("o", "O"):
            self.keysounds["enter"].play()
            self.keysounds["bell"].play()
        elif keyname == "delete":
            self.keysounds["delete"].play()
        elif keyname in (
            "up",
            "down",
            "left",
            "right",
            "ctrl_l",
            "ctrl_r",
            "shift_l",
            "shift_r",
            "alt_l",
            "alt_r",
            "tab",
            "caps_lock",
            "f1",
            "f2",
            "f3",
            "f4",
            "f5",
            "f6",
            "f7",
            "f8",
            "f9",
            "f10",
            "f11",
            "f12",
            "cmd",
            "esc",
        ):
            self.keysounds["shift"].play()
        elif keyname in ("page_up", "page_down", "home", "end"):
            self.keysounds["load"].play()
        else:
            self.keysounds["key"].play()

    def on_press(self, key):
        try:
            keyname = key.char if key.char else key.name

            # Determine mode based on key pressed
            if keyname in (
                "h",
                "j",
                "k",
                "l",
                "W",
                "w",
                "e",
                "E",
                "b",
                "B",
                "0",
                "$",
                "gg",
                "G",
                "H",
                "M",
                "L",
                "zz",
                "zb",
                "zt",
                "ge",
                "gE",
                "/",
                "?",
                "n",
                "N",
                "*",
                "#",
                "aw",
                "iw",
                "as",
                "is",
                "ap",
                "ip",
                "a[",
                "i[",
                "%",
                "i",
                "a",
            ):
                mode = "normal"
            elif keyname in ("V", "<C-v>"):
                mode = "visual"
            elif keyname in (":"):
                mode = "command"
            elif keyname in ("R"):
                mode = "replace"
            elif keyname in ("gh", "gH"):
                mode = "select"
            elif keyname in ("d", "y", "c", ">"):
                mode = "operator_pending"
            else:
                mode = "insert"

            self.play_sound(keyname, mode)
        except AttributeError:
            pass

    def start_listener(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        try:
            listener.join()
        except KeyboardInterrupt:
            self.keysounds["bell"].play()  # Play bell sound on exit
            print("\nProgram ended. Goodbye!")
            listener.stop()
            sys.exit(0)


def handle_sigint(signum, frame):
    sounds.keysounds["bell"].play()  # Play bell sound on exit
    print("\nProgram ended. Goodbye!")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_sigint)
    sounds = TypeWriterSounds()
    sounds.start_listener()
