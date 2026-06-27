class Memory:
    def __init__(self, size):
        self.data = [0] * size 

    def read(self,address):
        return self.data[address]
    
    def write(self, address, value):
        self.data[address] = value

class Register:
    def __init__(self):
        registers = {'R0': 0,
                     'R1': 0,
                     'R2': 0,
                     'R3': 0,
                     'R4': 0
                    }
        self.data = registers
    
    def read(self,name):
        return self.data[name]
    
    def write(self, name, value):
        self.data[name] = value

mem = Memory(100)
mem.write(10, 1)
print(mem.read(10))

reg = Register()
reg.write("R2", 99)
print(reg.read('R2'))

class CPU:
    def __init__(self):
        self.memory = Memory(256)
        self.register = Register()
        self.pc = 0
        self.running = False

    def execute(self, instruction):
        op = instruction[0] # first element is alywas instruction

        if op == 'LOAD':
            reg, value = instruction[1], instruction[2]
            self.register.write(reg, value)
        elif op == 'ADD':
            reg1, reg2 = instruction[1], instruction[2]
            a = self.register.read(reg1)
            b = self.register.read(reg2)
            self.register.write(reg1, a+b)
        elif op == 'SUB':
            reg1, reg2 = instruction[1], instruction[2]
            a = self.register.read(reg1)
            b = self.register.read(reg2)
            self.register.write(reg1, a - b)
        elif op == 'STORE':
            reg, address = instruction[1], instruction[2]
            value = self.register.read(reg)
            self.memory.write(address, value)
        elif op == 'HALT':
            self.running = False
        
    def run(self,program):
            self.running = True
            self.pc = 0

            while self.running:
                instruction = program[self.pc]
                self.execute(instruction)
                self.pc += 1
                print(f'Running: {instruction}')


cpu = CPU()
program = [("LOAD", 'R0', 5),
           ("LOAD", 'R1', 3),
           ("ADD", "R0", "R1"),
           ('STORE', 'R0', 50),
           ("HALT",)]
cpu.run(program)

print(cpu.register.read('R0'))
print(cpu.memory.read(50))