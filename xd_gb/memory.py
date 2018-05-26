# -*- coding: utf-8 -*-

"""
Memory module
"""

class Memory():
    def __init__(self, rom):
        self.rom = rom

    def read(self, pc):
        # 16kB ROM Bank 0
        if pc < 0x4000: 
            return self.rom[pc]
        