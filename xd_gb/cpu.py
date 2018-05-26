# -*- coding: utf-8 -*-

"""
CPU module
"""

from opcodes import Opcodes
from registers import Registers

class Cpu():
    def __init__(self, memory):
        self.state = 'RUN'
        self.memory = memory
        self.registers = Registers()
        self.pc = self.registers.get_pc()
        self.opcodes = Opcodes(self.pc)
        self.opcodes_table = self.opcodes.get_opcodes_table()
    
    def run(self):
        instruction = self.memory.read(self.pc)
        
        if instruction in self.opcodes_table:
            self.opcodes_table[instruction]
        else:
            print('Instruction %s is not implemented yet' % bin(instruction))
            self.pc +=1 
            return
        


