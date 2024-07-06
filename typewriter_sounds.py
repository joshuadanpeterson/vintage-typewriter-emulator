from __future__ import print_function
import sys
import os
import pygame
from pynput import keyboard


class TypeWriterSounds:
    """
    Typewriter sounds emulator for Python
    =====================================

    This program plays typewriter sounds each time a key is pressed, giving
    the user the vintage experience of an old typewriter machine.

    Sound samples come from https://www.freesound.org/, some were modified
    for this project.

    Requeriments
    ------------

    -  Python 3.x
    -  `PyGame <http://pygame.org>`__ (for sound)
    -  `pynput <https://pypi.org/project/pynput/>`__ (for global key capture)

    Usage
    -----

    cd into the project's directory and type:

    ::

        $ python typewriter_sounds.py

    to stop the program, just type CTRL-C.

    Author
    ------

    Manuel Arturo Izquierdo aizquier@gmail.com

    """

    def __init__(self):
        # Initializes pygame mixer. A buffer of 512 bytes is required for better performance
        pygame.mixer.init(buffer=512)

        self.bellcount = 0

        # Preloads sound samples
        self.keysounds = {
            "load": pygame.mixer.Sound("samples/manual_load_long.wav"),
            "shift": pygame.mixer.Sound("samples/manual_shift.wav"),
            "delete": pygame.mixer.Sound("samples/manual_backspace.wav"),
            "space": pygame.mixer.Sound("samples/manual_space.wav"),
            "key": pygame.mixer.Sound("samples/manual_key.wav"),
            "enter": pygame.mixer.Sound("samples/manual_return.wav"),
            "bell": pygame.mixer.Sound("samples/manual_bell.wav"),
        }

        print("TypeWriter Sounds Emulator. v1.0")
        print("type now and enjoy the vintage experience!...")

        self.run()

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()

    def on_press(self, key):
        try:
            if hasattr(key, "char") and key.char is not None:
                keyname = key.char
            else:
                keyname = key.name

            # Plays an audio sample according to the keyname
            if keyname == "enter":
                self.keysounds["enter"].play()
                self.bellcount = 0  # Reset bellcount on new line
                self.keysounds["bell"].play()  # Play bell sound on new line
            elif keyname == "space":
                self.keysounds["space"].play()
                self.bellcount += 1
            elif keyname in ("delete", "backspace"):
                self.keysounds["delete"].play()
                self.bellcount -= 1
                if self.bellcount <= 0:
                    self.bellcount = 0
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
                self.bellcount += 1

            # After 70 consecutive keypresses, play the bell sound
            if self.bellcount == 70:
                self.keysounds["bell"].play()
                self.bellcount = 0

        except AttributeError:
            pass


if __name__ == "__main__":
    TypeWriterSounds()
