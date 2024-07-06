# Vintage Typewriter Emulator

Vintage Typewriter Emulator is a Python program that emulates the sound of a typewriter as you type. This project is a fork of the Typewriter Sounds Emulator, taking a new direction by enhancing the key mapping and sound playback to provide a more immersive vintage typewriter experience.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Key Mapping](#key-mapping)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features

- **Enhanced Key Mapping**: This fork has improved key mappings to include a wider range of keys and modes in Vim, ensuring each keypress triggers an appropriate sound.
- **Custom Sounds**: Plays specific sounds for different keys, such as space, enter, backspace, and more.
- **Mode-Specific Sounds**: Different sounds for keys depending on the mode in Vim (normal, insert, visual, etc.).
- **Bell Sound**: Plays a bell sound when the program starts and when the enter key is pressed in insert mode.

## Requirements

- Python 3.6 or higher

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/joshuadanpeterson/vintage-typewriter-emulator.git
   cd vintage-typewriter-emulator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Program**:

   ```bash
   python typewriter_sounds.py
   ```

   This will start the Vintage Typewriter Emulator. You should hear a bell sound indicating the program has started.

2. **Type in Your Editor**:

   - Ensure your text editor or terminal window is focused.
   - Type normally and enjoy the vintage typewriter sounds!

3. **Exit the Program**:
   - Press `Ctrl-C` to exit the program gracefully. A message will be displayed indicating the program has ended.

## Key Mapping

The program maps specific sounds to different keys as follows:

- **Space Key**: Plays `manual_space.wav`
- **Backspace Key**: Plays `manual_backspace.wav`
- **Bell Sound**: Plays `manual_bell.wav` on startup and when enter key is pressed in insert mode
- **Enter Key**: Plays `manual_return.wav` and `manual_feed.wav`
- **Default Key Sound**: Plays `manual_key.wav`
- **Page Up, Page Down, Home, End Keys**: Plays `manual_load_long.wav`
- **Shift Key, Arrow Keys, Escape Key, 'i' and 'a' in Normal Mode, and Number Keys in Normal Mode**: Plays `manual_shift.wav`

## Acknowledgements

- Original project by Manuel Arturo Izquierdo (aizquier@gmail.com)
- Forked from the [Typewriter Sounds Emulator](https://github.com/akshith6212/typewriter-sounds) project
- Sound samples sourced from [freesound.org](https://www.freesound.org/), some of which have been modified for this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
