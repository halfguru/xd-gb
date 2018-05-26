# -*- coding: utf-8 -*-

"""
512 Opcodes Instruction Set
"""

from registers import Registers

class Opcodes():
    def __init__(self, pc):
        self.pc = pc
        self.opcodes_table = {
            0x00: self.NOP_00,
        }
    
    def get_opcodes_table(self):
        return self.opcodes_table

    def NOP_00(self):
        """
        00 NOP
        """
        self.pc +=1
        return 0

