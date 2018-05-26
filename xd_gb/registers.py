# -*- coding: utf-8 -*-

"""
Registers
"""

class Registers():
    def __init__(self):
        self.pc = 0x100
    
    def get_pc(self):
        return self.pc