# -*- coding: utf-8 -*-

"""
Main module
"""

from cpu import Cpu
from memory import Memory

def main():
    rom_path = 'C:/Users/Simon/Desktop/Coding/xd_gb/xd_gb/roms/pokemon.gb'
    with open(rom_path, 'rb') as rom_file:
        rom = [i for i in rom_file.read()]
    memory = Memory(rom)
    cpu = Cpu(memory)

    # Infinite game loop
    try:
        while cpu.state != "QUIT":
            if cpu.state == "RUN":
                cpu.run()
    except KeyboardInterrupt as e:
        raise KeyboardInterrupt('User interrupt')

if __name__ == '__main__':
    main()

